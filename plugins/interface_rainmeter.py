import ctypes
import os

# Chemin d'accès aux fichiers d'arrière-plan
BACKGROUND_RAINMETER = os.path.join(os.path.dirname(__file__), "C:/Users/Anonymous/Documents/ia/Renard_IA/background_rainmeter.png")
BACKGROUND_WINDOWS = os.path.join(os.path.dirname(__file__), "C:/Users/Anonymous/Documents/ia/Renard_IA/windows.jpg")

def set_wallpaper(image_path):
    # Définit le fond d'écran de Windows
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

def start_interface():
    # Démarrage de Rainmeter
    os.chdir(r"C:\Program Files\Rainmeter")
    os.system("start rainmeter.exe")
    # Changement du fond d'écran
    set_wallpaper(BACKGROUND_RAINMETER)
    print("Rainmeter démarré et fond d'écran changé.")

def close_interface():
    # Fermeture de Rainmeter
    os.system("taskkill /f /im rainmeter.exe")
    # Rétablissement du fond d'écran par défaut
    set_wallpaper(BACKGROUND_WINDOWS)
    print("Rainmeter fermé et fond d'écran rétabli.")

def respond(command):
    if "démarre ton interface" in command:
        start_interface()
    elif "ferme ton interface" in command:
        close_interface()
