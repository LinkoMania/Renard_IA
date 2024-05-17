# youtube_control.py

import os
import time
import webbrowser

def respond(input_text):
    if "renard va sur youtube et cherche" in input_text.lower():
        keyword = input_text.split("cherche")[-1].strip()
        open_youtube_and_search(keyword)
        return "J'ai ouvert YouTube et effectué la recherche."

    return None

def open_youtube_and_search(keyword):
    # Spécifier le chemin complet vers l'exécutable Chrome
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Chemin vers l'exécutable Chrome
    search_url = f"https://www.youtube.com/results?search_query={keyword}"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get("chrome").open_new(search_url)
    time.sleep(2)  # Attendre quelques secondes pour que la page se charge complètement

# Test rapide pour s'assurer que le plugin fonctionne correctement
if __name__ == "__main__":
    print(respond("Renard va sur YouTube et cherche Pikachu"))
