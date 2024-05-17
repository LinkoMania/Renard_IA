# ouvrir_dossier.py

import os

def respond(input_text):
    if "renard ouvre mes documents" in input_text.lower():
        open_folder(os.path.expanduser('~\Documents'))
        return "Ouverture du dossier Mes Documents."
    elif "renard ouvre mes images" in input_text.lower():
        open_folder(os.path.expanduser('~\Pictures'))
        return "Ouverture du dossier Mes Images."
    elif "renard ouvre mes musiques" in input_text.lower():
        open_folder(os.path.expanduser('~\Music'))
        return "Ouverture du dossier Mes Musiques."
    elif "renard ouvre backup" in input_text.lower():
        open_folder("D:\\backup")
        return "Ouverture du dossier Backup."
    elif "renard ouvre jeux" in input_text.lower():
        open_folder("E:\\jeux")
        return "Ouverture du dossier Jeux."
    else:
        return None

def open_folder(folder_path):
    os.system(f'explorer "{folder_path}"')

if __name__ == "__main__":
    input_text = input("Entrez votre texte : ")
    response = respond(input_text)
    if response:
        print(response)
    else:
        print("Commande non reconnue.")
