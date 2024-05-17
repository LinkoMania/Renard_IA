import subprocess

# Fonction pour éteindre l'écran
def turn_off_screen():
    # Spécifier le chemin d'accès complet vers cec-client avec des barres obliques inverses doubles
    subprocess.run(["C:\\Program Files (x86)\\Pulse-Eight\\USB-CEC Adapter\\cec-client.exe", "-s", "-d", "0", "standby"])

# Fonction pour répondre à l'utilisateur
def respond(user_input):
    if "coupe HDMI" in user_input:
        turn_off_screen()
        return "L'écran a été éteint."
    else:
        return None

# Tester le plugin
if __name__ == "__main__":
    user_input = input("Dites quelque chose... ")
    response = respond(user_input)
    if response:
        print("Plugin: éteindre écran ->", response)
    else:
        print("Impossible de comprendre l'audio")
