import io
import os
import sys
import aiohttp
from etc.config import settings
from fastapi import Request, UploadFile, File
from fastapi.responses import StreamingResponse, JSONResponse


async def get_audio_from_text(
    request: Request,
    text: str
)-> bin:
    """
    This async function use the ELevenlabs API sending a input text and returning a audio file
    Args:
        text (str): input text
    Returns:
        bin: audio file
    """

    # Build request
    request.state.log.debug("Request completed")
    headers = {
        "xi-api-key": settings.elevenlabs_api_key,
        "Content-Type": "application/json"
    }

    audio_format = {
        "text": str(text),
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": 1.0, "similarity_boost": 0.5}
    }

    # Make request to Elevenlabs
    async with aiohttp.ClientSession() as session:
        async with session.post(settings.elevenlabs_url.replace('method', settings.text_to_speech) + settings.voice_id, headers=headers, json=audio_format) as response:
            if response.status == 200:
                mp3_data = await response.read()
                mp3_file = io.BytesIO(mp3_data)
            else:
                error_message = await response.text()
                raise Exception(f"Errore: {response.status} - {error_message}\n")

    # Saving file
    try:
        return StreamingResponse(mp3_file, media_type="audio/mpeg", headers={"Content-Disposition": "attachment; filename=output.mp3"})
    except Exception as e:
        return {"error": str(e)}


async def get_text_from_audio(
    request: Request,
    file: UploadFile = File(...)
)-> dict:
    """
    This async function use the ELevenlabs API sending a input audio and returning a text file
    Args:
        bin (str): input audio
    Returns:
        text (str) : text file
    """

    if not file.filename.endswith(".mp3"):
        return JSONResponse(status_code=400, content={"error": "Only .mp3 files are allowed"})

    request.state.log.debug('building request')
    url = "https://api.elevenlabs.io/v1/speech-to-text"
    headers = {
        "xi-api-key": settings.elevenlabs_api_key
    }

    if sys.getsizeof(file) > 1073741824: # 1 Gigabyte
        raise Exception(f"Failed: filesize is too big {file.getsize()}")

    data = {
        "model_id": "scribe_v1",
        "language_code": "it", # ISO639-1
        "file": await file.read(),
        "filename":file.filename,
        "content_type":"audio/mpeg"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=data) as response:
            if response.status == 200:
                return await response.json()
            else:
                raise Exception(f"Failed: {response.status}")
