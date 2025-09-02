# 🐳 Entorno Docker para Proyecto Django `ecomerce`

Este entorno Docker está diseñado para desplegar el proyecto Django `ecomerce` con PostgreSQL como base de datos, utilizando `docker-compose` para orquestación y `.env` para configuración segura.

---

## ⚙️ Estructura de servicios

- `web`: contenedor Django con configuración en `Dockerfile`
- `db`: contenedor PostgreSQL con persistencia de datos

---

## 📋 Requisitos previos

- Docker Engine instalado (idealmente en WSL2 si usas Windows)
- docker-compose v2+
- Archivo `.env` con variables de entorno definidas
- Proyecto Django funcional con `manage.py` y `requirements.txt`

---

## 📁 Estructura esperada del proyecto
```
. 
├── Dockerfile 
├── docker-compose.yml 
├── .env 
├── requirements.txt 
├── manage.py 
├── ecomerce/ │ 
|   |── settings.py │ 
|   |── urls.py 
│   └── ...
```

---

## 🧱 Configuración del Dockerfile

```dockerfile
FROM python:3.11

WORKDIR /app

COPY . .

# Instala dependencias del sistema necesarias para compilar mysqlclient y psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    default-libmysqlclient-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

## 🧪 Variables de entorno (.env)

Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
POSTGRES_DB=ecomerce_db
POSTGRES_USER=luis
POSTGRES_PASSWORD=tu_clave_segura
DEBUG=True


---

### 2. 🔧 docker-compose.yml

Agrega también esta sección:

```markdown
## 🧩 docker-compose.yml

Este archivo define los servicios `web` (Django) y `db` (PostgreSQL):

```yaml
version: '3.9'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    env_file:
      - .env
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:


# 🔄 Construir y levantar contenedores
docker compose up --build

#🧹 Limpiar contenedores huérfanos
docker compose down --remove-orphans

#🛠️ Ejecutar comandos Django dentro del contenedor
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser

## 🔁 Recarga automática (hot reload)

Gracias al volumen `.:/app` definido en `docker-compose.yml` y a la variable `DEBUG=True` en el archivo `.env`, los cambios realizados en el código fuente se reflejan automáticamente en el contenedor sin necesidad de reiniciar el entorno.

Esto permite un flujo de desarrollo más ágil y eficiente.

---

## 🛡️ Buenas prácticas

- Mantén el archivo `.env` fuera del control de versiones (usa `.gitignore`)
- Usa tokens personales para autenticación segura en GitHub
- Documenta cada paso técnico en tu portafolio o en foros especializados
- Revisa conflictos antes de levantar el entorno con el siguiente comando:

```bash
grep -rE '<<<<<<<|=======|>>>>>>>' .
