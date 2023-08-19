## Criando um ambinte de desenvolvimento Python

- Para verificar se o python está instalado no seu computador, rode no terminal o comando ```python -version```.
Se retornar a versão, é porque está instalado. Continue dando proseguimento, caso contrário, vai na página oficial do Python e instale.
- Execute o seguinte comando para criar as libs básicas do python: ```python -m venv env```.
- Execute o arquivo "activate". Dependendo do terminal:

>powershell ```.ps1```  
>CMD ```.bat```.

```.\env\Scripts\Activate.ps1 ou .\env\Scripts\Activate.ps1```
 Caso dê algum erro, rode o seguinte comando em outro terminal: ```set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned```, em sequência confirme ``` [S] sim``` Caso peça, reinicie o terminal novamente e rode o arquivo ```activate```.

## Compilando Python

Após todas as configurações anteriores, selecione o interpretador python que tenha o arquivo "env". 
Ex. ```.\env\Scripts\python.exe```

## Como instalar um pacote Python

Rode o comando ```pip install [nome da biblioteca]``` no caso desse curso, vamos precisar do pacote "spacy". 
Para instalar use o  comando ```pip install spacy```

## Comandos do ambiente virtual
- Ativar: Caminho para o activate ```.\env\Scripts\Activate.ps1```
- Desativar: escreva no terminal do local da pasta  ```deactivate```
 