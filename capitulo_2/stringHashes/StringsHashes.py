import spacy

nlp = spacy.blank("en")

nlp.vocab.strings.add("coffee")

lexeme = nlp.vocab["coffee"]

coffee_hash = nlp.vocab.strings["coffee"]
coffee_string = nlp.vocab.strings[coffee_hash]

print(f'hash: {coffee_hash}')
print(f'palavra: {coffee_string}')

# Imprimir os atributos léxicos
print(f'text: {lexeme.text}, orth: {lexeme.orth}, is_alpha: {lexeme.is_alpha}')