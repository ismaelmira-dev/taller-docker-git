import os
from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def hola():
    try:
        conn = psycopg2.connect(
            host=os.environ.get("DB_HOST", "db"),
            dbname="postgres",
            user="postgres",
            password=os.environ.get("POSTGRES_PASSWORD", "demo")
        )
        conn.close()
        return "MiniBlog funcionando, conectado a la base de datos"
    except Exception as e:
        return f"MiniBlog arriba, pero sin conexión a DB: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)