# bruitage.py
import os
import pygame

# Chemin vers le dossier contenant les fichiers audio
AUDIO_FOLDER = "plugins/bruitage_songs"

def play_sound(animal):
    pygame.init()
    pygame.mixer.init()
    try:
        sound_path = os.path.join(AUDIO_FOLDER, animal.lower() + ".mp3")
        sound = pygame.mixer.Sound(sound_path)
        sound.play()
    except FileNotFoundError:
        print(f"Le son de {animal} n'a pas été trouvé.")

def list_available_animals():
    animals = [file.split(".")[0] for file in os.listdir(AUDIO_FOLDER)]
    return animals

def respond(input_text):
    if "renard" in input_text.lower() and ("fais le bruit du" in input_text.lower() or "fait le bruit du" in input_text.lower()):
        animals_available = list_available_animals()
        input_text = input_text.lower()
        for animal in animals_available:
            if animal in input_text:
                play_sound(animal)
                return f"Le son de {animal} a été joué."
    return None  # Aucune réponse si la commande ne correspond pas
