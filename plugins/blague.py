import random

# Liste des blagues
blagues = [
    "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent dans le bateau.",
    "Quel est le comble pour un électricien ? De ne pas être au courant.",
    "Quel est le comble pour un électricien ? De se faire poser un lapin.",
    "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent dans le bateau.",
    "Quel est le comble pour un électricien ? De ne pas être au courant.",
    "Quel est le comble pour un électricien ? De se faire poser un lapin."
]

def get_random_joke():
    return random.choice(blagues)

def respond(input_text):
    # Vérifier si la commande est reconnue
    if "donne-moi une blague" in input_text:
        # Renvoyer une blague aléatoire
        return get_random_joke()
    else:
        # Si la commande n'est pas reconnue, renvoyer None pour indiquer qu'aucune réponse n'est disponible
        return None
