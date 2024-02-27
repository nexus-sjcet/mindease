import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def sendMessage(message: str, phone: str):
    """
    message: Text you want to send
    phone: phone number with country code. (+911234567890)
    """
    return client.messages.create(body=message, from_=f'whatsapp:{TWILIO_NUMBER}', to=f"whatsapp:{phone}")

