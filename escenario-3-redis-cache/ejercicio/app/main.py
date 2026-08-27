from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import redis
import psycopg2
import time
import json
import os

app = FastAPI()

redis_client = redis.Redis(
    host=os.environ.get('REDIS_HOST', 'redis'),
    port=int(os.environ.get('REDIS_PORT', 6379)),
    decode_responses=True
)

def obtener_conexion_db():
    return psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db'),
        port=os.environ.get('DB_PORT', 5432),
        user=os.environ.get('DB_USER', 'postgres'),
        password=os.environ.get('DB_PASSWORD', 'postgres'),
        dbname=os.environ.get('DB_NAME', 'cachedb')
    )

LIMITE_POR_MINUTO = 10

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    ip_cliente = request.client.host
    clave = f"rate_limit:{ip_cliente}"

    peticiones = redis_client.incr(clave)
    if peticiones == 1:
        redis_client.expire(clave, 60)

    if peticiones > LIMITE_POR_MINUTO:
        return JSONResponse(
            status_code=429,
            content={"detail": "Demasiadas solicitudes, intenta en un minuto"}
        )

    respuesta = await call_next(request)
    return respuesta

@app.get("/")
def index():
    return {"servicio": "App FastAPI con Redis + PostgreSQL", "status": "activo"}

@app.get("/health")
def health():
    return {"status": "OK"}

@app.get("/contador")
def contador():
    nuevo_valor = redis_client.incr("contador_visitas")
    return {"contador": nuevo_valor}

@app.get("/usuarios")
def obtener_usuarios():
    cache_key = "usuarios_cache"

    # 1. Buscar primero en Redis
    datos_cache = redis_client.get(cache_key)
    if datos_cache:
        return {"origen": "cache", "usuarios": json.loads(datos_cache)}

    # 2. Si no está, buscar en PostgreSQL
    conexion = obtener_conexion_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, email FROM usuarios ORDER BY id")
    filas = cursor.fetchall()
    cursor.close()
    conexion.close()

    usuarios = [{"id": f[0], "nombre": f[1], "email": f[2]} for f in filas]

    # 3. Guardar en Redis para la próxima vez (30 segundos)
    redis_client.setex(cache_key, 30, json.dumps(usuarios))

    return {"origen": "postgres", "usuarios": usuarios}