<p align="center">
  <a href="https://mac-front.netlify.app/" target="blank"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyFF-pMobEjPx9qP3u97t47qBVudOQwbHcrA&usqp=CAU" width="200" alt="React logo" /></a>
</p>

# Mac-back

1. Clonar proyecto
2. Crear entorno y activarlo
3. Instalar dependencias del requirements.txt
4. Tener la base de datos postgres con credenciales
5. Cambiar variables de entorno, por archivo secrets
6. Hacer las migraciones respectivas
```
python manage.py makemigrations
python manage.py mimgrate
```
7. Crear superusuario con credenciales
```
python manage.py createsuperuser
```
8. Correr servidor
```
python manage.py runserver
```

# Producción

El servidor se encuentra desplegado en render.com y ya esta enlazado con el front de mac-front