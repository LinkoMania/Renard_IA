import os

def execute_script(script_name):
    script_path = os.path.join(os.path.dirname(__file__), "domotic_lamp", script_name)
    os.system(f"python {script_path}")

def respond(user_input):
    if "éteins la lampe" in user_input:
        execute_script("lampe_off_renard.py")
        return "Tout de suite monsieur."
    elif "allume la lampe" in user_input:
        execute_script("lampe_on_renard.py")
        return "Tout de suite monsieur."
    elif "mets la lampe en bleu" in user_input:
        execute_script("lampe_blue_renard.py")
        return "Tout de suite monsieur."
    elif "mets la lampe en rouge" in user_input:
        execute_script("lampe_red_renard.py")
        return "Tout de suite monsieur."
    elif "mets la lampe en verre" in user_input:
        execute_script("lampe_green_renard.py")
        return "Tout de suite monsieur."
    elif "mets la lampe en blanc" in user_input:
        execute_script("lampe_white_renard.py")
        return "Tout de suite monsieur."
    else:
        return None

# Tester le plugin
if __name__ == "__main__":
    user_input = input("Dites quelque chose... ")
    response = respond(user_input)
    if response:
        print("Plugin: lampe ->", response)
    else:
        print("Impossible de comprendre l'audio")
