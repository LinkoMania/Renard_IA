import requests

def get_weather_info(city):
    if city.lower() in ["belgique", "poupehan"]:
        url = "https://wttr.in/?format=%t%20%C"
    elif city.lower() in ["france", "paris"]:
        url = "https://wttr.in/France/Paris?format=%t%20%C"
    else:
        return "Veuillez spécifier un emplacement valide (belgique, poupehan, france, paris)."

    response = requests.get(url)
    
    if response.status_code == 200:
        weather_data = response.text.split("%20")
        temperature = weather_data[0].replace("+", "") + ""
        condition = translate_weather(weather_data[1].replace("+", " ").capitalize())
        return f"Il fait {temperature} et le temps est {condition}"
    else:
        return "Impossible de récupérer les données météorologiques."

def translate_weather(weather):
    weather_translation = {
        "Clear": "Dégagé",
        "Partly cloudy": "Partiellement nuageux",
        "Cloudy": "Nuageux",
        # Ajouter d'autres traductions ici...
    }
    return weather_translation.get(weather, weather)

def respond(user_input):
    if "météo" in user_input.lower():
        return get_weather_info("belgique")
    else:
        return None  # Retourne None si la demande ne concerne pas la météo

# Test du plugin météo_alternative

