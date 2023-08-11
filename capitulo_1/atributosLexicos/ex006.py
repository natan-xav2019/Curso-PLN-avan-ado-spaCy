# Use o atributo like_num para identificar se algum token no documento doc se assemelha a um número.
# Selecione o token seguinte ao token atual no documento. O índice para o próximo token no doc é token.i + 1.
# Verifique se o atributo text do próximo token é o sinal de porcentagem ”%“.

import spacy

nlp = spacy.blank("pt")

# Processar o texto
doc = nlp(
    "Em 1990, mais de 60% da população da Ásia Oriental estava em situação de extrema pobreza."
    "Agora, menos de 4% está nessa situação."
)

# Iterar os tokens de um documento doc 
for token in doc:
    # Checar se o token é composto por algarismos numéricos
    if token.like_num:
        # Selecionar o próximo token do documento
        next_token = doc[token.i + 1]
        # Checar se o texto do proximo token é igual a "%"
        if next_token.text == "%":
            print("Percentuais encontrados:", token.text)
