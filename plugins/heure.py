import datetime

def respond(input_text):
    # Phrases déclencheuses pour demander l'heure
    time_triggers = ["renard donne-moi l'heure", "renard donne moi l'heure", "renard il est quelle heure"]

    # Phrases déclencheuses pour demander la date
    date_triggers = ["renard quelle est la date"]

    # Récupérer l'heure actuelle au format HH:MM:SS
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    # Récupérer la date actuelle au format AAAA-MM-JJ
    current_date = datetime.date.today()

    # Vérifier si la demande concerne l'heure
    if any(trigger in input_text.lower() for trigger in time_triggers):
        return f"L'heure actuelle est {current_time}"

    # Vérifier si la demande concerne la date
    elif any(trigger in input_text.lower() for trigger in date_triggers):
        return f"La date actuelle est {current_date}"

    # Si la demande ne correspond à aucune des phrases déclencheuses connues
    else:
        return None  # Aucune réponse


