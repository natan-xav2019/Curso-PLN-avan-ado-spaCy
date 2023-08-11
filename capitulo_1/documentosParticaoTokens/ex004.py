# Quando você chama o objeto nlp passando uma string como parâmetro, a spaCy faz a toquenização do texto e cria um objeto do tipo documento. Neste exercício, você vai aprender mais sobre o documento Doc, assim como os objetos Token e partição Span.

# Importar spacy e criar o objeto nlp do Português
import spacy
nlp = spacy.blank("pt")

# Processar o texto
doc = nlp("Eu gosto de gatos e cachorros.")

# Selecionar o primeiro token
first_token = doc[0]

# Imprimir o texto do primeito token
print(first_token.text)