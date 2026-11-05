# Proyecto Urban Grocers

Este proyecto contiene pruebas automatizadas de validación para la API de Urban Grocers. Su objetivo es verificar el comportamiento del endpoint de creación de kits (`/api/v1/kits`) al recibir diferentes valores en el parámetro `name` del cuerpo de la solicitud POST. Las pruebas cubren escenarios positivos y negativos, comprobando el manejo de límites de caracteres, espacios, caracteres especiales, y la ausencia o tipo incorrecto del parámetro, asegurando que el servidor devuelva los códigos de estado HTTP correctos (201 y 400).

## Requisitos previos
- Python instalado en tu sistema.
- Necesitas tener instalados los paquetes `pytest` y `requests` para ejecutar las pruebas. Puedes instalarlos ejecutando el siguiente comando en tu terminal:
  ```bash
  pip install pytest requests

## Configuración

Antes de ejecutar las pruebas, asegúrate de configurar la URL del servidor:
- Abre el archivo configuration.py.
- Asigna la URL de tu entorno de pruebas a la variable URL_SERVICE (asegúrate de no incluir la barra diagonal / al final).