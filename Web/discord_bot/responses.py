import random

#function logic to return a response 
def handle_response(message) -> str:
    #process the message to lowercase
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'

    if p_message == 'roll':
        return str(random.randint(1,6))

    if p_message == '!help':
        return "` this is a help message that you can modify`"

    
