import os
from unicodedata import normalize
import nltk
from nltk.stem import RSLPStemmer

nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('portuguese')

def removeAcentos(text):
    return normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')


novoDoc = input(str("Criar novo documento [S/N]? "))

caminho = 'C:/Users/Usuario/OneDrive/Documentos/IMED/Estrutura de Dados/g2/docs/'

if novoDoc == "s":

    nome = input(str('Nome do arquivo [incluindo o .txt]: '))
    arquivo = open(caminho + nome, 'w')  # cria um aquivo no caminho
    conteudo = input(str(f"Digite o conteúdo do arquivo {nome}: "))
    conteudo = removeAcentos(conteudo)
    arquivo.write(conteudo)  # escreve o conteúdo

cont = 0
fraseS = []
indexados = {}

for _, _, arquivo in os.walk('C:/Users/Usuario/OneDrive/Documentos/IMED/Estrutura de Dados/g2/docs/'):
    # le os arquivos presentes na pasta

    for c in arquivo:  #percorre os arquivos .txt

        ler = open(caminho + c, 'r')  # abre os arquivos .txt
        print(ler.readlines()) #Frase SEM tokenização

        for frase in ler:  #Tokenização

            frase = frase.split().lower() #Normalização
            print(frase) #frase com stopwords

            for i, c in enumerate(frase):

                if frase[i] in stopwords:
                    frase.remove(frase[i])

                if frase[i] in stopwords:
                    frase.remove(frase[i])

                if frase[i] in stopwords:
                    frase.remove(frase[i])


            #print(frase) #não mexer, frase sem stop word