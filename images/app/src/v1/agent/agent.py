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
        presigned_url (str): this url permit to start conversation with the agent
    """

    request.state.log.info("Get agent link")
    headers = {
        "xi-api-key": settings.elevenlabs_api_key
    }

    params = {
        "agent_id": settings.CESARE
    }

    timeout = aiohttp.ClientTimeout(total=60)
    url = os.path.join(settings.elevenlabs_url_agent_conversation, 'get_signed_url')
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


async def get_agent_conversations_list(
    request: Request
)-> dict:
    """
    This async function use the ELevenlabs API return conversations list

    Returns:
        conversations_list_json (dict): returns a list of all conversations
    """

    request.state.log.info("Get agent link")
    headers = {
        "xi-api-key": settings.elevenlabs_api_key
    }

    
    timeout = aiohttp.ClientTimeout(total=60)
    url = os.path.join(settings.elevenlabs_url_agent_conversation + 's')

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

    conversations_list_json = await response.json()

    return conversations_list_json


async def get_agent_conversation_details(
    request: Request,
    conversation_id: str
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
        "xi-api-key": settings.elevenlabs_api_key
    }

    timeout = aiohttp.ClientTimeout(total=60)
    url = os.path.join(settings.elevenlabs_url_agent_conversation + 's', conversation_id)
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

    conversations_details_json = await response.json()
    return conversations_details_json