# act-ml-workflow

## Equipo: bookML

## Pasos para ejecutar el código:

1. Hacer fork al repositorio

2. Instalar uv para instalar las librerías necesarias para generar un entorno de python que contenga los paquetes necesarios para ejecutar los notebooks.

    - En caso de no querer usar uv, instalar con pip las versiones de librerías que aparecen en pyproject.toml

3. Dentro de la carpeta raíz crear un archivo .env que contenga el id de la suscripción con la que se generó el grupo de recursos, dentro de él escribir el id de la siguiente manera: **MY_SECRET=<id-de-la-suscripción>**

4. Cargar el archivo prueba.csv en la carpeta de `data`

5. Cargar el uri2.json dentro de la carpeta `src`

6. Ejecutar DataPreprocessing.ipynb

7. Ejecutar model_dummy.ipynb

8. Ejecutar despliegue.ipynb

9. Ejecutar API.ipynb, donde se hace inferencia con el archivo llamado *prueba.csv* dentro de la carpeta `data`

## Especificaciones de software mínimo:

Windows 10 (2015)

RAM: 512 MB

Ancho de banda: 0.9 MBps
