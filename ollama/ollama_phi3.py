import os
import subprocess
import time
import ollama
import psutil
import speech_recognition as sr

class OllamaChatbot:
    def __init__(self, mode):
        self.mode = mode
    
    def run_chatbot(self):
        if self.mode == "v":
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                print("Dites quelque chose...")
                audio = recognizer.listen(source)
            try:
                user_input = recognizer.recognize_google(audio, language='fr-FR')
                print("Vous avez dit:", user_input)
                if "ferme ton dialogue" in user_input:
                    self.restart_main()
                elif "démarre le dialogue" in user_input:
                    self.start_ollama_server("start")
            except sr.UnknownValueError:
                print("Impossible de comprendre l'audio")
                return
            except sr.RequestError as e:
                print("Erreur lors de la requête :", str(e))
                return
        elif self.mode == "t":
            user_input = input("Votre commande:\n")
            if "ferme ton dialogue" in user_input:
                self.restart_main()
            elif "démarre le dialogue" in user_input:
                self.start_ollama_server("start")

    def check_ollama_server(self):
        for proc in psutil.process_iter(['pid', 'name']):
            if 'ollama' in proc.info['name']:
                return True
        return False

    def start_ollama_server(self, action):
        if not self.check_ollama_server():
            print("Ollama server is not running. Starting the server...")
            subprocess.Popen(["ollama", "serve"])
            # Give some time for the server to start
            time.sleep(5)
        if action == "start":
            self.chat_with_ollama()

    def restart_main(self):
        # Fermer l'assistant
        os.system("taskkill /f /im python.exe")
        # Redémarrer l'assistant
        subprocess.Popen(["python", "main.py"])

    def chat_with_ollama(self):
        stream = ollama.chat(
            model='phi3:mini',
            messages=[{'role': 'user', 'content': ''}],
            stream=True,
        )
        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)

def main():
    # Lecture du mode dans le fichier de configuration
    mode = read_config()["mode"]
    ollama_chatbot = OllamaChatbot(mode)
    ollama_chatbot.run_chatbot()

if __name__ == '__main__':
    main()
