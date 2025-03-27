import io
import aiohttp
from etc.config import settings
from fastapi import Request
from fastapi.responses import StreamingResponse
from fastapi import FastAPI, File, UploadFile


async def generate_speech(
    request: Request,
    text: str
) -> File:
    request.state.log.debug("Request completed")
    headers = {
        "xi-api-key": settings.elevenlabs_api_key,
        "Content-Type": "application/json"
    }

    # TODO add body

    audio_format = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": 1.0, "similarity_boost": 0.5}
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(settings.elevenlabs_url.replace('select_elevenlabs_mode', 'text-to-speech'), headers=headers, json=audio_format) as response:

            if response.status != 200:
                error_message = await response.text()
                raise Exception(f"Errore: {response.status} - {error_message}")

            mp3_data = await response.read()
            return io.BytesIO(mp3_data)

async def get_audio_from_text(
    request: Request,
    text: str
) -> bin:

    mp3_file = await generate_speech(request, text)
    try:
        return StreamingResponse(mp3_file, media_type="audio/mpeg", headers={"Content-Disposition": "attachment; filename=output.mp3"})
    except Exception as e:
        return {"error": str(e)}



async def generate_text(
    request: Request,
    file: UploadFile = File(...)
) -> str: 
    request.state.log.debug("Request completed")
    headers = {
        "xi-api-key": settings.elevenlabs_api_key,
        "Content-Type": "multipart/form-data"
    }

    text_format = {
        "file": file,
        "model_id": "eleven_multilingual_v2"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(settings.elevenlabs_url.replace('select_elevenlabs_mode', 'speech-to-text'), headers=headers, json=text_format) as response:

            if response.status != 200:
                error_message = await response.text()
                raise Exception(f"Errore: {response.status} - {error_message}")

            mp3_data = await response.read()
            return io.BytesIO(mp3_data)

async def get_text_from_audio(
    request: Request,
    file: UploadFile = File(...)
): 
    ...