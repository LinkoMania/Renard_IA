import os
import speech_recognition as sr
import pyttsx3
import subprocess
import psutil
import ollama
class Chatbot():
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Réglage de la vitesse de la synthèse vocale
        self.engine.setProperty('volume', 1)  # Réglage du volume de la synthèse vocale
        self.prompt = str()
        self.dialogue_activated = False  # Booléen pour suivre si l'annonce vocale a déjà été faite
    
    def listen(self):
        recognizer = sr.Recognizer()
        microphone_index = 1  # Index du microphone à utiliser
        with sr.Microphone(device_index=microphone_index) as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Dites quelque chose...")
            if not self.dialogue_activated:
                self.speak("Monsieur le système dialogue est activé")  # Annonce vocale de l'activation
                self.dialogue_activated = True
            audio = recognizer.listen(source)

        try:
            prompt = recognizer.recognize_google(audio, language='fr-FR')  # Reconnaissance vocale en français
            print("Texte reconnu:", prompt)  # Affichage du texte reconnu
            return prompt
        except sr.UnknownValueError:
            return ""
    
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
        print(text)  # Affichage du texte

    def check_ollama_server(self):
        for proc in psutil.process_iter():
            if "ollama" in proc.name():
                return True
        return False

    def start_ollama_server(self):
        subprocess.Popen(["ollama", "serve"], shell=True)

    def run_chatbot(self):
        ollama_server_running = self.check_ollama_server()
        if not ollama_server_running:
            self.speak("Le serveur Ollama n'est pas en cours d'exécution. Démarrage du serveur.")
            self.start_ollama_server()

        while True:
            self.prompt = self.listen()
            if self.prompt:
                if "renard passe en mode assistant" in self.prompt:
                    self.speak("Fermeture du système de dialogue.")
                    main_py_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main.py'))
                    subprocess.run(["python", main_py_path])
                    break  # Sortir de la boucle après avoir lancé main.py
                else:
                    stream = ollama.chat(
                        model='phi3:mini',
                        messages=[{'role': 'user', 'content': self.prompt}],
                        stream=True,
                    )
                    response = ""
                    for chunk in stream:
                        response += chunk['message']['content']
                    print(response)
                    self.speak(response)
                    self.engine.setProperty('rate', 150)  # Rétablir la vitesse par défaut après la synthèse vocale
                    self.engine.setProperty('volume', 1)  # Rétablir le volume par défaut après la synthèse vocale

def main():
    Chatbot().run_chatbot()

if __name__ == '__main__':
    main()
