# Criar um objeto nlp
import spacy
nlp = spacy.blank("en")

# Importar a classe Doc 
from spacy.tokens import Doc

# As palavras e espaços em branco necessários para criar um doc:
words = ["Hello", "world", "!"]
spaces = [True, False, False]

# Criar um doc manualmente
doc = Doc(nlp.vocab, words=words, spaces=spaces)

print(doc)