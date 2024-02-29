import os
from dotenv import load_dotenv
from langchain_together import Together
from langchain_core.prompts import ChatPromptTemplate
from kor import create_extraction_chain, Object, Selection, Option
from typing import List, Tuple

load_dotenv()

TOGETHER_API_KEY = os.environ["TOGETHER_API_KEY"]

llm = Together(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    max_tokens=1024,
    together_api_key=TOGETHER_API_KEY
)

actions = Object(
    id="actions",
    many=True,
    description ="Actions that are required to run while user mensions his requirements",
    attributes=[
        Object(
            attributes=[],
            id="find_nearest_medical_care",
            description ="Action type if user need health care support. Also pass data such as nearest location and type of health support",
            examples=[
                ("Im having a mental break done, i need help", {"location":"NONE", "type":"mental"}),
                ("My sister is having heart attack, we live in new york", {"location":"new york", "type":"icu"}),
                ("Right now i here at a remote location called kochi, and its time for my regular gynaecologist visit", {"location":"kochi", "type":"gynaecologist"}),
                ("Find nearest trust worthy hospital for my surgery", {"location":"NONE", "type":"surgery"}),
            ]
        ),
        Object(
            attributes=[],
            id="set_emergency_contacts",
            description ="Action type if user wants to save his family or relative information, so in future this details might save their life. Extract name and phone number",
            examples=[
                ("I have a friend ALAN who might save my life anytime, his number is 1234567890", {"name":"ALAN", "number":"1234567890"}),
                ("My mother's number is 6543210987", {"name":"Mother", "number":"6543210987"}),
                ("Save this number, 3456734569, this guy might be help full", {"name":"NONE", "number":"3456734569"}),
                ("My fathers name is Sandeep, number 9876526782", {"name": "NONE", "number":"9876526782"}),
            ]
        ),
        Selection(
            id="initiate_emergency_call",
            options=[
                Option(id="family", description="Call relatives and family members such as mom, dad, brother etc (no needed to be an emergency situation)"),
                Option(id="police", description="if user needs police force support or he is trying to hurt him selfs (like suicide)"),
                Option(id="health", description="if user needs emergency medical support or an anbulance"),
                Option(id="none", description="if user needs no help, he is just messing with everyone"),
            ],
            description ="Action type if user tells that he is under a emergency situation and wants to inform family and relatives",
            examples=[
                ("I think im deading", "police"),
                ("Im just kiding, im not dieing ", "none"),
                ("I have an acciedent, reached hospital, but i just want to talk to my family ", "family"),
                ("Im hate my life, i just wanted to die, no kidding", "police"),
                ("Call someone, im having medical emergency here", "health"),
                ("Call 911", "police"),
                ("I need an anbulance", "health"),
            ]
        )
    ]
    
)

def get_action(message:str):
    chain = create_extraction_chain(llm, actions, encoder_or_encoder_class="json")
    return chain.run(message)["data"]