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
    id="message",
    attributes=[
        Text(
            id="new",
            examples=[(
                """
                [summary] A conversation about stress
                Human: What can I do?
                """, """
                Prioritize healthy habits: Regular exercise, balanced meals, and sufficient sleep contribute significantly to stress resilience.
                Mindfulness and relaxation techniques: Techniques like deep breathing, meditation, and progressive muscle relaxation can activate your body's relaxation response, helping you manage stress in the moment.
                Engage in activities you enjoy: Participating in hobbies and activities you find enjoyable can bring pleasure and a sense of accomplishment, reducing stress levels.
                Connect with loved ones: Strong social connections provide support and belonging, which can buffer the impact of stress.
                """
            ), (
                """
                [summary] none
                Human: Hi
                """, """
                Hello! How can I help you today?
                """
            )]
        )
    ]
)

def generate_message(message:str, summary:str="none"):
    chain = create_extraction_chain(llm, schema, encoder_or_encoder_class="json")
    return chain.invoke(f"""
    [summary] {summary}
    Human: {message}
    """)["text"]["data"]["message"]["new"].strip()

# print(generate_message("Hi, what can i do", "nA conversation about depression"))