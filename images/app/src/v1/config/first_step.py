import io
import aiohttp
from etc.config import settings
from fastapi import Request
from fastapi.responses import StreamingResponse


async def generate_speech(text: str, audio_format: dict):
    headers = {
        "xi-api-key": settings.elevenlabs_api_key,
        "Content-Type": "application/json"
    }

    # TODO add body
    # if audio_format == {}:
    audio_format = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": 1.0, "similarity_boost": 0.5}
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(settings.elevenlabs_url, headers=headers, json=audio_format) as response:
            if response.status == 200:
                mp3_data = await response.read()
                return io.BytesIO(mp3_data)
            else:
                error_message = await response.text()
                raise Exception(f"Errore: {response.status} - {error_message}")


async def get_audio_from_text(
    request: Request,
    text: str,
    # audio_format: TextToSpeechRequest = Body()

) -> bin:

    mp3_file = await generate_speech(text,)
    try:
        return StreamingResponse(mp3_file, media_type="audio/mpeg", headers={"Content-Disposition": "attachment; filename=output.mp3"})
    except Exception as e:
        return {"error": str(e)}

