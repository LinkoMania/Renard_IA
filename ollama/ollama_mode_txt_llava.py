import os
import cv2
import time
from PIL import ImageGrab  # Module pour prendre des captures d'écran

class Chatbot():
    def __init__(self):
        self.prompt = str()

    def process_image(self, image_path):
        # Utilise la CLI d'Ollama pour analyser l'image et générer une description
        command = f"ollama run llava:latest \"décris l'image en français en une phrase: {image_path}\""
        description = os.popen(command).read()
        # Retire les sauts de ligne et autres caractères spéciaux
        description = description.encode('latin1', 'ignore').decode('utf-8')
        # Supprime le texte indésirable
        description = description.replace("failed to get console mode for stdout: The handle is invalid.", "")
        return description.strip()  # Retire les espaces inutiles à la fin

    def take_screenshot(self, output_path):
        # Prend une capture d'écran et l'enregistre dans le chemin spécifié
        screenshot = ImageGrab.grab()
        screenshot.save(output_path)

    def take_webcam_photo(self, output_path):
        # Active la webcam et attend 2 secondes avant de prendre la photo
        webcam = cv2.VideoCapture(0)
        time.sleep(2)  # Attendre 2 secondes
        ret, frame = webcam.read()
        
        # Ajuster la luminosité de l'image capturée
        frame = cv2.convertScaleAbs(frame, alpha=1.5, beta=50)  # Ajuster les paramètres alpha et beta selon vos besoins

        cv2.imwrite(output_path, frame)
        webcam.release()

    def describe_webcam_photo(self, image_path):
        if os.path.exists(image_path):
            image_description = self.process_image(image_path)
            print(f"Description de la photo de la webcam : {image_description}")
        else:
            print("Aucune photo de la webcam n'a été sauvegardée.")

    def run_chatbot(self):
        images_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "images")) # Chemin absolu vers le dossier images
        
        while True:
            self.prompt = input("\n\nLinko: ")
            if self.prompt.lower() == "renard retourne en mode assistant":
                print("Fermeture du chatbot...")
                # Relancer le script main.py
                main_py_path = r"C:\Users\Anonymous\Documents\ia\Renard_IA\main.py"
                os.system(f"python {main_py_path}")
                break
            elif self.prompt.lower() == "sauvegarde l'image":
                output_path = os.path.join(images_dir, "latest_screenshot.png")
                self.take_screenshot(output_path)
                print(f"Image sauvegardée dans : {output_path}")
            elif self.prompt.lower() == "sauvegarde de la webcam":
                output_path = os.path.join(images_dir, "latest_webcam_photo.png")
                self.take_webcam_photo(output_path)
                print(f"Photo de la webcam sauvegardée dans : {output_path}")
            elif self.prompt.lower() == "renard décris moi l'image":
                image_path = os.path.join(images_dir, "latest_screenshot.png")
                self.describe_webcam_photo(image_path)
            elif self.prompt.lower() == "renard décris la photo de la webcam":
                image_path = os.path.join(images_dir, "latest_webcam_photo.png")
                self.describe_webcam_photo(image_path)
            else:
                print("Commande non reconnue.")

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
