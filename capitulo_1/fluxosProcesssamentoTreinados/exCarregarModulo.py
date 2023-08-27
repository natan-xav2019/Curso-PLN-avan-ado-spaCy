import spacy

nlp = spacy.load("pt_core_news_sm")
# Faça antes o download do fluxo com o comando: python -m spacy download pt_core_news_sm
text = "É oficial: a Apple é a primeira empresa dos Estados Unidos a ter o valor de mercado acima de 1 trilhão."

doc = nlp(text)

print(doc.text)
