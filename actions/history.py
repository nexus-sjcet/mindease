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

schema = Object(
    id="history",
    attributes=[
        Text(
            id="summary",
            examples=[
                ("""
                Human: Hello.
                AI: Hi! How can I help you?
                """, "A conversation with only greetings")
            ]
        )
    ]
)

def summarize_history(history: str):
    prompt = ChatPromptTemplate.from_template("""
    You are an ai that takes a conversation history and summarizes it. summarize the history below.
    {history}
    """)

    chain = create_extraction_chain(llm, schema, encoder_or_encoder_class="json")
    return chain.invoke(history)["text"]["data"]["history"]["summary"]

print(summarize_history("""
Human: Hi
AI: Hello
"""))