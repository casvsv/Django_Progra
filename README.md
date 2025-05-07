# 🧾 Django Progra

Este proyecto es una aplicación web desarrollada con Django, enfocada en la gestión de una cooperativa. Incluye funcionalidades para manejar información de socios, transacciones y otros aspectos relevantes.

---

## 📂 Estructura del Proyecto

```plaintext
Django_Progra/
├── apps/                 # Aplicaciones Django personalizadas
│   └── cooperativa/      # Aplicación principal para la gestión de la cooperativa
├── static/               # Archivos estáticos (CSS, JS, imágenes)
├── templates/            # Plantillas HTML para las vistas
├── manage.py             # Script de administración de Django
```

## Requisitos

- Python 3.x  
- Django 3.x o superior  
- Base de datos SQLite (por defecto)

## Requisitos
- Python 3.x  
- Django 3.x o superior  
- Base de datos SQLite (por defecto)

## Instalación y Ejecución
1. Clona el repositorio:  
   `git clone https://github.com/casvsv/Django_Progra.git`
2. Accede al directorio del proyecto:  
   `cd Django_Progra`
3. Crea y activa un entorno virtual (opcional pero recomendado):  
   `python -m venv env`  
   `source env/bin/activate`  # En Windows: env\Scripts\activate
4. Instala las dependencias:  
   `pip install -r requirements.txt`
5. Aplica las migraciones:  
   `python manage.py migrate`
6. Ejecuta el servidor de desarrollo:  
   `python manage.py runserver`
7. Accede a la aplicación en tu navegador:  
   `http://127.0.0.1:8000/`

## Contribuciones
¡Las contribuciones son bienvenidas! Si deseas colaborar:

1. Haz un fork del repositorio.
2. Crea una nueva rama:  
   `git checkout -b feature/nueva-funcionalidad`
3. Realiza tus cambios y haz commit:  
   `git commit -m "Agrega nueva funcionalidad"`
4. Haz push a tu rama:  
   `git push origin feature/nueva-funcionalidad`
5. Abre un Pull Request detallando tus cambios.

## Licencia
Este proyecto está bajo la Licencia MIT. 
