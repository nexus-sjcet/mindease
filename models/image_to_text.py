import requests
from requests.auth import HTTPBasicAuth
import json
import io
import os
import base64
from dotenv import load_dotenv

from rich import print
from PIL import Image

load_dotenv()

ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

class LLAVA:
    SYSTEM_PROMPT = """Your are a chatbot and a detailed information extraction asssitance. 
The assistant that gives helpful, detailed, and polite answers to the human's questions. Information includes details of surroundings, objects and peoples emotions in it.
Never forget to extract information about emotional attachment of people in it"""

    def __init__(self):
        self.url = 'http://127.0.0.1:8080/completion'
        self.system_prompt = self.SYSTEM_PROMPT

        self.parameters = {
            "stream": True,
            "n_predict": 400,
            "temperature": 0.2,
            "stop": ["</s>", "Llama:", "User:"],
            "repeat_last_n": 256,
            "repeat_penalty": 1.18,
            "top_k": 40,
            "top_p": 0.7,
            "tfs_z": 1,
            "typical_p": 1,
            "presence_penalty": 0,
            "frequency_penalty": 0,
            "mirostat": 0,
            "mirostat_tau": 5,
            "mirostat_eta": 0.1,
            "grammar": "",
            "n_probs": 0,
            "cache_prompt": True,
            "slot_id": -1,
        }

    def process_image(self, image):
        if image.startswith('http://') or image.startswith('https://'):
            basic = HTTPBasicAuth(ACCOUNT_SID, AUTH_TOKEN)
            response = requests.get(image, auth=basic)
            response.raise_for_status()
            img_data = io.BytesIO(response.content)
        else:
            img_data = image

        with Image.open(img_data) as img:
            img_bytes = io.BytesIO()
            img.save(img_bytes, format=img.format)
            encoded_img_bytes = base64.b64encode(img_bytes.getvalue()).decode('utf-8')

        return encoded_img_bytes


    def complete(self, image_path, prompt="", stream=False):
        enriched_prompt = f"USER:[img-10]{prompt}\nASSISTANT:"

        encoded_img_bytes = self.process_image(image_path)        
        data = self.parameters | {
            "prompt": enriched_prompt,
            "image_data": [{"data": encoded_img_bytes, "id": 10}]
        }

        response = requests.post(
            url=self.url,
            headers={'Accept': 'text/event-stream'},
            data=json.dumps(data),
            stream=True
        )

        if stream:
            def response_generator():
                for line in response.iter_lines():
                    if line:
                        line_str = line.decode('utf-8')
                        if line_str.startswith('data: '):
                            json_str = line_str[6:]
                            try:
                                json_data = json.loads(json_str)
                                yield json_data["content"]
                            except json.JSONDecodeError:
                                pass
            return response_generator()
        else:
            content = ""
            for line in response.iter_lines():
                if line:
                    line_str = line.decode('utf-8')
                    if line_str.startswith('data: '):
                        json_str = line_str[6:]
                        try:
                            json_data = json.loads(json_str)
                            content += json_data["content"]
                        except json.JSONDecodeError:
                            pass
            return content
        
def llava(url:str):
    client =  LLAVA()
    return client.complete(url)
    
