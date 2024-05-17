# Plugin politesse

import random

def respond(user_input):
    if "merci" in user_input:
        responses = ["De rien, maître.", "Je vous en prie.", "C'est un plaisir.", "Pas de problème.", "Toujours à votre service."]
        return random.choice(responses)
    elif "bonne nuit" in user_input:
        responses = ["Bonne nuit.", "Dormez bien.", "Faites de beaux rêves.", "À demain.", "Bonne nuit, que les anges veillent sur vous."]
        return random.choice(responses)
    elif "bonjour" in user_input or "salut" in user_input:
        name = user_input.split()[-1]
        return f"Bonjour {name.capitalize()} !"
    elif "bonsoir" in user_input:
        name = user_input.split()[-1]
        return f"Bonsoir {name.capitalize()} !"
    else:
        return None
