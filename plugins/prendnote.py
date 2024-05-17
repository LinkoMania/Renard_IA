# prendnote.py

import os

def respond(input_text):
    normalized_text = input_text.lower()
    if "prend notes" in normalized_text or "écris" in normalized_text or "renard prend note" in normalized_text:
        note_content = normalized_text.split("prend note")[-1].strip()
        save_note(note_content)
        return "Note enregistrée avec succès !"
    elif "donne moi le nombre de note" in normalized_text or "donne-moi le nombre de notes" in normalized_text:
        return f"Nombre de notes enregistrées : {count_notes()}"
    elif "lis moi la note" in normalized_text:
        note_number = extract_note_number(normalized_text)
        return read_note(note_number)
    elif "efface la note" in normalized_text:
        note_number = extract_note_number(normalized_text)
        delete_note(note_number)
        return f"Note {note_number} effacée avec succès !"
    else:
        return None

def save_note(note_content):
    notes_directory = "plugins/notes"
    os.makedirs(notes_directory, exist_ok=True)
    note_files = [f for f in os.listdir(notes_directory) if f.startswith("note_")]
    next_note_number = len(note_files) + 1
    with open(os.path.join(notes_directory, f"note_{next_note_number:03}.txt"), "w") as note_file:
        note_file.write(note_content)

def count_notes():
    notes_directory = "plugins/notes"
    os.makedirs(notes_directory, exist_ok=True)
    note_files = [f for f in os.listdir(notes_directory) if f.startswith("note_")]
    return len(note_files)

def extract_note_number(input_text):
    try:
        return int(input_text.split("lis moi la note")[-1].strip())
    except ValueError:
        return None

def read_note(note_number):
    notes_directory = "plugins/notes"
    os.makedirs(notes_directory, exist_ok=True)
    try:
        with open(os.path.join(notes_directory, f"note_{note_number:03}.txt"), "r") as note_file:
            return note_file.read()
    except FileNotFoundError:
        return f"La note {note_number} n'existe pas."

def delete_note(note_number):
    notes_directory = "plugins/notes"
    os.makedirs(notes_directory, exist_ok=True)
    try:
        os.remove(os.path.join(notes_directory, f"note_{note_number:03}.txt"))
    except FileNotFoundError:
        pass
