import os
from dotenv import load_dotenv
from langchain_together import Together
from langchain_core.prompts import ChatPromptTemplate
from kor import create_extraction_chain, Object, Text

load_dotenv()

TOGETHER_API_KEY = os.environ["TOGETHER_API_KEY"]

llm = Together(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    max_tokens=1024,
    together_api_key=TOGETHER_API_KEY
)

