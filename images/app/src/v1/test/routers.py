from src.v1.test import first_step
from fastapi import Request, APIRouter, UploadFile, File

router = APIRouter()

@router.get(
    "/audio_from_text",
    response_model=None,
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


@router.post(
    "/text_from_audio",
    response_model=None,

)
async def get_text_from_audio(
        request: Request,
        file: UploadFile = File(...)
):

    """This API given a text returns the audio version of it

    **Limitation**:
    No authentication required
    """

    return await first_step.get_text_from_audio(
        request,
        file 
    )