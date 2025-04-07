from src.v1.agent import agent
from fastapi import Request, APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get(
    "/get_agent_info",
    response_model=None,
)
async def get_agent_info(
        request: Request
):

    """This API given a text returns the audio version of it

    **Limitation**:
    No authentication required
    """

    response = await agent.get_agent_info(
        request
    )
    return JSONResponse(content=response)


@router.get(
    "/get_agent_link",
    response_model=None,
)
async def get_agent_link(
        request: Request
):

    """This API given a text returns the audio version of it

    **Limitation**:
    No authentication required
    """

    response = await agent.get_agent_link(
        request
    )
    return JSONResponse(content=response)


@router.get(
    "/get_agent_presigned_url",
    response_model=None,
)
async def get_agent_presigned_url(
        request: Request
):

    """This API return a presigned url

    **Limitation**:
    authentication required
    """

    response = await agent.get_agent_presigned_url(
        request
    )
    return JSONResponse(content=response)