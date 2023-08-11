# Parte 3: Espanhol
# Utilize spacy.blank para criar um objeto nlp vazio do idioma espanhol (“es”).
# Crie uma variável doc e imprima o seu conteúdo.

# Importe a biblioteca spaCy
import spacy

# Crie um objeto nlp do Espanhol
nlp = spacy.blank("es")

# Processar o texto em espanhol (equivalente ao português: "Como vai?")
doc = nlp("¿Cómo estás?")

# Imprimir o texto do documento
print(doc.text)