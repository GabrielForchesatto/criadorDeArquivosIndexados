# encoding: utf-8
import os
import pickle
import nltk
from nltk.stem import RSLPStemmer

nltk.download('rslp')


# Agrupando as funções previamente
def Stemming(frase):
    nucleo = RSLPStemmer()
    fraseNucleo = []
    for palavra in frase:
        fraseNucleo.append(nucleo.stem(palavra.lower()))
    return fraseNucleo


def removerPontuacao(frase, paraRemover):
    fraseLimpa = frase
    for x in paraRemover:
        fraseLimpa = fraseLimpa.replace(x, '')
    return fraseLimpa


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

# Editar o caminho conforme o seu
caminho = 'C:/Users/Usuario/OneDrive/Documentos/IMED/Estrutura de Dados/g2/docs/'

# Menu e ciclo de execução da aplicação
print('------- INDEXAÇÃO -------')
print("""0. Encerrar a aplicação
1. Criar Novo Documento
2. Indexar documentos '.txt' presentes na pasta docs/
3. Realizar consultas
    1. Usando operador OR
    2. Usando operador AND
    3. [opcional] Usando expressões booleanas
4. Mostrar Índice Invertido (para debug / print)""")

while True:
    # O que o usuário deseja fazer
    decision = input(str("Digite a opção: "))

    # Verificando se o comando é válido ou não
    if decision not in '01234':
        print("Comando inváido")

    else:
        # Instanciando as variáveis necessárias
        indexados = {}
        frase_final = []

        if decision == "1":
            nome = input(str('Nome do arquivo [incluindo o .txt]: '))

            arquivo = open(caminho + nome, 'w')  # cria um aquivo no caminho

            conteudo = input(str(u'Digite o conteúdo do arquivo: ')).lower()

            conteudo = removerPontuacao(conteudo, ".,:!?")

            arquivo.write(conteudo)  # escreve o conteúdo



        elif decision == "2":
            # Instanciando o objeto pickle responsável por criar/escrever o arquivo, "wb" = write binary
            pickle_out = open("dict_index.txt", "wb")
            # Editar o caminho igual ao caminho anterior
            for _, _, arquivos in os.walk('C:/Users/Usuario/OneDrive/Documentos/IMED/Estrutura de Dados/g2/docs/'):
                # le os arquivos presentes na pasta

                for arquivo in arquivos:  # percorre os arquivos .txt

                    print(arquivo)
                    ler = open(caminho + arquivo, 'r')  # abre os arquivos .txt

                    for texto in ler:
                        #print("\n====== TEXTOS =====")
                        # print(texto)

                        # transforma o conteudo dos arquivos de list para string
                        palavras = texto.split()  # remove os espaços e retorna uma list com cada palavra indentada
                        # print(palavras)

                        for i, c in enumerate(palavras):  # percorre todas as palavras da list

                            if palavras[i] in stopwords:
                                palavras.remove(palavras[i])

                            if palavras[i] in stopwords:
                                palavras.remove(palavras[i])

                            if palavras[i] in stopwords:
                                palavras.remove(palavras[i])

                        palavras = Stemming(palavras)

                        for palavra in palavras:

                            if palavra in texto:
                                if palavra not in indexados:
                                    indexados[palavra] = arquivo
                                else:
                                    if indexados[palavra] != arquivo:
                                        valor = indexados[palavra] + "," + arquivo
                                        indexados[palavra] = valor
            # Salva o dicionário e fecha o objeto pickle
            pickle.dump(indexados, pickle_out)
            pickle_out.close()

        elif decision == "4":
            # Instancia o objeto pickle, abre o arquivo em modo "rb" = read byte
            pickle_in = open("dict_index.txt", "rb")
            final_dict = pickle.load(pickle_in)
            for k, v in final_dict.items():
                print(f"Palavra: {k}, Docs: {v}")
            break

        elif decision == "0":
            break