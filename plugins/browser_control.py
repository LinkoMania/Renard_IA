import webbrowser
import os

def open_website_in_chrome(url):
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab(url)

def go_back():
    os.system("nircmd.exe sendkeypress alt+left")

def go_forward():
    os.system("nircmd.exe sendkeypress alt+right")

def refresh_page():
    os.system("nircmd.exe sendkeypress f5")

def close_browser():
    os.system("nircmd.exe sendkeypress alt+F4")

def minimize_window():
    os.system("nircmd.exe sendkeypress alt+space")
    os.system("nircmd.exe sendkeypress n")

def add_to_favorites():
    os.system("nircmd.exe sendkeypress ctrl+d")

def start_chrome():
    os.system("start chrome")

def scroll_down():
    os.system("nircmd.exe sendkeypress {DOWN}")

def scroll_up():
    os.system("nircmd.exe sendkeypress {UP}")

def respond(user_input):
    if "page suivante" in user_input:
        go_forward()
        return "Page suivante."
    elif "page précédente" in user_input:
        go_back()
        return "Page précédente."
    elif "rafraîchis la page" in user_input:
        refresh_page()
        return "La page est rafraîchie."
    elif "tape URL" in user_input:
        parts = user_input.split("site")[1].strip()
        open_website_in_chrome(parts)
        return f"Le site {parts} est ouvert dans Chrome."
    elif "ferme le navigateur Chrome" in user_input:
        close_browser()
        return "Le navigateur Chrome est fermé."
    elif "diminue la fenêtre du navigateur" in user_input:
        minimize_window()
        return "La fenêtre du navigateur est réduite."
    elif "ajoute la page au favoris" in user_input:
        add_to_favorites()
        return "La page est ajoutée aux favoris."
    elif "démarre chrome" in user_input:
        start_chrome()
        return "Chrome est démarré."
    elif "descend la page" in user_input:
        scroll_down()
        return "La page est descendue."
    elif "monte la page" in user_input:
        scroll_up()
        return "La page est montée."
    else:
        return None

# Tester le plugin
if __name__ == "__main__":
    user_input = input("Dites quelque chose... ")
    response = respond(user_input)
    if response:
        print("Plugin: browser_control ->", response)
    else:
        print("Impossible de comprendre l'audio")
