import os
import aiohttp
import asyncio
from datetime import datetime
from etc.config import settings
from fastapi import Request, UploadFile, File,request
from fastapi.responses import StreamingResponse, JSONResponse
# import speech_recognition as sr
# from elevenlabs import generate, play



async def get_agent_info()-> dict:

    request.state.log.info("Get agent info")
    headers = {
        "xi-api-key": settings.elevenlabs_api_key
    }

    timeout = aiohttp.ClientTimeout(total=60)
    response = await request.state.session.get(settings.elevenlabs_url_agent.replace('agent_id', settings.CESARE), headers=headers, json=audio_format, timeout=timeout)

    # Make request to Elevenlabs
    if response.status != 200:
        error_message = await response.text()
        raise Exception(f"Errore: {response.status} - {error_message}\n")
    request.state.log.debug("Successfull request")

