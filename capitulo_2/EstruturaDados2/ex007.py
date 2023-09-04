import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Berlin looks like a nice city")

for token in doc:
    # Verifica se o token atual é um substantivo próprio.
    if token.pos_ == "PROPN":
        # Verifica se o próximo token é um verbo
        if (doc[token.i + 1].pos_ == "VERB") & (token.i + 1 < len(doc)) :
            print("Found proper noun before a verb:", token.text)