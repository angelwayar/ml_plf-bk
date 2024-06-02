#!/bin/bash

# Exportar todas las variables al entorno
set -a

# Comprobar si el archivo .env existe en el directorio padre y cargarlo
if [ -f ../.env ]; then
    . ../.env
else
    echo "Advertencia: archivo ../.env no encontrado."
fi

# Dejar de exportar todas las variables al entorno
set +a

# Ejecutar el script de Python para inicializar la base de datos
python db_init.py

# Comprobar si el script de Python se ejecutó correctamente
if [ $? -eq 0 ]; then
    echo "Inicialización de la base de datos completada exitosamente."
else
    echo "Error: La inicialización de la base de datos falló."
    exit 1
fi
