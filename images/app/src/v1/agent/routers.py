from src.v1.agent import agent
from fastapi.responses import JSONResponse

from fastapi import Request, APIRouter

router = APIRouter()

@router.get(
    "/create_booking",
    response_model=None,
)
async def create_booking(
        request: Request,
        data: dict
):

    """This API given a text returns the audio version of it

    **Limitation**:
    No authentication required
    """

    response = await agent.create_booking(
        request,
        data 
    )
    return JSONResponse(content=response)
