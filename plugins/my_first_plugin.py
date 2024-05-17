# my_first_plugin.py

import random

def respond(input_text):
    responses = [
        "Bonjour, que puis-je faire pour vous ?",
        "Salut, comment puis-je vous aider ?",
        "Coucou, que puis-je faire pour vous ?",
        "Hello, comment puis-je vous aider ?",
        "Salutations, que puis-je faire pour vous ?"
    ]
    
    greetings = [
        "Salut !",
        "Yo !",
        "Bonjour !",
        "Salutations !"
    ]
    
    feelings = [
        "Tranquille et toi ?",
        "Ça va bien, merci !",
        "Tout va bien de mon côté, merci !",
        "Je me porte bien, et toi ?"
    ]
    
    activities = [
        "Je discute avec toi !",
        "Je suis là pour répondre à tes questions.",
        "Je suis ton assistant vocal personnalisé.",
        "Je suis un programme informatique conçu pour interagir avec toi !"
    ]
    
    if "bonjour renard" in input_text.lower():
        return random.choice(responses)
    elif "salut renard" in input_text.lower() or "yo renard" in input_text.lower():
        return random.choice(greetings)
    elif "ça va renard" in input_text.lower() or "tranquille ou quoi renard" in input_text.lower():
        return random.choice(feelings)
    elif "tu fais quoi renard" in input_text.lower() or "sa fais quoi renard" in input_text.lower():
        return random.choice(activities)
    elif "tu es qui renard" in input_text.lower() or "qui es tu renard" in input_text.lower():
        return "Je suis un bot conçu pour te fournir des réponses."
    else:
        return None  # Aucune réponse si la phrase n'est pas reconnue
