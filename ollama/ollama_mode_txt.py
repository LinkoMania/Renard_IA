import ollama
import os

class Chatbot():
    def __init__(self):
        self.prompt = str()
    
    def run_chatbot(self):
        while True:
            self.prompt = input("\n\nLinko: ")
            if self.prompt.lower() == "renard retourne en mode assistant":
                print("Fermeture du chatbot...")
                break
            stream = ollama.chat(
                model='phi3:mini',
                messages=[{'role': 'user', 'content': self.prompt}],
                stream=True,
            )
            for chunk in stream:
                print(chunk['message']['content'], end='', flush=True)
        # Une fois que la commande est détectée, exécuter main.py
        os.system('python main.py')

def main():
    print(r'''
      ____                          _ 
     |  _ \ ___ _ __   __ _ _ __ __| |
     | |_) / _ \ '_ \ / _` | '__/ _` |
     |  _ <  __/ | | | (_| | | | (_| |
     |_| \_\___|_| |_|\__,_|_|  \__,_|
                                      
    Created by Kersteens Colin alias , binary fox and Linko Labs
    url : https://linko-creation.fr/ 
    personal use accepted and prohibited sale of my creation
    ''')

    # Lancer le chatbot après avoir affiché la bannière
    Chatbot().run_chatbot()

if __name__ == '__main__':
    main()
