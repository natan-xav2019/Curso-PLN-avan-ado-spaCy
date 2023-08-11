import spacy

nlp = spacy.blank("en")

#Criando após processar um texto com objeto nlp
doc = nlp("Hello World!")

#Percorrendo os Tokensdo doc
for token in doc:
    print(token.text)