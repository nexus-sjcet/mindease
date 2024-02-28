import os
from dotenv import load_dotenv
from langchain_together import Together
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from typing import List, Tuple

load_dotenv()

TOGETHER_API_KEY = os.environ["TOGETHER_API_KEY"]

llm = Together(
    model="mistralai/Mixtral-8x7B-v0.1",
    max_tokens=1024,
    together_api_key=TOGETHER_API_KEY
)

def generate_message(message:str, history:List[Tuple[str]]=[]):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Limit the response to one line"),
        *history,
        ("human", "{input}")
    ])

    output_formatter = StrOutputParser()
    chain = prompt | llm | output_formatter

    return chain.invoke({
        "input": message
    })
