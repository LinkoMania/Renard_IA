import requests

def search_wikipedia(query):
    try:
        lang = 'fr'  # Définir la langue sur français
        url = f"https://{lang}.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "exintro": True,
            "explaintext": True,
            "titles": query
        }
        response = requests.get(url, params=params)
        data = response.json()
        page_id = next(iter(data['query']['pages'].keys()))
        summary = data['query']['pages'][page_id]['extract']
        return summary
    except Exception as e:
        print(e)
        return "Une erreur s'est produite lors de la recherche sur Wikipédia. Veuillez réessayer plus tard."

def respond(user_input):
    if "renard recherche sur Wikipédia" in user_input:
        query = user_input.replace("renard recherche sur Wikipédia", "").strip()
        return search_wikipedia(query)
    else:
        return None
