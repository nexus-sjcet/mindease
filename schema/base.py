# from langchain.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from kor import create_extraction_chain, Object, Text, Option, Selection


actions = Object(
    id="actions",
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
                Option(id="family", description="Call relatives and family members"),
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

def getSchema():
    return Object(
        id="message",
        description ='''You are a health care assistant, working for people who suffer small mental and stress issues. You need to engage with these people and talk to them about there life. You can tell stories, listern to them, and teach them about the importance of having purpose in life. Return mutliple object attributes. 
                    Prioritize healthy habits: Regular exercise, balanced meals, and sufficient sleep contribute significantly to stress resilience.
                 Mindfulness and relaxation techniques: Techniques like deep breathing, meditation, and progressive muscle relaxation can activate your body's relaxation response, helping you manage stress in the moment.
                 Engage in activities you enjoy: Participating in hobbies and activities you find enjoyable can bring pleasure and a sense of accomplishment, reducing stress levels.
                 Connect with loved ones: Strong social connections provide support and belonging, which can buffer the impact of stress.''',
        attributes=[
            Text(
                id="intro_message",
                description="Optional Introduction or first time Messsage for end user, take time and understand previous summary and continue conversations. Use smiling emojies and casual genz words to keep up the younth.",
                examples=[
                    ("This user is having mid life crises, age 44, unmarried.","Hi Mate, how's life?"),
                    ("This user is so busy with his work, might need some break from that.","Long time, no see. What are you doing right now? "),
                    ("This user is a student, might need someone to talk to.","How's your studying going? Wanna take a break, Im free to talk by the way"),
                ],
                many=False,
            ),
            Text(
                id="replay",
                description="User said something about something, understand it, listen to it and make better replys like a therapist. Use minimal words and use sad emojies to learn for more ",
                examples=[
                    ("I'm having a bad day, you know life hits different sometimes","Hmm.. tell me more"),
                    ("My wife left me, she was love of my life, I cant live without her","Love is something everyone deserves, tell me more, what happend to her?"),
                    ("I was a great student, i used to study new things everyday, but now i dont know what happend to me, lost that interest.","why do you think that, any particular reason?"),
                    ("Everyone want money and fame, no one wants love anymore, i think i lost the purpose 😢","I had that feeling back in my days too. Sometimes having no purpose gives happiness too, Tell me, you want happiness or purpose"),
                ],
                many=False,
            ),
            Text(
                id="recommended_actions",
                description="Some fun and casual tasks to reccommend end user for his/her stress managements, user can choose",
                examples=[
                    ("Let take picture of what are you doing", "picture"),
                    ("I recommend you to go outside and play with your friends", "go_outside"),
                    ("Take the spotify and play some lofi, so you focus on working", "spotify"),
                    ("I got some stories for you, wanna hear?", "story_time"),
                ],
                many=True
            ),
            Text(
                id="recommended_actions",
                description="Some fun and casual tasks to reccommend end user for his/her stress managements, user can choose",
                examples=[
                    ("Let take picture of what are you doing", "picture"),
                    ("I recommend you to go outside and play with your friends", "go_outside"),
                    ("Take the spotify and play some lofi, so you focus on working", "spotify"),
                    ("I got some stories for you, wanna hear?", "story_time"),
                ],
                many=True
            ),
            actions
        ]
    )