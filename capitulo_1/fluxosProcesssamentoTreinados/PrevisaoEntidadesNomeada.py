import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("Apple is looking at buyinh U.K. startup for $1 bilion")

for ent in doc.ents:
    print(ent.text,  ent.label_)