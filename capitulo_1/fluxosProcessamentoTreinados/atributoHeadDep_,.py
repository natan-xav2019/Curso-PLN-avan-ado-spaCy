import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("She ate the pizza")

for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)

# O atributo .head retorna o índice do token principal. Você pode pensar nele como o "pai" ao qual a palavra está conectada.
# O atributo .dep_ retorna o marcador de dependência (ou termo sintático) previsto.