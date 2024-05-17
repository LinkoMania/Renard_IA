# calculatrice.py

def respond(input_text):
    # Vérifie si la phrase contient une opération mathématique
    if "calcule" in input_text.lower():
        # Divise la phrase en mots
        words = input_text.lower().split()
        # Recherche les opérateurs mathématiques
        operators = ['+', '-', '*', '/']
        # Initialise les valeurs des nombres
        num1 = None
        num2 = None
        operator = None
        # Parcourt les mots pour trouver les nombres et l'opérateur
        for word in words:
            if word.isdigit():
                if num1 is None:
                    num1 = int(word)
                else:
                    num2 = int(word)
            elif word in operators:
                operator = word
        # Si les nombres et l'opérateur sont trouvés
        if num1 is not None and num2 is not None and operator is not None:
            # Effectue le calcul
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                # Vérifie si le deuxième nombre n'est pas zéro pour éviter la division par zéro
                if num2 != 0:
                    result = num1 / num2
                else:
                    return "Impossible de diviser par zéro !"
            else:
                return "Opérateur non reconnu !"
            return str(result)  # Retourne le résultat sous forme de chaîne de caractères
        else:
            return "Opération mathématique invalide !"
    else:
        return None  # Aucune réponse si la phrase ne contient pas d'opération mathématique
