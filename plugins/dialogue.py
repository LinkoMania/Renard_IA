# dialogue.py

import random

def respond(input_text):
    # Phrases-clés
    key_phrases = [
        "comment vas-tu",
        "quel est ton nom",
        "quel temps fait-il",
        "qu'est-ce que tu fais",
        "quelle est ta couleur préférée",
        "parle-moi de toi",
        "raconte une blague",
        "quels sont tes hobbies",
        "quelle est ta musique préférée",
        "tu es là"
    ]

    # Réponses aléatoires pour chaque phrase-clé
    responses = {
        "comment vas-tu": [
            "Je vais bien, merci ! Et vous ?",
            "Ça va plutôt bien aujourd'hui, et vous ?",
            "Tout va bien de mon côté, et vous ?"
        ],
        "quel est ton nom": [
            "Je suis Renard, votre assistant virtuel !",
            "Mon nom est Renard, à votre service !",
            "Je m'appelle Renard, enchanté de vous rencontrer !"
        ],
        "quel temps fait-il": [
            "Il fait beau et ensoleillé !",
            "Le temps est plutôt nuageux aujourd'hui.",
            "Il pleut des cordes dehors !"
        ],
        "tu es là": [
            "Oui monsieur",
            "Oui maître",
            "Où pensez-vous que je suis ?"
        ]
        # Ajoutez des réponses pour les autres phrases-clés de manière similaire
    }

    # Vérifier si l'entrée correspond à l'une des phrases-clés
    for key_phrase in key_phrases:
        if key_phrase in input_text.lower():
            return random.choice(responses.get(key_phrase, ["Je ne sais pas quoi répondre."]))

    # Si aucune phrase-clé n'est trouvée dans l'entrée
    return None

# Test du plugin de dialogue

