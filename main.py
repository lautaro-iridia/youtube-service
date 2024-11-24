from fastapi import FastAPI, HTTPException
from youtube_transcript_api import YouTubeTranscriptApi

# Crear una instancia de la aplicación FastAPI
app = FastAPI(
    title="Servicio de Transcripciones de YouTube",
    description="API para obtener transcripciones de videos de YouTube"
)

@app.get("/transcript/{video_id}", 
         summary="Obtener transcripción de un video",
         description="Recupera la transcripción de un video de YouTube en el idioma especificado")
async def get_transcript(video_id: str, language: str = "es"):
    """
    Obtiene la transcripción de un video de YouTube.
    
    Args:
        video_id (str): Identificador único del video de YouTube
        language (str, opcional): Idioma de la transcripción. Por defecto es español.
    
    Returns:
        dict: Transcripción formateada del video
    
    Raises:
        HTTPException: Si no se puede obtener la transcripción
    """
    try:
        # Recuperar la transcripción del video en el idioma especificado
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])

        # Formatear la transcripción con información de tiempo
        output = ""
        for entry in transcript:
            start_time = entry["start"]
            duration = entry["duration"]
            text = entry["text"]
            
            # Crear una entrada formateada con tiempo de inicio, duración y texto
            output += f"[{start_time:.2f}s - {duration:.2f}s]\n{text}\n---\n"

        # Devolver la transcripción formateada
        return {"transcript": output}

    except Exception as e:
        # Manejar errores y devolver un error 404 con detalles
        raise HTTPException(
            status_code=404, 
            detail=f"No se pudo obtener la transcripción: {str(e)}"
        )

# Punto de entrada para ejecutar el servidor (solo para desarrollo local)
if __name__ == "__main__":
    import uvicorn
    
    # Ejecutar el servidor con configuraciones específicas
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True  # Habilitar recarga automática durante el desarrollo
    )
