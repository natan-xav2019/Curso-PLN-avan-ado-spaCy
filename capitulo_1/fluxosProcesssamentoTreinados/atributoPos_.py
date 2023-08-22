import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("She ate the pizza")

for token in doc:
    print(token.text, token.pos_)

# Para cada token no doc, podemos imprimir o texto e o atributo .pos_, que é a classe gramatical prevista.