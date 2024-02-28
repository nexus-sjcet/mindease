import os
from dotenv import load_dotenv
from langchain_together import Together
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from kor import create_extraction_chain, Object, Number

load_dotenv()

TOGETHER_API_KEY = os.environ["TOGETHER_API_KEY"]

llm = Together(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    max_tokens=1024,
    together_api_key=TOGETHER_API_KEY
)

schema = Object(
    id="score",
    attributes=[
        Number(
            id="Openness",
            example=[
                ("They rarely venture outside their familiar routines, preferring predictable and comfortable environments.", 0),
                ("They are constantly seeking new knowledge and experiences, actively enrolling in courses and engaging in novel hobbies.", 5),
                ("They thrive on exploration and pushing their boundaries, readily embracing challenges and unfamiliar situations.", 9),
                ("They enjoy delving into complex topics, finding joy in intellectual stimulation and learning new perspectives.", 7),
                ("They are open to trying new things occasionally, but prefer a balance between familiar activities and new experiences.", 3)
            ]
        ),
        Number(
            id="Concientiousness",
            example=[
                ("They prioritize organization and meticulous planning, creating detailed schedules and following them rigorously.", 9),
                ("They often act impulsively without considering long-term consequences, prioritizing immediate gratification over future outcomes.", 0),
                ("They strive for balance, aiming to be thorough while remaining adaptable, making adjustments as needed based on unforeseen circumstances.", 5),
                ("They enjoy a sense of order and structure, yet understand the need for flexibility and adjust their plans when necessary.", 7),
                ("They may struggle with maintaining consistent organization, but prioritize completing tasks eventually, even if it takes longer than planned.", 3)
            ]
        ),
        Number(
            id="Extraversion",
            example=[
                ("They are most comfortable in quiet, solitary environments, finding peace and comfort in their own company.", 0),
                ("They naturally gravitate towards social settings and interactions, drawing energy from engaging with others.", 10),
                ("They enjoy a mix of social activities and introspective time, finding balance and recharge in both settings.", 5),
                ("They can be comfortable in both social and solitary situations, adapting their behavior based on the context and their energy levels.", 7),
                ("While they may prefer quiet environments, they can engage in social interactions when needed, especially with close friends and family.", 3)
            ]
        ),
        Number(
            id="Agreeableness",
            example=[
                ("They prioritize their own needs and desires over the needs of others, often appearing self-centered in their actions.", 0),
                ("They readily sacrifice their own needs for the well-being of others, putting others' needs first even at their own expense.", 10),
                ("They seek solutions that benefit everyone involved, valuing cooperation and compromise in most situations.", 5),
                ("They prioritize fairness and equality, striving to ensure everyone's needs are considered when making decisions.", 7),
                ("They are generally willing to help others when able, but may prioritize their own commitments and responsibilities.", 3)
            ]
        ),
        Number(
            id="Neuroticism",
            example=[
                ("They experience frequent and intense emotional fluctuations, readily displaying emotions and struggling to regulate them at times.", 10),
                ("They rarely experience strong emotions and maintain a calm demeanor, appearing composed and collected even in stressful situations.", 0),
                ("They experience a normal range of emotions but may struggle with regulation at times, requiring conscious effort to manage their emotional responses.", 5),
                ("They tend to be sensitive to criticism and may experience emotional setbacks when faced with challenges.", 7),
                ("They generally maintain a positive outlook, but may experience occasional emotional ups and downs depending on life circumstances.", 3)
            ]
        ),
    ]
)

def generate_ocean_score(text:str):
    prompt = ChatPromptTemplate.from_template("""
    You are a bot that predicts the levels of openness, concientiousness, extraversion, agreeableness and neuroticism from a description of a person. Predict these levels for the text below.
    {text}
    """)

    output_formatter = StrOutputParser()

    chain = create_extraction_chain(llm, schema, encoder_or_encoder_class="json")
    return chain.invoke(text)["text"]["data"]

print(generate_ocean_score("Summary: I am not happy.  don't like to party. I ate sushi for the first time yesterday"))