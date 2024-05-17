import os
import sys

def change_mode(new_mode):
    config_file = os.path.join(os.path.dirname(__file__), "..", "config.txt")  # Chemin vers le fichier config.txt
    lines = []
    with open(config_file, "r") as file:
        for line in file:
            key, value = line.strip().split(":")
            if key.strip() == "mode":
                value = new_mode
            lines.append(f"{key.strip()}: {value.strip()}\n")
    with open(config_file, "w") as file:
        file.writelines(lines)

def respond(command):
    if "vocal" in command.lower():
        change_mode("v")
        print("Mode changé en vocal.")
        os.execv(sys.executable, [sys.executable] + sys.argv)
    elif "texte" in command.lower():
        change_mode("t")
        print("Mode changé en texte.")
        os.execv(sys.executable, [sys.executable] + sys.argv)
