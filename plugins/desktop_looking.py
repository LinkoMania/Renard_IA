import pyautogui

def show_desktop():
    # Minimiser toutes les fenêtres pour afficher le bureau
    pyautogui.hotkey('win', 'd')

def restore_windows():
    # Restaurer les fenêtres actives
    pyautogui.hotkey('win', 'shift', 'm')

def respond(user_input):
    if "affiche le bureau" in user_input.lower() or "montre le bureau" in user_input.lower():
        show_desktop()
        return "Bureau affiché."
    elif "remets les fenêtres" in user_input.lower() or "restaure les fenêtres" in user_input.lower():
        restore_windows()
        return "Fenêtres restaurées."
    else:
        return None

# Tester le plugin
if __name__ == "__main__":
    print(respond("Renard affiche le bureau"))
    print(respond("Renard remets les fenêtres"))
