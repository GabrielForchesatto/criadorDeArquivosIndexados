# encoding: utf-8
import os
import nltk
from nltk.stem import RSLPStemmer

nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('portuguese')

novoDoc = input(str("Criar novo documento [S/N]? ")).lower()

caminho = 'C:/Users/Usuario/OneDrive/Documentos/IMED/Estrutura de Dados/g2/docs/'

if novoDoc == "s":
    nome = input(str('Nome do arquivo [incluindo o .txt]: '))

    arquivo = open(caminho + nome, 'w')  # cria um aquivo no caminho

    conteudo = input(str(u'Digite o conteúdo do arquivo: ')).lower()

    arquivo.write(conteudo)  # escreve o conteúdo

cont = 0
fraseS = []
indexados = {}

for _, _, arquivo in os.walk('C:/Users/Usuario/OneDrive/Documentos/IMED/Estrutura de Dados/g2/docs/'):
    # le os arquivos presentes na pasta

    for c in arquivo:  # percorre os arquivos .txt

        ler = open(caminho + c, 'r')  # abre os arquivos .txt

        for frase in ler:  # transforma o conteudo dos arquivos de list para string

            frase = frase.split()  # remove os espaços e retorna uma list com cada palavra indentada
            #print(frase)

            for i, c in enumerate(frase):

                if frase[i] in stopwords:
                    frase.remove(frase[i])

                if frase[i] in stopwords:
                    frase.remove(frase[i])

                if frase[i] in stopwords:
                    frase.remove(frase[i])


        print(frase) #não mexer, frase sem stop word


