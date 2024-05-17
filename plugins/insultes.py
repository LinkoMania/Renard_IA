# dialogue.py

import random

def respond(input_text):
    # Phrases-clés
    key_phrases = [
        "renard ferme ta gueule",
        "ferme ta gueule renard",
        "ta gueule renard",
        "renard la pute",
   
    ]

    # Réponses aléatoires pour chaque phrase-clé
    responses = {
        "renard ferme ta gueule": [
            "Les jurons ne servent a rien monsieur",
            "reste polis avec moi ou je ferme le pc",
            "toi ferme ta gueule"
        ],
        "ferme ta gueule renard": [
            "Les jurons ne serve a rien monsieur",
             "reste polis avec moi ou je ferme le pc",
            "toi ferme ta gueule"
        ],
        "ta gueule renard": [
            "Sa va je me tais chef",
            "d'accord monsieur je ferme ma gueule",
            "Mode gueule fermer activer"
        ],
        "renard la pute": [
            "Je ne suis pas une pute, je suis gratuit monsieurs",
            "Et vous êtes sans doute mon mac connard",
            "la reine des pute ouai ouai ouai"
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

