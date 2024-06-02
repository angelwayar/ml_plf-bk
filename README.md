# Machine Learning Platform
El siguiente proyecto pretende llevar una colección de modelos de inteligencia artificial que pueden ser utilizados como herramientas.

## Arquitectura del proyecto

El presente proyecto hace uso de una arquitectura tipo Model View Controller (MVC), organizado de la siguiente manera.

- **controllers:** Contiene los controladores responsables de manejar solicitudes y lógica de negocio.
- **db:** Contiene el controlador de la base de datos y la lógica para crear la base de datos.
- **middlewares:** Alberga varios middleware para el manejo de solicitudes (por ejemplo, archivos estáticos, CORS).
- **models:** Almacena los modelos de datos y esquemas de la aplicación.
- **repositories:** Maneja la interacción con bases de datos o servicios externos.
- **services:** Implementa la lógica de negocio para trabajar con objetos.
- **static:** Contiene archivos estáticos (algunas bibliotecas de js, css, imágenes, etc.).
- **templates:** Contiene plantillas HTML para renderizar vistas.
- **utils:** Contiene funciones de utilidad.

```
├── app
│   ├── controllers
│   │   ├── auth_controller.py
│   │   ├── page_controller.py
│   │   ├── private_controller.py
│   │   └── user_controller.py
│   ├── db
│   │   └── context.py
│   ├── middlewares
│   │   ├── cors_middleware.py
│   │   └── static_middleware.py
│   ├── models
│   │   ├── db.py
│   │   └── dto.py
│   ├── repositories
│   │   ├── token_repository.py
│   │   └── user_repository.py
│   ├── services
│   │   ├── token_service.py
│   │   └── user_service.py
│   ├── templates
│   │   ├── 403.html
│   │   ├── 404.html
│   │   ├── login.html
│   │   ├── main.html
│   │   ├── private.html
│   │   └── register.html
│   ├── utils
│   │   ├── dependencies.py
│   │   ├── formating.py
│   │   ├── hashing.py
│   │   ├── pages.py
│   │   └── validators.py
│   ├── static
│   ├── prod.sh
│   ├── db_init.bash
│   ├── db_init.py
│   ├── dev.bash
│   └── main.py
├── .env.example
├── docker-compose.yml
├── Dockerfile
├── install_env.sh
├── LICENSE
├── README.md
└── requirements.txt

11 directories, 35 files
```


## Requerimientos

| N |                Requerimientos                |    Estado    |
|---|----------------------------------------------|--------------|
|1  |Registrar usuario                             |              |
|2  |Iniciar sesión                                |              |
|3  |Cerrar sesión                                 |              |
|4  |Modificar usuario                             |              |
|5  |Seleccion de plan de servicio                 |              |
|6  |Cancerlar suscripcion                         |              |
|7  |Upload imagen                                 |              |
|8  |Pago online - Eliminar este caso en lo posible|              |
|9  |Mejoramiento de imagen                        |              |
|10 |Visualizar imagen de entrada y salida         |              |
|11 |Almacenar imagen mejorada                     |              |
|12 |Descargar imagen mejorada                     |              |
|13 |Eliminar imagen mejorada                      |              |
|14 |Lista imagen almacenada                       |              |
|15 |Filtrar las imagenes entre dos fechas         |              |

## Como ejecutar el proyecto de manera local
1. Crear entorno de ejecución para Python.

    |   SO  |      Comando       |
    |-------|--------------------|
    |Windows|python -m venv venv |
    |Linux  |python3 -m venv venv|

2. Activar entorno de ejecución.

- Windows
    ```
        $ cd venv/Scripts/
    ```
    ```
        $ activate
    ``` 
- Linux
    ```
        $ source venv/bin/activate
    ```

3. En la terminal dirigirce a la carpeta `/app`, que se encuentra en la raíz.

    ```
    $ cd /app
    ```

4. Ejecutar el siguiente comando para instalar las dependencias necesarias, que se encuentra en la raíz `/requirements.txt`.

    ```
        $ pip install -r requirements.txt
    ```

5. Ejercutar el siguiente comando para lanzar el proyecto.

    ```
    $ fastapi dev main.py
    ```

Webs Consultas
- https://github.dev/ViktorViskov/fastapi-mvc