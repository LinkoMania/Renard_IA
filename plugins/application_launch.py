import os

def start_application(application_name):
    if application_name.lower() == "brave":
        os.system("start brave")
        return "Brave Browser est lancé."
    elif application_name.lower() == "outlook":
        os.system("start outlook")
        return "Outlook est lancé."
    elif application_name.lower() == "rdp":
        os.system("start mstsc")
        return "Connexion Bureau à distance est lancée."
    elif application_name.lower() == "tor":
        os.system("start tor")
        return "Tor Browser est lancé."
    elif application_name.lower() == "paint":
        os.system("start mspaint")
        return "Paint est lancé."
    elif application_name.lower() == "screenshot":
        os.system("start snippingtool")
        return "L'outil de capture d'écran est lancé."
    elif application_name.lower() == "visual code":
        os.system("start code")
        return "Visual Studio Code est lancé."
    else:
        return f"L'application {application_name} n'est pas reconnue."

def respond(user_input):
    if "renard démarre le logiciel" in user_input:
        words = user_input.split()
        application_name = " ".join(words[4:])
        return start_application(application_name)
    else:
        return None

# Tester le plugin
if __name__ == "__main__":
    user_input = input("Dites quelque chose... ")
    response = respond(user_input)
    if response:
        print("Plugin: application_launch ->", response)
    else:
        print("Impossible de comprendre l'audio")
