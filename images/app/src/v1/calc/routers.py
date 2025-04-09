from src.v1.calc import calc
from fastapi import Request, APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get(
    "/get_calc_info",
    response_model=None,
)
async def get_calc_info(
        request: Request
):

    """This API given a text returns the audio version of it

    **Limitation**:
    No authentication required
    """

    response = await calc.get_calc_info(
        request
    )
    return JSONResponse(content=response)
