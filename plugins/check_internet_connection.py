# internet_check.py

import requests

def check_internet_connection():
    try:
        # Envoyer une requête à google.com
        response = requests.get("https://www.google.com")
        # Si la réponse est réussie (code de statut 200), alors il y a une connexion Internet
        if response.status_code == 200:
            return "Oui, il y a une connexion Internet."
        else:
            return "Non, il n'y a pas de connexion Internet."
    except requests.ConnectionError:
        # Si une erreur de connexion se produit, alors il n'y a pas de connexion Internet
        return "Non, il n'y a pas de connexion Internet."

def respond(input_text):
    if "renard il y a internet" in input_text.lower():
        return check_internet_connection()
    else:
        return None

