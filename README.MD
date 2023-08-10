## Criando um ambinte de desenvolvimento Python

- Verifique se o mesmo esta instalado no seu computador rode no terminal ```python -version```.
Se retornar a versão e por que esta estalado e continue dando proseguimento caso contrario vai na pagina oficial do Python e estale o mesmo.
- Execute o seguinte comando para criar as libs basicas do python ```python -m venv env```.
- Execute o arquivo activate dependendo terminal se for powershell ```.ps1``` e se for CMD ```.bat```.

```.\env\Scripts\Activate.ps1 ou .\env\Scripts\Activate.ps1```
 caso de algum erro rode o seguinte comando em outro terminal ```set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned``` em sequencia dando ``` [S] sim``` caso peça reinicie o terminal novamente e rode o arquivo ```activate```.

## Compilando Python

Apos todas as cofigurações anteriores selecione a interpretador python que tenha o arquivo env algo como ```.\env\Scripts\python.exe```

## Como estalar um pacote Python

Simplesmente rode o comando ```pip install [nome da biblioteca]``` no nosso caso desse curso vamos precisar do pacote spacy rondando assim o  comando ```pip install spacy```

## Comandos do ambiente virtual
- Ativar: Caminho para o activate ```.\env\Scripts\Activate.ps1```
- Desativando: escrevendo no terminal da local da pasta  ```deactivate```
 