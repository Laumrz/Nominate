### CRUD con Python - Django y MySQL


1.  Crear un entorno virtual, hay muchas formas

        Opción 1: Crear entorno virtual con el paquete virtualenv
        Si no tienes instalado virtualenv puedes instalarlo de forma global en el sistema atraves de https://pypi.org/project/virtualenv/
        pip install virtualenv ->Instalar de forma global
        virtualenv env ->Crear entorno
        virtualenv --version ->Ver la versión de virtualenv

        Opción 2: Crear un entorno virtual con el paquete que ya viene por defecto en las ultimas versiones de Python
        python -m venv env

2.  Activar entorno virtual

        . env/Script/activate ->para Windows
        . env/bin/activate -> Para Mac
        deactivate -->Para desactivar mi entorno virtual

3.  Instalar Django desde el manejador de paquete de Python Pip, ya dentro del entorno virtual.

        python -m pip install Django
        pip install Django
        Nota: para instalar Django en una version especifica
        pip install Django==4.2.4

4.  Ver la versión de Django instalada en el proyecto

        python -m django --version

5.  Instalar Driver para conectar Gestor de BD MySQL con Django

        pip install mysqlclient

6.  Instalar el paquete (biblioteca) Pillow, esto con el fin de poder procesar la subida de imagen en el servidor

        Pillow es la librería que nos permitirá usar el campo ImageField para poder guardar imágenes

        https://pypi.org/project/Pillow/
        pip install Pillow

7.  Instalar el paquete (biblioteca) openpyxl y pandas

        pip install openpyxl
        pip install pandas

8.  Crear el proyecto con Django

        `django-admin startproject project_core .`
        El punto . es crucial le dice al script que instale Django en el directorio actual

        Ya en este punto se puede correr el proyecto que a creado Django,
        python manage.py runserver

9.  Crear mi primera aplicación en Django

        python manage.py startapp empleados

10. Instalar nuestra aplicación (empleados) ya creada en el proyecto, en el archivo settings.py

        archivo settings.py
        INSTALLED_APPS = [
        ----,
        'empleados',
        ]

11. Crear una clase en models.py la cual reprtesentara mi tabla en BD,(bd_django) preferiblemente los modelos
    se declaran en singular

        class Empleado(models.Model):
                nombre_empleado = models.CharField(max_length=200)
                apellido_empleado = models.CharField(max_length=100)
                email_empleado = models.EmailField(max_length=50)
                edad_empleado = models.IntegerField()
                genero_empleado = models.CharField(max_length=80, choices=generos)
                salario_empleado = models.DecimalField(
                        max_digits=10, decimal_places=2, null=True, blank=True)
                foto_empleado = models.ImageField(
                        upload_to='fotos_empleados/', null=True, blank=True)
                created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
                updated = models.DateTimeField(auto_now_add=False, auto_now=True)

12. crear la Base de Datos (bd_django_mysql) en MySQL

13. Editar el archivo settings.py del proyecto, cambiando los parametros de conexión a MySQL

        `
        DATABASES = {
                'default': {
                        'ENGINE': 'django.db.backends.mysql', #ENGINE es motor de BD
                        'NAME': 'bd_django_mysql',
                        'USER': 'root',
                        'PASSWORD': '',
                        'HOST': '127.0.0.1',
                        'PORT': '3306',
                }
        }
        `

14. Crear las migraciones y correrlas

        python manage.py makemigrations -> Creando migraciones
        python manage.py migrate         -> Correr migraciones

15. Correr el proyecto

        python manage.py runserver
        Revisar la consola y visitar la URL http://127.0.0.1:8000

16. Crear el archivo urls.py en la aplicación (bd_django_mysql)

        from django.urls import path
        from . import views

                urlpatterns = [
                        path('', views.inicio, name='inicio'),
                        path('registrar_empleado/', views.registrar_empleado,
                                name='registrar_empleado'),
                        path('empleados/', views.listar_empleados, name='listar_empleados'),
                ]

17. Conectar las URLS de mi aplicación con el projecto, para esto vamos al archivo uls.py del projecto
    from django.urls import path, include

        urlpatterns = [
                path('admin/', admin.site.urls),
                path("", include('empleados.urls'))
        ]

18. Crear la carpeta 'templates' dentro de la aplicación donde estarán mis archivos.html

19. Crear la carpeta 'static' dentro de mi aplicacion, aqui estaran archivos
    estaticos (css, js, imagenes, etc..)

20. Crear la carpeta media, para almacenar las imagenes del empleado

21. Correr archivo requirement.txt

        pip install -r requirements.txt

22. Crear el archivo requirements.txt para tener todos los paquetes del proyecto a la mano

        pip freeze > requirements.txt

        Nota: para instalar los paquetes solo basta ejecutar
        pip install -r requirements.txt

#### Resultado final
