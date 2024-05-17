import random

# Chemin vers le fichier de citations
CITATION_FILE_PATH = "plugins/citation/citation.txt"

def respond(user_input):
    if "renard dis-moi une citation" in user_input.lower():
        return get_random_citation()
    else:
        return None

def get_random_citation():
    try:
        # Lire les citations depuis le fichier
        with open(CITATION_FILE_PATH, "r", encoding="utf-8") as file:
            citations = file.readlines()
        
        # Choisir une citation aléatoire
        random_citation = random.choice(citations).strip()
        
        return random_citation
    except FileNotFoundError:
        return "Désolé, le fichier de citations est introuvable."
