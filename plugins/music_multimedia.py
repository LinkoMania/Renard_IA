import os

def launch_rock_music():
    os.system("start wmplayer.exe /playlist rock")

def pause_music():
    os.system("nircmd.exe mutesysvolume 1")

def play_music():
    os.system("nircmd.exe mutesysvolume 0")

def next_track():
    os.system("nircmd.exe sendkeypress ctrl+n")

def previous_track():
    os.system("nircmd.exe sendkeypress ctrl+b")

def increase_volume():
    os.system("nircmd.exe changesysvolume 2000")

def decrease_volume():
    os.system("nircmd.exe changesysvolume -2000")

def respond(user_input):
    if "renard musique" in user_input:
        if "rock" in user_input:
            launch_rock_music()
            return "La musique rock est lancée."
        elif "pause" in user_input:
            pause_music()
            return "La musique est en pause."
        elif "play" in user_input:
            play_music()
            return "La musique est en lecture."
        elif "change de musique" in user_input:
            next_track()
            return "Musique suivante."
        elif "musique précédente" in user_input:
            previous_track()
            return "Musique précédente."
        elif "augmente le volume" in user_input:
            increase_volume()
            return "Le volume est augmenté."
        elif "diminue le volume" in user_input:
            decrease_volume()
            return "Le volume est diminué."
        else:
            return "Je ne comprends pas votre demande concernant la musique."
    else:
        return None

# Tester le plugin
if __name__ == "__main__":
    user_input = input("Dites quelque chose... ")
    if user_input.strip():
        response = respond(user_input)
        if response:
            print("Plugin: music_multimedia ->", response)
        else:
            print("Impossible de comprendre l'audio")
