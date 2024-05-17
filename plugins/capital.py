# Plugin capital

capitals = {
    "france": "Paris",
    "belgique": "Bruxelles",
    "allemagne": "Berlin",
    "italie": "Rome",
    "espagne": "Madrid",
    "portugal": "Lisbonne",
    "pays-bas": "Amsterdam",
    "royaume-uni": "Londres",
    "suisse": "Berne",
    "suède": "Stockholm",
    "norvège": "Oslo",
    "danemark": "Copenhague",
    "finlande": "Helsinki",
    "autriche": "Vienne",
    "grèce": "Athènes",
    "turquie": "Ankara",
    "russie": "Moscou",
    "canada": "Ottawa",
    "états-unis": "Washington D.C.",
    "mexique": "Mexico",
    "brésil": "Brasilia",
    "argentine": "Buenos Aires",
    "australie": "Canberra",
    # Ajouter d'autres pays et capitales au besoin
}

def respond(user_input):
    if "capitale de" in user_input:
        country = user_input.split("capitale de")[1].strip().lower()
        capital = capitals.get(country, None)
        if capital:
            return f"La capitale de {country.capitalize()} est {capital}."
        else:
            return f"Je ne connais pas la capitale de {country.capitalize()}."
    else:
        return None
