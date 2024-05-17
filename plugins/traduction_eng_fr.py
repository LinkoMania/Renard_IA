from translate import Translator

def translate_text(text_to_translate, src_lang, dest_lang):
    translator = Translator(from_lang=src_lang, to_lang=dest_lang)
    translation = translator.translate(text_to_translate)
    return translation

def respond(user_input):
    if "renard traduit" in user_input:
        if "en anglais" in user_input:
            text_to_translate = user_input.replace("renard traduit en anglais", "").strip()
            return translate_text(text_to_translate, src_lang="fr", dest_lang="en")
        elif "en français" in user_input:
            text_to_translate = user_input.replace("renard traduit en français", "").strip()
            return translate_text(text_to_translate, src_lang="en", dest_lang="fr")
        else:
            return "Je ne comprends pas votre demande de traduction."
    else:
        return None

# Tester le plugin
if __name__ == "__main__":
    user_input = input("Dites quelque chose... ")
    if user_input.strip():
        response = respond(user_input)
        if response:
            print("Plugin: traduction_eng_fr ->", response)
        else:
            print("Impossible de comprendre l'audio")
