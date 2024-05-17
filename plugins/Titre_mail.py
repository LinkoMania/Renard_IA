import imaplib
import email
from email.header import decode_header

def fetch_emails_info(username, password, server, limit=3):
    try:
        # Connexion au serveur IMAP
        mail = imaplib.IMAP4_SSL(server)
        mail.login(username, password)
        mail.select("inbox")  # Sélection de la boîte de réception

        # Recherche des derniers e-mails
        result, data = mail.search(None, "ALL")
        ids = data[0].split()
        latest_emails_ids = ids[-limit:]  # Sélection des derniers e-mails

        # Récupération des informations des e-mails
        emails_info = []
        for email_id in latest_emails_ids:
            result, data = mail.fetch(email_id, "(RFC822)")
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)
            sender = decode_header(msg["From"])[0][0]
            if isinstance(sender, bytes):
                # Décodage si nécessaire
                sender = sender.decode()
            if "<" in sender:
                sender = sender.split("<")[0].strip()  # Supprimer l'adresse e-mail
            emails_info.append(sender)

        # Fermeture de la connexion
        mail.logout()

        return emails_info
    except Exception as e:
        return str(e)

def test_email_connection(username, password, server):
    try:
        # Connexion au serveur IMAP
        mail = imaplib.IMAP4_SSL(server)
        mail.login(username, password)
        mail.logout()

        return "La connexion aux e-mails a réussi."
    except Exception as e:
        return "Échec de la connexion aux e-mails : " + str(e)

def respond(user_input):
    if "renard test la connexion aux e-mails" in user_input:
        # Paramètres pour Gmail
        username = 'linkocreation@gmail.com'
        password = 'stkmffnekfvutwox'
        server = 'imap.gmail.com'

        # Test de la connexion
        return test_email_connection(username, password, server)
    elif "renard lis mes 3 derniers emails" in user_input:
        # Paramètres pour Gmail
        username = 'linkocreation@gmail.com'
        password = 'stkmffnekfvutwox'
        server = 'imap.gmail.com'

        # Récupération des informations des e-mails
        return fetch_emails_info(username, password, server)
    else:
        return None

# Tester le plugin
if __name__ == "__main__":
    user_input = input("Dites quelque chose... ")
    response = respond(user_input)
    if response:
        if isinstance(response, list):
            clean_senders = [sender.split("@")[0] if "@" in sender else sender for sender in response]
            print("Plugin: Titre_mail -> Vous avez des e-mails de", ", ".join(clean_senders))
        else:
            print("Plugin: Titre_mail ->", response)
    else:
        print("Impossible de comprendre l'audio")
