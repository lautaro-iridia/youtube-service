# Servicio de Transcripciones de YouTube

## Descripción

El **Servicio de Transcripciones de YouTube** es una API desarrollada con **FastAPI** que permite obtener las transcripciones de videos de YouTube en el idioma especificado. Esta herramienta es ideal para desarrolladores que buscan integrar funcionalidades de transcripción en sus aplicaciones o para cualquier persona que necesite acceder a las transcripciones de videos de manera programática.

## Características

- **Obtención de Transcripciones:** Recupera las transcripciones de videos de YouTube utilizando el `video_id`.
- **Soporte Multilingüe:** Permite especificar el idioma de la transcripción.
- **API RESTful:** Fácil de integrar con cualquier aplicación que soporte llamadas HTTP.
- **Dockerizado:** Facilita el despliegue en diferentes entornos mediante el uso de contenedores Docker.

## Tecnologías Utilizadas

- [Python 3.11](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api)
- [Docker](https://www.docker.com/)

## Instalación

### Prerrequisitos

- [Python 3.11](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Docker](https://www.docker.com/get-started) (opcional, para despliegue en contenedores)

### Clonar el Repositorio

```bash
git clone git@github.com:lautaro-iridia/youtube-service.git
cd youtube-service
```

### Crear y Activar un Entorno Virtual (Opcional pero Recomendado)

```bash
python -m venv env
```

#### En Windows

```bash
env\Scripts\activate
```

#### En Unix o MacOS

```bash
source env/bin/activate
```

### Instalar las Dependencias

```bash
pip install --no-cache-dir -r requirements.txt
```

## Uso

### Ejecutar la Aplicación Localmente

```bash
uvicorn main:app --reload
```

La API estará disponible en `http://127.0.0.1:8000`.

### Endpoints Disponibles

#### Obtener Transcripción de un Video

- **URL:** `/transcript/{video_id}`
- **Método:** `GET`
- **Parámetros:**
  - `video_id` (string): Identificador único del video de YouTube.
  - `language` (string, opcional): Idioma de la transcripción (por defecto es `es` para español).

- **Descripción:**
  Recupera la transcripción de un video de YouTube en el idioma especificado.

- **Respuesta Exitosa:**

  ```json
  {
      "transcript": "[0.00s - 5.00s]\nHola, bienvenidos al video.\n---\n[5.00s - 10.00s]\nHoy vamos a hablar sobre...\n---\n"
  }
  ```

- **Errores Comunes:**
  - `404 Not Found`: Si no se puede obtener la transcripción del video.

- **Ejemplo de Solicitud:**

  ```bash
  curl -X GET "http://127.0.0.1:8000/transcript/dQw4w9WgXcQ?language=en" -H "accept: application/json"
  ```

### Documentación Interactiva

FastAPI provee una interfaz de documentación interactiva disponible en:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Despliegue con Docker

### Construir la Imagen de Docker

```bash
docker build -t youtube-service .
```

### Ejecutar el Contenedor

```bash
docker run -d --name youtube-service -p 8000:8000 youtube-service
```

La API estará disponible en `http://localhost:8000`.

## Contribuciones

¡Contribuciones son bienvenidas! Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. **Fork** el repositorio.
2. Crea una **rama** para tu feature o arreglo: `git checkout -b feature/nueva-funcionalidad`.
3. **Commit** tus cambios: `git commit -m 'Añadir nueva funcionalidad'`.
4. **Push** a la rama: `git push origin feature/nueva-funcionalidad`.
5. Abre un **Pull Request**.

## Licencia

Este proyecto está licenciado bajo la **Licencia MIT**. Para más detalles, consulta el archivo [LICENSE](LICENSE).

## Contacto

Para cualquier duda o comentario, puedes contactarme a través de [lautaro.vallejos@iridia.com.ar](mailto:lautaro.vallejos@iridia.com.ar).
