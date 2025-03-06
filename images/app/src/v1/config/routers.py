from src.v1.config import first_step
from fastapi import Request, APIRouter


router = APIRouter()

@router.get(
    "/audio_from_text"
)
async def get_audio_from_text(
        request: Request,
        text: str
):

    """This API given a text returns the audio version of it

    **Limitation**:
    No authentication required
    """

    return await first_step.get_audio_from_text(
        request,
        text
    )