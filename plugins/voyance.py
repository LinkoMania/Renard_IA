import random

def get_horoscope_prediction():
    # Liste de prédictions pour l'horoscope
    predictions = [
        "Aujourd'hui, vous pourriez recevoir une bonne nouvelle qui apportera de la joie à votre vie amoureuse.",
        "Il est possible que vous rencontriez quelqu'un de spécial aujourd'hui. Gardez un esprit ouvert.",
        "Votre relation amoureuse pourrait prendre un tournant positif aujourd'hui. Restez optimiste.",
        "Il est temps de laisser le passé derrière vous et d'embrasser les nouvelles opportunités en amour.",
        "Vous pourriez recevoir une invitation inattendue qui vous conduira vers de nouvelles rencontres amoureuses.",
        "La communication sera la clé de votre succès amoureux aujourd'hui. Exprimez-vous librement."
    ]
    # Sélection aléatoire d'une prédiction
    return random.choice(predictions)

def get_horoscope_for_lion():
    # Prédiction aléatoire pour l'horoscope
    prediction = get_horoscope_prediction()
    # Obtention des informations astrologiques pour le Lion
    return f"Horoscope du Lion : {prediction}"

def respond(user_input):
    # Phrases prédéfinies pour demander l'horoscope
    horoscope_phrases = ["mon horoscope", "l'horoscope", "horoscope du lion"]
    
    # Vérifie si la demande concerne spécifiquement l'horoscope pour le Lion
    if any(phrase in user_input.lower() for phrase in horoscope_phrases):
        return get_horoscope_for_lion()
    else:
        return None

# Tester le plugin
if __name__ == "__main__":
    print(respond("Donne-moi l'horoscope"))
