import os
from dotenv import load_dotenv
from langchain_together import Together
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from kor import create_extraction_chain, Object, Number

load_dotenv()

TOGETHER_API_KEY = os.environ["TOGETHER_API_KEY"]

llm = Together(
    model="mistralai/Mixtral-8x7B-v0.1",
    max_tokens=1024,
    together_api_key=TOGETHER_API_KEY
)

schema = Object(
    id="score",
    attributes=[
        Number(
            id="Openness"
        ),
        Number(
            id="Concientiousness"
        ),
        Number(
            id="Extraversion"
        ),
        Number(
            id="Agreeableness"
        ),
        Number(
            id="Neuroticism"
        ),
    ]
)

def generate_ocean_score(text:str):
    prompt = ChatPromptTemplate.from_template("""
    Generate only a list of scores on a scale of zero to hundred for the given text based on the following parameters in the same order: Openness, Concientiousness, Extraversion, Agreeableness, Neuroticism.
    Definitions:
        Openness: Being open to new experiences
        Concientiousness: tendency to be self disciplined
        Extraversion: Breadth of activities.
        Agreeableness: general concern for social harmony
        Neuroticism: Tendency to have extreme negative emotion
    Text: {text}
    """)

    output_formatter = StrOutputParser()

    chain = create_extraction_chain(llm, schema, encoder_or_encoder_class="json")
    return chain.invoke(text)["text"]["data"]

print(generate_ocean_score("It was fantastic! I finally finished that project I've been working on, and I feel really accomplished. How was your day?"))