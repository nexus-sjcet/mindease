import os
from dotenv import load_dotenv
from langchain_together import Together
from langchain_core.prompts import ChatPromptTemplate
from kor import create_extraction_chain, Object, Text
from typing import List, Tuple

load_dotenv()

TOGETHER_API_KEY = os.environ["TOGETHER_API_KEY"]

llm = Together(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    max_tokens=1024,
    together_api_key=TOGETHER_API_KEY
)

schema = Object(
    id="history",
    attributes=[
        Text(
            id="summary",
            examples=[
                ("""
                [summary] none
                Human: Hello.
                AI: Hi! How can I help you?
                """, "A conversation with only greetings"),
                ("""
                [summary] A conversation about the universe.
                Human: Stars really are a beautiful thing.
                AI: I agree, stars are very beautiful
                Human: I want to be a star one day
                AI: It is good to have goals in life. However, it is okay if they change too.
                """, "A conversation about goals and change")
            ]
        )
    ]
)

def summarize_history(prompt:str, response:str, history:List[Tuple[str, str]]=[], summary:str="none"):
    history_string = f"""[summary] {summary}
    """
    for (entity, message) in history:
        history_string += f"{entity}: {message}\n"

    history_string += f"""
    Human: {prompt}
    AI: {response}
    """

    chain = create_extraction_chain(llm, schema, encoder_or_encoder_class="json")
    return chain.invoke(history_string)["text"]["data"]["history"]["summary"]

# print(summarize_history("I'm depressed.", "Depression can be very diffult to go through, I'm sorry you're going through a hard time. How can I help?", history=[
#     ("Human", "Hi"),
#     ("AI", "Hello")
# ]))