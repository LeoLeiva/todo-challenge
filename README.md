# Invera Challenge de tareas
Chellenge realizado para invera, descripcion de lo pedido:
* [https://github.com/LeoLeiva/todo-challenge/tree/main/docs](https://github.com/LeoLeiva/todo-challenge/tree/main/docs) <== Link al README.md

Tecnologias usadas:
  * Python 
  * Django
  * Html + Css + Js + Bootstrap
  * Virtualenv
  * Docker
  
Paquetes usados:
  * Django Rest Framework
  * django-userforeignkey
  * gunicorn
  * psycopg2

---

## Iniciando el proyecto
Primero tenemos que tener instalado python 3 verificamos la version con ==>python --version e instalamos virtualenv para el entorno,
```sh
$ python --version
$ pip install virtualenv
```
_En el caso de tener python 2 cuando instalemos los repositorios se debera instalar con pip3 y correr con python3_

Creamos el entorno virtual y lo activamos:
```sh
$ virtualenv venv
$ source venv/bin/activate
```

Si tenemos python 2 y 3 en Linux podemos crear el entorno virtual solo con python 3:
```sh
$ virtualenv -p /usr/bin/python3
$ source venv/bin/activate
```

En el caso de tener windows, para activar el entorno virtual:
```sh
$ python -m venv venv
$ .\venv\scripts\activate
```

Clonamos el proyecto:
```sh
$ git clone https://github.com/LeoLeiva/todo-challenge.git
```

Ingresamos a la carpeta de la aplicacion
```sh
$ cd todo-challenge
$ cd invera
```

Instalamos los paquetes del proyecto:
```sh
$ pip install -r ../requirements.txt
```
==>Como el requeriments esta en la carpeta todo challenge se agrega ../requeriments.txt

La app tiene configuracion para manejar sqlite3 o postgresql en docker, por lo tanto edite setting.py para elegir la bd:
 * Para sqlite dejar como esta
 * Para postgresql comentar desde la linea 99 a 105 de settings.py y descomentar desde 88 a 96
 * Recuerde cambiar DEBUG = True por False en la linea 26

Hacemos el migrate para crear la base de datos:
```sh
$ python manage.py migrate
```

Ya esta listo para ejecutar la aplicacion:
```sh
$ python manage.py runserver
```

Para ingresar
* [http://localhost:8000/](http://localhost:8000/) - Para el FronEnd
* [http://localhost:8000/api/task/](http://localhost:8000/api/task/) - Para utilizar la API

Para correr los test:
```sh
$ python manage.py test
```

Para correr de forma inversa:
```sh
$ python manage.py test --reverse
```

---

## En el caso de querer utilizar Docker
_Necesitamos tener instalado Docker y docker-compose_
El docker esta preparado para usar postgresql, por lo tanto edite setting.py para elegir la bd:
 * Comentar desde la linea 99 a 105 de settings.py y descomentar desde 88 a 96
 * Recuerde cambiar DEBUG = True por False en la linea 26

Desde la carpeta todo-challenge hacemos la migracion para que se cree la base de datos y collectstatic para las imagenes:
```sh
$ docker-compose run django_app python invera/manage.py migrate
$ docker-compose run django_app python invera/manage.py collectstatic
```

En el caso de querer crear un superuser para poder ver los logs:
```sh
$ docker-compose run django_app python invera/manage.py createsuperuser
```

Para ejecutarlo una ves que la app se haya construido:
```sh
$ docker-compose up --build
```

Para ingresar una vez que se haya construido:

* [http://0.0.0.0:8000/](http://0.0.0.0:8000/) - Para el FronEnd
* [http://0.0.0.0:8000/api/task/](http://0.0.0.0:8000/api/task/) - Para utilizar la API

