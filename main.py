import os
import sys
import speech_recognition as sr
import pyttsx3
import pyaudio
import importlib.util
from colorama import Fore, Style
import subprocess

# Fonction pour effacer la console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fonction pour centrer le texte dans la console
def center_text(text):
    term_width = os.get_terminal_size().columns
    return text.center(term_width)

# Bannière
banner = center_text(r'''
  ____                          _ 
 |  _ \ ___ _ __   __ _ _ __ __| |
 | |_) / _ \ '_ \ / _` | '__/ _` |
 |  _ <  __/ | | | (_| | | | (_| |
 |_| \_\___|_| |_|\__,_|_|  \__,_|
                                  
Created by Kersteens Colin alias , binary fox and Linko Labs
url : https://linko-creation.fr/ 
personal use accepted and prohibited sale of my creation
''')

# Affichage de la bannière
print(banner)

# Emplacement du fichier de configuration
CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.txt")

# Chargement des plugins
plugins_dir = os.path.join(os.path.dirname(__file__), 'plugins')
sys.path.append(plugins_dir)
plugins_loaded = []

for filename in os.listdir(plugins_dir):
    if filename.endswith(".py") and filename != "__init__.py":
        plugin_name = os.path.splitext(filename)[0]
        spec = importlib.util.spec_from_file_location(plugin_name, os.path.join(plugins_dir, filename))
        plugin_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plugin_module)
        globals()[plugin_name] = plugin_module
        plugins_loaded.append(plugin_name)

# Fonction pour lire les configurations depuis le fichier
def read_config():
    config = {}
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            for line in file:
                key, value = line.strip().split(":")
                config[key.strip()] = value.strip()
    return config

# Fonction pour écrire les configurations dans le fichier
def write_config(config):
    with open(CONFIG_FILE, "w") as file:
        for key, value in config.items():
            if key in ["voice", "microphone", "user_name", "mode"]:
                file.write(f"{key}: {value}\n")

# Vérifier les dépendances des plugins
def check_dependencies(plugin_name):
    try:
        importlib.import_module(plugin_name)
    except ModuleNotFoundError:
        print(f"Dépendances manquantes pour le plugin {plugin_name}. Installation en cours...")
        try:
            os.system(f'pip install -r {os.path.join(plugins_dir, plugin_name, "requirements.txt")}')
        except:
            print(f"L'installation automatique des dépendances pour le plugin {plugin_name} a échoué. Veuillez installer manuellement les packages nécessaires.")
            sys.exit(1)

# Vérifier toutes les dépendances des plugins
def check_all_dependencies():
    for plugin_name in plugins_loaded:
        check_dependencies(plugin_name)

# Sélectionner la voix à utiliser
def select_voice():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    print(Fore.CYAN + "Voix disponibles :")
    for i, voice in enumerate(voices):
        print(f"{i}: {voice.name}")
    selected_index = int(input("Entrez le numéro de la voix à utiliser : "))
    return voices[selected_index]

# Sélectionner le microphone à utiliser
def select_microphone():
    print(Fore.CYAN + "Microphones disponibles :")
    audio = pyaudio.PyAudio()
    for i in range(audio.get_device_count()):
        device_info = audio.get_device_info_by_index(i)
        print(f"{i}: {device_info['name']}")
    selected_index = int(input("Entrez le numéro du microphone à utiliser : "))
    return selected_index

# Reconnaissance vocale
def listen(selected_index):
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=selected_index) as source:
        print(Fore.YELLOW + "Dites quelque chose...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language='fr-FR')
        print(Fore.GREEN + "Vous avez dit:", text)
        return text
    except sr.UnknownValueError:
        print(Fore.RED + "Impossible de comprendre l'audio")
        return ""
    except sr.RequestError as e:
        print(Fore.RED + "Erreur lors de la requête :", str(e))
        return ""

# Synthèse vocale
def speak(text, selected_voice):
    engine = pyttsx3.init()
    engine.setProperty('voice', selected_voice.id)
    engine.say(text)
    engine.runAndWait()

# Fonction principale
def main():
    clear_console()  # Nettoyer la console au démarrage
    check_all_dependencies()
    print(Fore.YELLOW + banner)
    
    # Lecture des configurations existantes
    config = read_config()
    
    # Vérification et enregistrement du prénom de l'utilisateur dans la configuration
    if 'user_name' not in config:
        user_name = input("Entrez votre prénom : ")
        config['user_name'] = user_name
    
    # Vérification des paramètres vocaux et de microphone dans la configuration
    if 'voice' not in config:
        selected_voice = select_voice()
        config['voice'] = selected_voice.id
    else:
        voices = pyttsx3.init().getProperty('voices')
        selected_voice = [v for v in voices if v.id == config['voice']][0]
    
    if 'microphone' not in config:
        selected_index = select_microphone()
        config['microphone'] = selected_index
    else:
        selected_index = int(config['microphone'])
    
    # Vérification du mode de discussion dans la configuration
    if 'mode' not in config:
        mode = select_mode()  # Variable qui contient le choix du mode de l'utilisateur
        config['mode'] = mode
    else:
        mode = config['mode']
    
    # Enregistrement des configurations
    write_config(config)
    
    # Affichage des plugins chargés
    num_plugins = len(plugins_loaded)
    print(Fore.YELLOW + f"{num_plugins} plugins chargés.")

    # Si le mode est vocal, annoncer l'initialisation du mode assistant et activer le mode assistant
    if mode.lower() == "v":
        speak("Initialisation du mode assistant.", selected_voice)
        speak("Pour activer le mode assistant, dites 'renard passe en mode assistant' pour le mode dialogue dite 'renard passe en mode dialogue'.", selected_voice)

    if mode.lower() == "v":
        print(Fore.GREEN + "Le mode ollama vocal n'est pas activé.")
    elif mode.lower() == "t":
        print(Fore.GREEN + "Le mode ollama texte n'est pas activé.")
    
    while True:
        # Gestion des commandes utilisateur et des plugins
        if mode.lower() == "v":
            user_input = listen(selected_index)
            if user_input:
                # Vérification si le mot "renard" est présent parmi les trois premiers mots de la phrase
                first_three_words = user_input.split()[:3]
                if "renard" not in first_three_words:
                    print(Fore.RED + "Le mot 'renard' n'est pas présent parmi les trois premiers mots. Arrêt de l'écoute.")
                    continue  # Revenir au début de la boucle pour attendre une nouvelle entrée
        else:
            user_input = input(Fore.CYAN + "Entrez votre texte : ")
        
        # Activation du mode ollama si la commande spécifique est détectée
        if user_input.lower() == "renard passe en mode dialogue":
            mode = "v"  # Mode vocal pour le mode dialogue
            config['mode'] = mode
            write_config(config)
            subprocess.Popen(["python", os.path.join("ollama", "ollama_mode_voc.py")])  # Lancer le script ollama
            print(Fore.GREEN + "Le mode dialogue a été activé.")
            break
        
        # Activation du mode assistant si la commande spécifique est détectée
        if user_input.lower() == "renard passe en mode assistant":
            mode = "t"  # Mode texte pour le mode assistant
            config['mode'] = mode
            write_config(config)
            subprocess.Popen(["python", "main.py"])  # Relancer main.py
            print(Fore.GREEN + "Le mode assistant a été activé.")
            break
        
        # Exécution des plugins
        for plugin_name in plugins_loaded:
            if hasattr(globals()[plugin_name], "respond"):
                response = getattr(globals()[plugin_name], "respond")(user_input)
                if response:
                    print(Fore.MAGENTA + f"Plugin: {plugin_name} ->", end=" ")
                    print(Style.RESET_ALL + f"{response}")
                    speak(response, selected_voice) if mode.lower() == "v" else None
                    break

if __name__ == "__main__":
    main()
