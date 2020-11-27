# encoding: utf-8
import os
import nltk
from nltk.stem import RSLPStemmer
nltk.download('rslp')

def Stemming(frase):
    nucleo = RSLPStemmer()
    fraseNucleo = []
    for palavra in frase:
        fraseNucleo.append(nucleo.stem(palavra.lower()))
    return fraseNucleo



stopwords = ['de', 'a', 'o', 'que', 'e', 'é', 'do', 'da', 'em', 'um', 'para', 'com', 'não', 'uma', 'os', 'no', 'se',
             'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'ao', 'ele', 'das', 'à', 'seu', 'sua', 'ou', 'quando',
             'muito', 'nos', 'já', 'eu', 'também', 'só', 'pelo', 'pela', 'até', 'isso', 'ela', 'entre', 'depois', 'sem',
             'mesmo', 'aos', 'seus', 'quem', 'nas', 'me', 'esse', 'eles', 'você', 'essa', 'num', 'nem', 'suas', 'meu',
             'às', 'minha', 'numa', 'pelos', 'elas', 'qual', 'nós', 'lhe', 'deles', 'essas', 'esses', 'pelas', 'este',
             'dele', 'tu', 'te', 'vocês', 'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas', 'nosso',
             'nossa', 'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas', 'aquele', 'aquela', 'aqueles',
             'aquelas', 'isto', 'aquilo', 'estou', 'está', 'estamos', 'estão', 'estive', 'esteve', 'estivemos',
             'estiveram', 'estava', 'estávamos', 'estavam', 'estivera', 'estivéramos', 'esteja', 'estejamos', 'estejam',
             'estivesse', 'estivéssemos', 'estivessem', 'estiver', 'estivermos', 'estiverem', 'hei', 'há', 'havemos',
             'hão', 'houve', 'houvemos', 'houveram', 'houvera', 'houvéramos', 'haja', 'hajamos', 'hajam', 'houvesse',
             'houvéssemos', 'houvessem', 'houver', 'houvermos', 'houverem', 'houverei', 'houverá', 'houveremos',
             'houverão', 'houveria', 'houveríamos', 'houveriam', 'sou', 'somos', 'são', 'era', 'éramos', 'eram',
             'fui', 'foi', 'fomos', 'foram', 'fora', 'fôramos', 'seja', 'sejamos', 'sejam', 'fosse', 'fôssemos',
             'fossem', 'for', 'formos', 'forem', 'serei', 'será', 'seremos', 'serão', 'seria', 'seríamos', 'seriam',
             'tenho', 'tem', 'temos', 'tém', 'tinha', 'tínhamos', 'tinham', 'tive', 'teve', 'tivemos', 'tiveram',
             'tivera', 'tivéramos', 'tenha', 'tenhamos', 'tenham', 'tivesse', 'tivéssemos', 'tivessem', 'tiver',
             'tivermos', 'tiverem', 'terei', 'terá', 'teremos', 'terão', 'teria', 'teríamos', 'teriam']

def removerPontuacao(frase, paraRemover):
    fraseLimpa = frase
    for x in paraRemover:
        fraseLimpa = fraseLimpa.replace(x, '')
    return fraseLimpa



novoDoc = input(str("Criar novo documento [S/N]? ")).lower()

#Editar o caminho conforme o seu
caminho = 'C:/Users/LEO/Desktop/criadorDeArquivosIndexados-master/docs/'

if novoDoc == "s":
    nome = input(str('Nome do arquivo [incluindo o .txt]: '))

    arquivo = open(caminho + nome, 'w')  # cria um aquivo no caminho

    conteudo = input(str(u'Digite o conteúdo do arquivo: ')).lower()

    conteudo = removerPontuacao(conteudo, ".,:!?")

    arquivo.write(conteudo)  # escreve o conteúdo

indexados = {}

#Editar o caminho igual ao caminho anterior
for _, _, arquivos in os.walk('C:/Users/LEO\Desktop/criadorDeArquivosIndexados-master/docs/'):
    # le os arquivos presentes na pasta

    for arquivo in arquivos:  # percorre os arquivos .txt
        
        ler = open(caminho + arquivo, 'r')  # abre os arquivos .txt

        for texto in ler: 
            print("\n====== TEXTOS =====")
            print(texto)
            
            # transforma o conteudo dos arquivos de list para string
            palavras = texto.split()  # remove os espaços e retorna uma list com cada palavra indentada
            #print(palavras)                

            for i, c in enumerate(palavras): #percorre todas as palavras da list

                if palavras[i] in stopwords:
                    palavras.remove(palavras[i])

                if palavras[i] in stopwords:
                    palavras.remove(palavras[i])

                if palavras[i] in stopwords:
                    palavras.remove(palavras[i])                    

           
            for palavra in palavras:
                if palavra in texto:
                    if palavra not in indexados:
                        indexados[palavra] = arquivo
                    else:
                        if indexados[palavra] != arquivo:
                            valor = indexados[palavra] +","+ arquivo
                            indexados[palavra] = valor
            palavraSteming = Stemming(palavras) #só jesus sabe o que isso faz

print("\n")          
print(indexados)



