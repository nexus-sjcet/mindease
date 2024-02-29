from services import call
def find_nearest_medical_care(data):
    return f'''Nearest {data["type"]} Hospital is {data["location"]}'''

def set_emergency_contacts(data):
    db = {"name":data["name"], "number":data["number"]}
    return f"Done adding contact: {data}"

def initiate_emergency_call(data):
    call.make_call("+918921964884")
    return f'''Initiated call to {data}'''

def picture(data): 
    pass
def go_outside(data): 
    pass
def spotify(data): 
    pass
def story_time(data): 
    pass


actionsConfig = {
    "find_nearest_medical_care": lambda data: find_nearest_medical_care(data),
    "set_emergency_contacts": lambda data: set_emergency_contacts(data),
    "initiate_emergency_call": lambda data: initiate_emergency_call(data),   
}

recommenedAcriontionsConfig = {
    "picture": lambda data: picture(data),
    "go_outside": lambda data: go_outside(data),
    "spotify": lambda data: spotify(data),   
    "story_time": lambda data: story_time(data),   
}


def getPriority(reponce:dict):
    message = reponce["message"]
    if "actions" in message.keys() and message["actions"]:
        x=""
        for (key, value) in message["actions"].items():
           x += (actionsConfig[key](value)) + "\n"
           
        return x
            
        
    elif "recommended_actions" in message.keys() and message["recommended_actions"]:
        x=""
        for (key, value) in message["actions"].items():
            x+=(recommenedAcriontionsConfig[key](value))  + "\n"
            
        return x
            
    elif "intro_message" in message.keys() and message['intro_message']:
        return message["intro_message"]
    
    elif "replay" in message.keys() and message['replay']:
        return message["replay"]
        
    