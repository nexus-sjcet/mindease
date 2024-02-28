import os
from dotenv import load_dotenv
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

load_dotenv()

ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = "+17814293189"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def make_call(phone:str):
    client.calls.create(
        url='http://demo.twilio.com/docs/voice.xml',
        to=phone,
        from_=TWILIO_NUMBER
    )

def dial(phone:str):
    response = VoiceResponse()
    response.dial(phone)
    return response