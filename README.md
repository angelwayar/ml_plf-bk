# Machine Learning Platform
El siguiente proyecto pretende llevar una colección de modelos de inteligencia artificial que pueden ser utilizados como herramientas.

## Requerimientos

|N| Requerimientos | Estado |
|-|----------------|--------|
|1  | Registrar usuario | |
|2  | Iniciar sesión||
|3  | Cerrar sesión| |
|4  | Modificar usuario| |
|5  | Seleccion de plan de servicio| |
|6  | Cancerlar suscripcion| |
|7  | Upload imagen| |
|8  | Pago online - Eliminar este caso en lo posible| |
|9  | Mejoramiento de imagen| |
|10 |Visualizar imagen de entrada y salida| |
|11 |Almacenar imagen mejorada| |
|12 |Descargar imagen mejorada| |
|13 |Eliminar imagen mejorada| |
|14 |Lista imagen almacenada| |
|15 |Filtrar las imagenes entre dos fechas| |

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

4. Ejercutar el siguiente comando.

    ```
    $ fastapi dev main.py
    ```