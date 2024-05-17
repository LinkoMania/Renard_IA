# system_control.py

import os

def respond(input_text):
    if "ferme ton système" in input_text.lower():
        close_system()
        return "Je ferme le système."
    elif "relance ton système" in input_text.lower():
        restart_system()
        return "Je redémarre le système."
    else:
        return None

def close_system():
    # Exécuter la commande pour fermer la fenêtre actuelle
    os.system("Exit")

def restart_system():
    # Exécuter la commande pour lancer un nouveau processus Python dans un nouveau terminal
    os.system("cmd /c start python main.py")
    # Fermer l'instance actuelle du script
    os._exit(0)
