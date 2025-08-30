FROM python:3.11-slim

# Evita prompts interactivos
ENV DEBIAN_FRONTEND=noninteractive

# Instala dependencias del sistema necesarias para compilar mysqlclient y psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    default-libmysqlclient-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*


# Crea directorio de trabajo
WORKDIR /app

# Copia dependencias
COPY requirements.txt .

# Instala dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del proyecto
COPY . .

# Expone el puerto
EXPOSE 8000

# Comando por defecto
CMD ["gunicorn", "ecommerce.wsgi:application", "--bind", "0.0.0.0:8000"]


