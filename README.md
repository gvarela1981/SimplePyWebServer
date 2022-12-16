Challenge para probar la clase SimpleHTTPServer

Initial commit July 20, 2021

## Requerimientos

| Requerimiento     | Estado           |
| -------------     | -------------    |
| Endopoint que devuelva JSON  al recibir request ej. (0.0.0.0:8000/)  | completo |
| Endopoint que devuelva JSON  con valor status: Test OK al recibir request ej. (0.0.0.0:8000/valor_aceptado)  | completo |
| Endopoint que devuelva JSON  con valor status: Value not valid al recibir request ej. (0.0.0.0:8000/valor_no_aceptado)  | completo |
| Presentado en un repositorio en github     | completo      |
| Incluya instrucciones de como instalar dependencias y cómo utilizarlo.     | completo      |

## Deseables

| Requerimiento     | Estado           |
| -------------     | -------------    |
| Implementar el webservice usando la biblioteca estándar (BaseHTTPServer).     | completo      |
| Principios de programación SOLID, en particular la separación en servicios del cliente de la API de terceros.    | completo      |
| Modularización del código en varios archivos.    | completo      |
| Cobertura con tests y mocks.    | pendiente      |
| Correr via Docker o equivalente, incluyendo la instalación de dependencias para la misma.     | completo      |


### Ejecucion de Webserver con Docker

- Se requiere instalación de dockerEngine y docker-compose (https://gist.github.com/Zalitoar/ef1577acad9c3a78461954e080dc8576)
- git clone https://github.com/gvarela1981/SimplePyWebServer.git
- cd SimplePyWebServer
- Ejecutar docker-compose up -d --build

### Instalacion de Webserver en el host (SIN VENV)

- Se requiere python instalado v3+


### Ejecucion de Webserver en el host (SIN VENV)

- cd SimplePyWebServer
- python3 server.py

### To do

- Agragar al Read.me instalacion de venv
