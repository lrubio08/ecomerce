# 🛒 Proyecto Django: Ecomerce

Este es un proyecto de e-commerce desarrollado con Django, PostgreSQL y Docker, orientado a la creación de una infraestructura profesional y modular para tiendas en línea. Está diseñado para ser escalable, seguro y fácilmente desplegable en entornos Linux (WSL2, VPS, etc.).

---

## 🚀 Funcionalidades principales

- Gestión de productos, categorías y stock
- Carrito de compras persistente
- Registro y autenticación de usuarios
- Panel de administración con Django Admin
- Integración con correo profesional para notificaciones
- Infraestructura Dockerizada con PostgreSQL y pgAdmin

---

## 🧱 Stack tecnológico

- **Backend**: Django + Python 3.11
- **Base de datos**: PostgreSQL
- **Contenedores**: Docker + Docker Compose
- **Gestión visual de DB**: pgAdmin (opcional)
- **Servidor local**: WSL2 sobre Ubuntu

---

## 📁 Estructura del proyecto

```
ecomerce/
├── apps/                      # Módulos funcionales (productos, usuarios, etc.)
├── ecomerce/                  # Configuración principal de Django
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
├── README.md
└── README_docker.md
```

---

## ⚙️ Despliegue local con Docker

Para levantar el entorno completo, sigue los pasos descritos en [`README_docker.md`](./README_docker.md). Incluye:

- Configuración de contenedores `web`, `db` y `pgadmin`
- Variables de entorno seguras
- Comandos para migraciones y superusuario
- Recarga automática (hot reload)

---

## 🧪 Instalación manual (sin Docker)

Si prefieres ejecutar el proyecto sin contenedores:

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

-> Asegúrate de tener PostgreSQL instalado y configurado localmente.

# 📬 Configuración de correo profesional
Este proyecto incluye integración SMTP con registros SPF, DKIM y DMARC verificados. La configuración se realiza en settings.py usando variables del archivo .env.

📌 Autor
Luis Rubio Desarrollador Full Stack. Especializado en Django, despliegue en VPS, automatización y gestión avanzada de correo profesional.

## 🤝 Comunidad y uso

Este proyecto está disponible para estudio, aprendizaje y referencia técnica. Se agradecen sugerencias y reportes de errores a través de issues.

Las decisiones de desarrollo, implementación y evolución del proyecto son gestionadas exclusivamente por el autor, con foco en mantener coherencia técnica y escalabilidad.

## 📄 Licencia

Distribuido bajo la licencia MIT. Puedes revisar el código, adaptarlo para tus propios fines, pero no modificar este repositorio directamente sin autorización.
