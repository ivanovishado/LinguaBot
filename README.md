# LinguaBot+

Chatbot asistente para el repaso del idioma inglés.

## Instalación

### Instalar Redis

Más información
[aquí](https://redis.io/download)

Para obtener el código puede clonarlo o bajarlo

### Clonar

    git clone git@github.com:ivanovishado/LinguaBot.git

### Bajarlo

Bajarlo de
[aquí](https://github.com/ivanovishado/LinguaBot/archive/master.zip)

Descomprimir

## Habilitar virtualenv

Instalar virtualenv

    sudo apt install virtualenv

Activar virtualenv en el directorio con el código

    source facebook_chatbot/bin/activate

## Instalar los requirements

En el directorio del código hacer

    pip install -r requirements.txt

## Habilitar _ngrok_

_ngrok_ es una herramienta de tunel que nos permitirá exponer nuestro servicio
en una dirección url pública

    1. Obtenerlo
    [aquí](https://ngrok.com/download)
    2. Descomprimir
    3. Ejecutar

        ./ngrok http <puerto>

    4. Al ejecutarse te dará una dirección publica, con esa hay que configurar
       el chatbot en facebook

Donde <puerto> es el puerto escrito en "server.py" (default=8080).

## Chatbot en Facebook

    1. Crear una Página de Facebook
    2. Registrarse como desarrollador
    3. Crear una nueva aplicación
    4. Activar el servicio de messenger para dicha aplicación
    5. Asignar token de verificación, y obtener token de acceso al archivo de
       configuración
    6. Probar en el chat de la página


## Ejecutarlo

Para ejecutarlo de forma normal

    python server.py

Despues de esto, comprobar que el chatbot responda desde Messenger.
