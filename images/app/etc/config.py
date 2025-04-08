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

    # Agent ids
    CESARE: str = 'JQs3sHjD1wG0KtfcTji3'

    # ========== TOKENS ==========
    elevenlabs_api_key: str = os.getenv('ELEVENLABS_API_KEY', "sk_464c5738b2fb145b274e2087a05d7cc089d33d380d26e37c")
    voice_id: str="JBFqnCBsd6RMkjVDRZzb"

    # calc auth
    calc_api_key: str = 'cal_live_d8ab90417cf3f9fb60b9e70d21832627'

    # ========== paths-urls ==========
    text_to_speech: str = "text-to-speech"
    speech_to_text: str = "speech-to-text"

    elevenlabs_url: str = "https://api.elevenlabs.io/v1/__method__/"

    # Agent
    elevenlabs_url_agent: str = "https://api.elevenlabs.io/v1/convai/agents/agent_id"
    
    # Conversation Agent
    elevenlabs_url_agent_conversation: str = 'https://api.elevenlabs.io/v1/convai/conversation'

    save_audio_path: str = '/home/emir/Documents/personal/XMED/XMED-api/images/app/var/audios'

settings = Settings()
