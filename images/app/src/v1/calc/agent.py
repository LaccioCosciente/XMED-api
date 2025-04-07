import os
import aiohttp
import asyncio

from etc.config import settings
from datetime import datetime

from fastapi import Request, UploadFile, File
from fastapi.responses import StreamingResponse, JSONResponse
import pytz
# import speech_recognition as sr
# from elevenlabs import generate, play



async def create_appointment(
    
    text: str
)-> bin:


    ...

# import os
# from fastapi import FastAPI
# from pydantic import BaseModel
# from dotenv import load_dotenv


ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
CALCOM_API_KEY = os.getenv("CALCOM_API_KEY")
EVENT_TYPE_ID = os.getenv("EVENT_TYPE_ID")




async def speak(text: str):
    audio = generate(text=text, api_key=ELEVENLABS_API_KEY)
    play(audio)


def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            return r.recognize_google(audio, language="it-IT")
        except:
            return "Errore nel riconoscimento."


async def create_booking(
    request: Request,
    data: dict
):
    rome = pytz.timezone("Europe/Rome")
    utc = pytz.utc

    dt_start = rome.localize(datetime.strptime(f"{data.date} {data.start_time}", "%Y-%m-%d %H:%M")).astimezone(utc)
    dt_end = rome.localize(datetime.strptime(f"{data.date} {data.end_time}", "%Y-%m-%d %H:%M")).astimezone(utc)

    payload = {
        "eventTypeId": EVENT_TYPE_ID,
        "start": dt_start.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "end": dt_end.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "language": "it",
        "attendees": [{"name": data.name, "email": data.email}]
    }

    headers = {
        "Authorization": f"Bearer {CALCOM_API_KEY}",
        "Content-Type": "application/json"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post("https://api.cal.com/v2/bookings", json=payload, headers=headers) as resp:
            return await resp.json()


# @app.post("/prenota")
# async def prenota_appuntamento(data: Appointment):
#     result = await create_booking(data)
#     if "error" in result:
#         await speak("C'è stato un errore nella prenotazione.")
#         return {"status": "errore", "dettagli": result}
#     await speak("Appuntamento creato con successo.")
#     return {"status": "successo", "dati": result}


# @app.get("/parla")
# async def interazione_vocale():
#     await speak("Dimmi la data e l'orario per il tuo appuntamento.")
#     input_utente = recognize_speech()
#     return {"utente_ha_detto": input_utente}