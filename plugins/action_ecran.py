import ctypes

# Constantes pour identifier l'écran principal
HWND_BROADCAST = 0xFFFF
WM_SYSCOMMAND = 0x0112
SC_MONITORPOWER = 0xF170
MONITOR_OFF = 2
MONITOR_ON = -1

def turn_off_screen():
    # Éteindre l'écran principal
    ctypes.windll.user32.SendMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, MONITOR_OFF)

def turn_on_screen():
    # Allumer l'écran principal
    ctypes.windll.user32.SendMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, MONITOR_ON)

def respond(user_input):
    if "éteins l'écran" in user_input.lower() or "ferme l'écran" in user_input.lower():
        turn_off_screen()
        return "Écran éteint."
    elif "allume l'écran" in user_input.lower():
        turn_on_screen()
        return "Écran allumé."
    else:
        return None

# Tester le plugin
if __name__ == "__main__":
    print(respond("Renard éteins l'écran"))
    print(respond("Renard allume l'écran"))
