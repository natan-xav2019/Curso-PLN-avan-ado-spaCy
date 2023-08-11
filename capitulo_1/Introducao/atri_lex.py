import spacy

nlp = spacy.blank("en")

doc = nlp("It costs $5.")

print("Index:   ",[token.i for token in doc])
print("Text:   ",[token.text for token in doc])

print("is_alpha:   ",[token.is_alpha for token in doc])
print("is_punct:   ",[token.is_punct for token in doc])
print("like_num:   ",[token.like_num for token in doc])

# is_alpha, is_punct e like_num retornam valores boleanos (verdadeiro ou falso)
# indicando respectivamente se o token tem caracteres alfabéticos, se é uma 
# pontuação ou se assemelha-se a um número, por exemplo, o token "10" – um, 
# zero – ou a palavra "dez" – D,E,Z.