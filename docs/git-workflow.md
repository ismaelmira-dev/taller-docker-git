# Flujo de Trabajo con Git — Taller Docker + Git

## Estrategia de ramas

| Rama                     | Propósito                                          |
|---------------------------|-----------------------------------------------------|
| `main`                    | Documentación general, README, guías                |
| `escenario-1-wordpress`   | Desarrollo del Escenario 1 (WordPress + MySQL)       |
| `escenario-2-api-node`    | Desarrollo del Escenario 2 (API Node.js + PostgreSQL)|
| `escenario-3-redis`       | Desarrollo del Escenario 3 (App con caché Redis)     |
| `escenario-4-cicd`        | Desarrollo del Escenario 4 (CI/CD con GitHub Actions)|
| `feature/nombre`          | Ramas personales por estudiante dentro de cada escenario |

## Flujo de trabajo por escenario

1. **Clonar el repo** (o crearlo la primera vez)
   ```bash
   git clone <url-del-repo>
   cd taller-docker-git
   ```

2. **Crear la rama del escenario**
   ```bash
   git checkout -b escenario-1-wordpress
   ```

3. **Trabajar en la carpeta correspondiente**
   ```bash
   cd escenario-1-wordpress/ejercicio/
   # ... crear archivos ...
   ```

4. **Commits frecuentes y descriptivos**
   ```bash
   git add .
   git commit -m "feat: agrega docker-compose para WordPress + MySQL"
   ```

5. **Subir la rama**
   ```bash
   git push origin escenario-1-wordpress
   ```

6. **Al terminar, fusionar con la rama principal** (vía Pull Request o merge directo)
   ```bash
   git checkout main
   git merge escenario-1-wordpress
   ```

## Convención de commits

| Prefijo    | Uso                                                   |
|------------|--------------------------------------------------------|
| `feat:`    | Nueva funcionalidad                                     |
| `fix:`     | Corrección de error                                     |
| `docs:`    | Documentación                                            |
| `style:`   | Formato, espacios, puntos y comas (no afecta el código) |
| `refactor:`| Refactorización de código                                |
| `test:`    | Agregar o corregir pruebas                                |
| `chore:`   | Tareas de mantenimiento, configuración                    |

### Ejemplos

```
feat: agrega soporte para phpMyAdmin en el escenario 1
fix: corrige la conexión a PostgreSQL en el escenario 2
docs: actualiza README con instrucciones de uso
```

## Otros comandos útiles

**Ramas**
```bash
git branch          # Listar ramas locales
git branch -a       # Listar todas (incluidas remotas)
git checkout -b nombre-rama   # Crear y cambiar a una rama
git switch -c nombre-rama     # Alternativa moderna
```

**Commits**
```bash
git status
git add .
git commit -m "tipo: descripción"
git log --oneline --graph   # Ver historial resumido
```

**Sincronización**
```bash
git pull origin main
git push origin nombre-rama
git fetch --all
```

**Unir ramas**
```bash
git checkout main
git merge nombre-rama
git branch -d nombre-rama   # Eliminar rama local ya fusionada
```

**Stash (guardar cambios temporales)**
```bash
git stash push -m "descripción"
git stash list
git stash pop
```

## Checklist antes de pasar al siguiente escenario

- [ ] Crear la rama correspondiente (`escenario-X-nombre`)
- [ ] Levantar los contenedores sin errores (`docker-compose up -d`)
- [ ] Verificar que los servicios se comunican entre sí
- [ ] Probar los endpoints o funcionalidades
- [ ] Verificar persistencia de datos (reiniciar contenedores, ¿persisten?)
- [ ] Documentar en README.md cómo usar el escenario
- [ ] Hacer commit y push de la rama
- [ ] Hacer merge a main (opcional, al finalizar)