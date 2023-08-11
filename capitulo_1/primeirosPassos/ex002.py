# Parte 2: Alemão
# Utilize spacy.blank para criar um objeto nlp vazio do idioma alemão (“de”).
# Crie uma variável doc e imprima o seu conteúdo.

# Importe a biblioteca spaCy
import spacy

# Crie um objeto nlp do Alemão
nlp = spacy.blank("de")

# Processe o texto (equivalente ao português: "Atenciosamente")
doc = nlp("Liebe Grüße!")

# Imprima o texto do documento
print(doc.text)