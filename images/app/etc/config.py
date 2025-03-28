import os
from dotenv import load_dotenv
load_dotenv()

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
PREFIX = os.path.dirname(CURRENT_DIR)

class Settings():

    # ========== DEBUG ==========
    DEVELOP: str = True
    TITLE: str = "XMED api service"
    VERSION: str = "0.0.1-alpha"
    ROOT_PATH: str = ""
    SUMMARY: str = "These APi will allow yuo to perform a smooth experience using Elevenlabs service"

    # ========== TOKENS ==========
    elevenlabs_api_key: str = os.getenv('ELEVENLABS_API_KEY')
    voice_id: str="JBFqnCBsd6RMkjVDRZzb"

    # ========== paths-urls ==========
    elevenlabs_url: str = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

settings = Settings()
