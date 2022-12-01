# Proyecto Integrador DJANGO

## Grupo 7

1. Genaro, Juan Pablo (Dueño del Repositorio)
2. Marquez, Lisandro
3. Rolleri, Valentino Filippo

## Verdulería

Nuestro proyecto se trataba sobre la resolución ante un problema, una verdulería quiere vender productos a sus clientes a través de un sitio web. Nosotros nos encargamos de crear un sitio web simple, cómodo y eficaz para la resolución de ello.

### Páginas

Nuestra app consiste de 4 páginas:

1. Inicio
2. Compra
3. Como Comprar
4. Registro de Usuarios

#### Inicio *[/home]*

Aquí se muestran los productos que el *Usuario* puede comprar en nuestra verdulería, así mismo, se pueden añadir productos en caso de que la verdulería agregue alguno nuevo en algún momento.

#### Compra *[/home/compra]*

Esta página muestra una tabla con todos los productos y cantidades de los mismos seleccionados hasta el momento, aquí se podrá finalizar la compra o continuar agregando productos en caso de desearlo.

#### Como Comprar *[home/como-comprar]*

En esta página hay un breve pero útil instructivo sobre como funciona tanto las páginas **Inicio** como **Compra** para cualquier persona que ingrese al sitio por primera vez.

#### Registro de Usuarios *[home/compra/usuario]*

Si usted no está registrado dentro de la base de datos de la verdulería, podrá insertar sus datos a la misma para posteriormente realizar la compra de manera adecuada. En caso de ya estar registrado, solo deberá ingresar los datos solicitados para así efectuar la compra.

### Guía de Instalación

Lo primero que debemos hacer para que el proyecto se ejecute correctamente es abrir el mysql desde la terminal y ejecutar:

*sudo mysql*

*source **[ruta del archivo "Integrador_Verduleria/Documentacion/database.sql"]***

Y posteriormente ejecutar las siguientes lineas de código:

*use mysql;*

*create user 'Usuario'@'localhost' identified by 'Pepe_1234';*

*GRANT ALL ON . TO 'Usuario'@'localhost';*

Esto lo que hará será que la base de datos ingresada anteriormente pueda ser accedida por el proyecto.

Ahora debemos instalar los *packages* de Python para que funcione el proyecto dentro de un PipEnv u otros. Se crea a partir del siguiente comando ubicados en la carpeta base del Proyecto (Integrador_Verduleria):

*pipenv install*

*pipenv shell*

Aquí dentro podremos instalar los *packages* sin que se instalen en nuestro dispositivo, para evitar conflictos con otros proyectos. Ahora, los *packages* que debemos instalar para que funcione este proyecto estan en ["Integrador_Verduleria/Documentacion/requierements.txt"] y debemos ejecutar el siguiente comando con cada *package*:

*pip install [**package**]*

Una vez instalados todos los *packages*, ejecutamos el siguiente comando (estando en la carpeta "Integrador_Verduleria/Proyecto") con la terminal de python:

*./manage.py runserver*

Y así ejecutaremos el proyecto.

**Copyright © 2022 ITSVillada 6C [Genaro, Marquez, Rolleri]**. *All rights reserved*