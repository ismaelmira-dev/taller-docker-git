# Comandos Docker Útiles — Taller Docker + Git

## Levantar servicios

```bash
docker-compose up -d              # Levantar en segundo plano
docker-compose up --build -d      # Reconstruir imágenes antes de levantar
docker-compose up -d --scale api=3  # Escalar un servicio a 3 instancias
```

## Ver estado

```bash
docker-compose ps                 # Estado de los contenedores del proyecto
docker-compose logs -f            # Ver logs en tiempo real (todos los servicios)
docker-compose logs -f [servicio] # Logs de un servicio específico
docker-compose top                # Procesos corriendo dentro de los contenedores
```

## Gestión

```bash
docker-compose stop               # Detener sin eliminar contenedores
docker-compose start              # Reanudar contenedores detenidos
docker-compose restart [servicio] # Reiniciar un servicio puntual
docker-compose down               # Detener y eliminar contenedores (conserva volúmenes)
docker-compose down -v            # Detener, eliminar contenedores Y volúmenes
```

## Inspección

```bash
docker-compose exec [servicio] sh     # Abrir una shell dentro de un contenedor
docker-compose exec db psql -U postgres    # Consola de PostgreSQL
docker-compose exec redis redis-cli        # Consola de Redis
```

## Limpieza

```bash
docker system prune -f            # Eliminar contenedores, redes e imágenes sin usar
docker volume prune -f            # Eliminar volúmenes no usados
docker-compose down --rmi all -v  # Limpieza total del proyecto (imágenes + volúmenes)
```

## Verificar que Docker está corriendo (Windows)

Si un comando falla con un error como:
```
failed to connect to the docker API at npipe:////./pipe/dockerDesktopLinuxEngine
```
significa que **Docker Desktop no está abierto**. Ábrelo desde el menú de inicio, espera a
que el ícono de la ballena deje de estar animado, y confirma con:
```bash
docker info
```
Si devuelve información en vez de un error, ya puedes ejecutar `docker-compose` con normalidad.