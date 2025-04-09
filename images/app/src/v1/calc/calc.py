import os
import aiohttp
import asyncio
from datetime import datetime
from etc.config import settings
from fastapi import Request, UploadFile, File
from fastapi.responses import StreamingResponse, JSONResponse


async def get_calc_info(
    request: Request
)-> dict:
    """
    This async function use the ELevenlabs API return conversation details given a conversation id

    args:
        conversation_id (str): identifier of conversation use to retrieve a dict 

    Returns:
        (dict): _description_
    """
    request.state.log.info("Get agent link")
    headers = {
        "Authorization": f"Bearer: {settings.elevenlabs_api_key}"
    }

    timeout = aiohttp.ClientTimeout(total=60)
    url = os.path.join()
    response = await request.state.session.get(
        url,
        headers=headers,
        timeout=timeout
    )

    # Make request to Elevenlabs
    if response.status != 200:
        error_message = await response.text()
        raise Exception(f"Errore: {response.status} - {error_message}\n")
    request.state.log.debug("Successfull request")

    placeholder = await response.json()
    return placeholder
   