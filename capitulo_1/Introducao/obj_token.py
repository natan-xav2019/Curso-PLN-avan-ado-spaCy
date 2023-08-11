import spacy

nlp = spacy.blank("en")

doc = nlp("Hello world!")

# Indexar o doc para obter um Token
token = doc[1]

# Obter o texto do token através do atributo .text
print(token.text)