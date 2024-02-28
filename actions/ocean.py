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
    Input: A piece of text (e.g., a news article, social media post, email, etc.)

    Output: A score between 0 and 1 for each of the Big Five personality traits (OCEAN):

        Openness (O): How open-minded and receptive to new ideas is the text?
        Conscientiousness (C): How organized, detail-oriented, and self-disciplined is the text?
        Extraversion (E): How outgoing, social, and assertive is the text?
        Agreeableness (A): How cooperative, compassionate, and helpful is the text?
        Neuroticism (N): How emotional, anxious, and prone to negative emotions is the text?

    Instructions:

        Analyze the input text for linguistic cues related to each personality trait.
        Consider:
            Openness: Keywords like "explore," "innovative," "curious," etc. Conversely, "traditional," "conventional," etc. might indicate lower openness.
            Conscientiousness: Keywords like "plan," "organize," "efficient," etc. Conversely, "impulsive," "careless," "disorganized," etc. might indicate lower conscientiousness.
            Extraversion: Keywords like "outgoing," "talkative," "assertive," etc. Conversely, "introverted," "shy," "reserved," etc. might indicate lower extraversion.
            Agreeableness: Keywords like "cooperative," "helpful," "compassionate," etc. Conversely, "argumentative," "selfish," "critical," etc. might indicate lower agreeableness.
            Neuroticism: Keywords like "anxious," "worried," "stressed," etc. Conversely, "calm," "relaxed," "stable," etc. might indicate lower neuroticism.
        Assign a score between 0 and 1 for each trait based on the frequency and intensity of these cues (higher frequency and intensity = higher score).
        Consider the overall context and sentiment of the text to further refine the scores.

    Text: {text}
    """)

    output_formatter = StrOutputParser()

    chain = create_extraction_chain(llm, schema, encoder_or_encoder_class="json")
    return chain.invoke(text)["text"]["data"]["score"]

print(generate_ocean_score("It was fantastic! I finally finished that project I've been working on, and I feel really accomplished. How was your day?"))