# chifoumi.py

import random

def respond(input_text):
    if "lance le jeu chifoumi" in input_text.lower():
        return play_chifoumi()
    else:
        return None

def play_chifoumi():
    choices = ["pierre", "papier", "ciseaux"]
    user_choice = input_or_listen("Choisissez entre pierre, papier ou ciseaux : ").lower()
    bot_choice = random.choice(choices)

    if user_choice not in choices:
        return "Choix invalide. Veuillez choisir entre pierre, papier ou ciseaux."

    result = determine_winner(user_choice, bot_choice)

    return f"Vous avez choisi {user_choice}, Renard a choisi {bot_choice}. Résultat : {result}."

def determine_winner(user_choice, bot_choice):
    if user_choice == bot_choice:
        return "Égalité !"
    elif (user_choice == "pierre" and bot_choice == "ciseaux") or \
         (user_choice == "papier" and bot_choice == "pierre") or \
         (user_choice == "ciseaux" and bot_choice == "papier"):
        return "Vous avez gagné !"
    else:
        return "Renard a gagné !"

def input_or_listen(prompt):
    mode = input("Mode (t: texte, v: vocal) : ").lower()
    if mode == "v":
        return listen(prompt)
    else:
        return input(prompt)

def listen(prompt):
    # Implémenter la reconnaissance vocale ici
    # Cette fonction doit retourner la réponse vocale de l'utilisateur
    return "pierre"  # Exemple de réponse vocale (à remplacer par la vraie implémentation)

