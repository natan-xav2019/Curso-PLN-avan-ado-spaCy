import spacy

nlp = spacy.blank("en")

doc = nlp("Hello World!")

span = doc[1:3]

print(span.text)