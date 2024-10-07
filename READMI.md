# Traductor de Voz

Este proyecto es una aplicación de traducción de voz a texto y de texto a voz utilizando `whisper`, `translate` y `gTTS`. La interfaz de usuario está construida con `gradio`.

## Requisitos Previos

- Docker
- Docker Compose

## Instalación

1. Clona este repositorio:
    ```sh
    git clone https://github.com/Edimega/MyVoiceTranslator
    cd MyVoiceTranslator
    ```

## Ejecución

### Usando Docker

1. Construye la imagen de Docker:
    ```sh
    docker build -t traductor-voz .
    ```

2. Ejecuta el contenedor:
    ```sh
    docker run -p 80:80 traductor-voz
    ```

### Usando Docker Compose

1. Ejecuta el siguiente comando para levantar los servicios:
    ```sh
    docker-compose up --build
    ```

La aplicación se ejecutará en `http://0.0.0.0:80`.

## Uso

1. Selecciona el idioma de entrada y el idioma de salida.
2. Sube un archivo de audio o graba uno utilizando el micrófono.
3. La aplicación transcribirá el audio, lo traducirá y generará un archivo de audio con la traducción.

## Contribución

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.