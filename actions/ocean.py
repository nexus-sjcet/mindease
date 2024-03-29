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
    together_api_key=TOGETHER_API_KEY,
)

schema = Object(
    id="score",
    description="Process of converting human charachers attributes in 0 to 10, where 0 is very low and 10 is very high. The Big Five model was built to understand the relationship between personality and academic behaviour. so we need 5 type of numerical values from description of a person's image.",
    attributes=[
        Number(
            id="openness",
            description="Openness is a general appreciation for art, emotion, adventure, unusual ideas, imagination, curiosity, and variety of experience. People who are open to experience are intellectually curious, open to emotion, sensitive to beauty, and willing to try new things. They tend to be, when compared to closed people, more creative and more aware of their feelings. They are also more likely to hold unconventional beliefs. From the description of image, get apporpriate openness.",
            examples=[
                (
                    "They rarely venture outside their familiar routines, preferring predictable and comfortable environments.",
                    0,
                ),
                (
                    "They are constantly seeking new knowledge and experiences, actively enrolling in courses and engaging in novel hobbies.",
                    5,
                ),
                (
                    "They thrive on exploration and pushing their boundaries, readily embracing challenges and unfamiliar situations.",
                    9,
                ),
                (
                    "They enjoy delving into complex topics, finding joy in intellectual stimulation and learning new perspectives.",
                    7,
                ),
                (
                    "They are open to trying new things occasionally, but prefer a balance between familiar activities and new experiences.",
                    3,
                ),
            ],
        ),
        Number(
            id="conscientiousness",
            description="Conscientiousness is a tendency to be self-disciplined, act dutifully, and strive for achievement against measures or outside expectations. It is related to people's level of impulse control, regulation, and direction. High conscientiousness is often perceived as being stubborn and focused. Low conscientiousness is associated with flexibility and spontaneity, but can also appear as sloppiness and lack of reliability. High conscientiousness indicates a preference for planned rather than spontaneous behaviour.",
            examples=[
                (
                    "They prioritize organization and meticulous planning, creating detailed schedules and following them rigorously.",
                    9,
                ),
                (
                    "They often act impulsively without considering long-term consequences, prioritizing immediate gratification over future outcomes.",
                    0,
                ),
                (
                    "They strive for balance, aiming to be thorough while remaining adaptable, making adjustments as needed based on unforeseen circumstances.",
                    5,
                ),
                (
                    "They enjoy a sense of order and structure, yet understand the need for flexibility and adjust their plans when necessary.",
                    7,
                ),
                (
                    "They may struggle with maintaining consistent organization, but prioritize completing tasks eventually, even if it takes longer than planned.",
                    3,
                ),
            ],
        ),
        Number(
            id="extroversion",
            description="Extraversion is characterised by breadth of activities (as opposed to depth), surgency from external activities/situations, and energy creation from external means.The trait is marked by pronounced engagement with the external world. Extraverts enjoy interacting with people, and are often perceived as energetic. They tend to be enthusiastic and action-oriented. They possess high group visibility, like to talk, and assert themselves. Extraverts may appear more dominant in social settings, as opposed to introverts in that setting.",
            examples=[
                (
                    "They are most comfortable in quiet, solitary environments, finding peace and comfort in their own company.",
                    0,
                ),
                (
                    "They naturally gravitate towards social settings and interactions, drawing energy from engaging with others.",
                    10,
                ),
                (
                    "They enjoy a mix of social activities and introspective time, finding balance and recharge in both settings.",
                    5,
                ),
                (
                    "They can be comfortable in both social and solitary situations, adapting their behavior based on the context and their energy levels.",
                    7,
                ),
                (
                    "While they may prefer quiet environments, they can engage in social interactions when needed, especially with close friends and family.",
                    3,
                ),
            ],
        ),
        Number(
            id="agreeableness",
            description="Agreeableness is the general concern for social harmony. Agreeable individuals value getting along with others. They are generally considerate, kind, generous, trusting and trustworthy, helpful, and willing to compromise their interests with others.Agreeable people also have an optimistic view of human nature.",
            examples=[
                (
                    "They prioritize their own needs and desires over the needs of others, often appearing self-centered in their actions.",
                    0,
                ),
                (
                    "They readily sacrifice their own needs for the well-being of others, putting others' needs first even at their own expense.",
                    10,
                ),
                (
                    "They seek solutions that benefit everyone involved, valuing cooperation and compromise in most situations.",
                    5,
                ),
                (
                    "They prioritize fairness and equality, striving to ensure everyone's needs are considered when making decisions.",
                    7,
                ),
                (
                    "They are generally willing to help others when able, but may prioritize their own commitments and responsibilities.",
                    3,
                ),
            ],
        ),
        Number(
            id="neuroticism",
            description="Neuroticism is the tendency to have strong negative emotions, such as anger, anxiety, or depression.It is sometimes called emotional instability, or is reversed and referred to as emotional stability.",
            examples=[
                (
                    "They experience frequent and intense emotional fluctuations, readily displaying emotions and struggling to regulate them at times.",
                    10,
                ),
                (
                    "They rarely experience strong emotions and maintain a calm demeanor, appearing composed and collected even in stressful situations.",
                    0,
                ),
                (
                    "They experience a normal range of emotions but may struggle with regulation at times, requiring conscious effort to manage their emotional responses.",
                    5,
                ),
                (
                    "They tend to be sensitive to criticism and may experience emotional setbacks when faced with challenges.",
                    7,
                ),
                (
                    "They generally maintain a positive outlook, but may experience occasional emotional ups and downs depending on life circumstances.",
                    3,
                ),
            ],
        ),
    ],
)


def generate_ocean_score(text: str):
    chain = create_extraction_chain(llm, schema, encoder_or_encoder_class="json")
    return chain.run(text)["data"]