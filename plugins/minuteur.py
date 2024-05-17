# minuteur.py

import time
import threading
import winsound

class Timer:
    def __init__(self, duration):
        self.duration = duration

    def start(self):
        print(f"Minuteur démarré pour {self.duration} secondes.")
        threading.Timer(self.duration, self.timeout).start()

    def timeout(self):
        print("Le minuteur a expiré !")
        winsound.Beep(1000, 1000)  # Émet un son pendant 1 seconde

def respond(input_text):
    if "renard mets le chrono à" in input_text.lower():
        try:
            duration_str = input_text.lower().split("renard mets le chrono à")[-1].strip()
            duration = parse_duration(duration_str)
            if duration:
                timer = Timer(duration)
                timer.start()
                return f"Minuteur réglé sur {duration} secondes."
            else:
                return "Désolé, je n'ai pas compris la durée spécifiée."
        except ValueError:
            return "Désolé, je n'ai pas compris la durée spécifiée."
    else:
        return None

def parse_duration(duration_str):
    # Convertit la durée de la forme "x heures y minutes z secondes" en secondes
    tokens = duration_str.split()
    total_seconds = 0
    for i in range(0, len(tokens), 2):
        value = int(tokens[i])
        unit = tokens[i + 1]
        if unit.startswith("heur"):
            total_seconds += value * 3600
        elif unit.startswith("minute"):
            total_seconds += value * 60
        elif unit.startswith("seconde"):
            total_seconds += value
        else:
            raise ValueError("Unité de temps invalide.")
    return total_seconds

if __name__ == "__main__":
    duration_str = input("Entrez la durée du minuteur (par exemple, '2 heures 30 minutes 10 secondes') : ")
    duration = parse_duration(duration_str)
    if duration:
        timer = Timer(duration)
        timer.start()
    else:
        print("Désolé, la durée spécifiée est invalide.")
