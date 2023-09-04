import spacy

# Importar as classes Doc e Span
from spacy.tokens import Doc, Span

nlp = spacy.blank("en")

# As palavras e espaços em branco necessários para criar o doc
words = ["Hello", "world", "!"]
spaces = [True, False, False]

# Criar um doc manualmente 
doc = Doc(nlp.vocab, words=words, spaces=spaces)

# Criar uma particção span manualmente
span = Span(doc, 0, 2)

# Criar uma partição span com um marcador
span_with_label = Span(doc, 0, 2, label="GREETING")

# Adicionar a partição a doc.ents
doc.ents = [span_with_label]

print(f"words: {words}\nspaces: {spaces}\ndoc: {doc}\nspan: {span}\nspan_with_label: {span_with_label}\nents: {doc.ents}.")