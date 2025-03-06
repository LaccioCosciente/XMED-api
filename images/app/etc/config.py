
import os
from dotenv import load_dotenv
load_dotenv()

class Settings():

    elevenlabs_api_key: str = os.getenv('ELEVENLABS_API_KEY')
    voice_id: str="JBFqnCBsd6RMkjVDRZzb"
    elevenlabs_url: str = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    # SERVICE CONFIG
    TITLE: str = "XMED api service"
    VERSION: str = "0.0.1-alpha"
    ROOT_PATH: str = ""
    SUMMARY: str = "These APi will allow yuo to perform a smooth experience using Elevenlabs service"

settings = Settings()