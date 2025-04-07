import os
import aiohttp
import asyncio
from datetime import datetime
from etc.config import settings
from fastapi import Request, UploadFile, File
from fastapi.responses import StreamingResponse, JSONResponse


async def get_agent_info(
    request: Request
)-> dict:

    request.state.log.info("Get agent info")
    headers = {
        "xi-api-key": settings.elevenlabs_api_key
    }

    timeout = aiohttp.ClientTimeout(total=60)
    response = await request.state.session.get(settings.elevenlabs_url_agent.replace('agent_id', settings.CESARE), headers=headers, timeout=timeout)

    # Make request to Elevenlabs
    if response.status != 200:
        error_message = await response.text()
        raise Exception(f"Errore: {response.status} - {error_message}\n")
    request.state.log.debug("Successfull request")

    agent_info = await response.json()

    return agent_info


async def get_agent_link(
    request: Request
)-> dict:

    request.state.log.info("Get agent link")
    headers = {
        "xi-api-key": settings.elevenlabs_api_key
    }

    timeout = aiohttp.ClientTimeout(total=60)
    url = os.path.join(settings.elevenlabs_url_agent.replace('agent_id', settings.CESARE), 'link')
    response = await request.state.session.get(url, headers=headers, timeout=timeout)

    # Make request to Elevenlabs
    if response.status != 200:
        error_message = await response.text()
        raise Exception(f"Errore: {response.status} - {error_message}\n")
    request.state.log.debug("Successfull request")

    agent_link = await response.json()

    return agent_link


async def get_agent_presigned_url(
    request: Request
)-> str:
    """
    This async function use the ELevenlabs API return a presigned url to start a conversation with the agent

    Returns:
        presigned_url: this url permit to start conversation with the agent
    """

    request.state.log.info("Get agent link")
    headers = {
        "xi-api-key": settings.elevenlabs_api_key
    }

    params = {
        "agent_id": settings.CESARE
    }

    timeout = aiohttp.ClientTimeout(total=60)
    url = settings.elevenlabs_url_agent_conversation.replace('__method__', 'get_signed_url')
    response = await request.state.session.get(
        url,
        headers=headers,
        params=params,
        timeout=timeout
    )

    # Make request to Elevenlabs
    if response.status != 200:
        error_message = await response.text()
        raise Exception(f"Errore: {response.status} - {error_message}\n")
    request.state.log.debug("Successfull request")

    agent_presigned_url = await response.json()

    return agent_presigned_url

# https://api.elevenlabs.io/v1/convai/conversation/get_signed_url
# https://api.elevenlabs.io/v1/convai/conversation/get_signed_url/