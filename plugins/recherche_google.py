# recherche_google.py

import webbrowser
from googlesearch import search

# Chemin vers l'exécutable Chrome sur Windows
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'

def respond(input_text):
    if "renard cherche sur google" in input_text.lower():
        query = input_text.split("renard cherche sur google")[-1].strip()
        results = list(search(query, num=5, stop=5))
        first_result = results[0]
        save_search_results(results)
        description = get_description(first_result)
        return f"J'ai trouvé quelques résultats pour '{query}'. Voici une description du premier résultat : {description}"
    elif "ouvre la recherche google" in input_text.lower():
        open_search_results()
        return "Ouverture du résultat de recherche Google dans Google Chrome."
    else:
        return None

def get_description(url):
    # Fonction pour obtenir la description de la page Web
    # Cela dépendra de la façon dont vous souhaitez extraire la description du site Web.
    # Pour l'instant, je vais simplement retourner l'URL.
    return url

def save_search_results(results):
    with open("plugins/recherche_google/search_results.txt", "w") as file:
        for result in results:
            file.write(result + "\n")

def open_search_results():
    with open("plugins/recherche_google/search_results.txt", "r") as file:
        first_link = file.readline().strip()
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open(first_link)

