Renard - Assistant Virtuel Personnel
Description du Projet
Renard est un assistant virtuel personnel conçu pour interagir avec vous dans des dialogues simples et effectuer diverses tâches telles que le lancement du navigateur, la recherche sur Internet, la lecture de musique, etc. L'idée de Renard est née de la nécessité de remplacer des logiciels obsolètes et vulnérables à diverses cyberattaques, tels que Sarah V3. Ce projet s'inspire également du travail réalisé par d'autres développeurs, notamment le projet "Loqui" de @nixiz0, qui a introduit l'idée d'inclure la vision et le modèle Ollama dans un nouvel ensemble de plugins pour créer un assistant virtuel capable de raisonnement presque humain.

L'objectif principal de Renard est d'offrir une plateforme d'apprentissage conviviale pour ceux qui souhaitent apprendre Python tout en développant des compétences en programmation et en sécurité informatique. Le projet est entièrement codé en Python, ce qui facilite la création de plugins personnalisés pour étendre les fonctionnalités de l'assistant.

Il est important de souligner que Renard est destiné uniquement à un usage personnel et éducatif, et ne doit jamais être utilisé à des fins commerciales ou illégales.

Installation des Dépendances
Pour installer les dépendances nécessaires à l'utilisation de Renard sous Windows 11, exécutez la commande suivante :

Copier le code
pip install pyaudio pygame pyautogui google SpeechRecognition==3.8.1 pyttsx3==2.90 translate==3.5.0 nltk==3.6.3 requests==2.26.0 selenium==4.1.0
Assurez-vous également que le dossier de voix Windows est configuré comme suit :

shell
Copier le code
%windir%\SysWOW64\speech\SpeechUX\sapi.cpl
Configuration Requise
Avec Plugin Ollama (IA)
Processeur: Intel Core i5 4ème génération 3.5 GHz
Mémoire: 16 Go de RAM DDR3
Espace disque: environ 20 Go
Sans Plugin Ollama
Processeur: 2.0 GHz
Mémoire: 1 Go de RAM DDR3
Espace disque: environ 1 Go
Versions Disponibles
Renard V-0.1
Changements Récents:
Création du fichier de configuration.
Mise en place du système de déclenchement d'actions par mots-clés dans le texte.
Intégration du mode vocal pour effectuer des actions.
Développement du système de chargement de plugins.
Création de 29 plugins de gestion différents.
Renard V-0.2
Nouveautés:
Sauvegarde des interactions et des résultats.
Ajout d'un message vocal et textuel lors du chargement de l'assistant.
Mode serveur: utilisation via des requêtes HTTP pour une utilisation externe.
Mode Discord: connexion de l'assistant à Discord pour dialoguer avec les utilisateurs (multi-room vocal et textuel).
Amélioration du design de l'interface.
Installation automatique des dépendances requises.
Développement du plugin Ollama pour dialoguer avec Renard en langage naturel (personnalisé phi3:mini).
Ajout du plugin Ollama_Vision pour l'analyse d'images capturées à l'écran.
Optimisation de l'écoute du bot pour ne se déclencher que sur détection du mot "renard".