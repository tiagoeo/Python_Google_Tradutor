from googletrans import Translator

trans = Translator()

texto_original = r"The book is on the table!"

google_translator = trans.translate(texto_original, dest="pt")

idioma_detectado = google_translator.src

texto_traducao = google_translator.text

print(f"No texto original: {texto_original}, foi detectado o idioma: {idioma_detectado}, e sua tradução em português é: {texto_traducao}")

