# encoding: utf-8
import os
import pickle
import nltk

from nltk.stem import RSLPStemmer

nltk.download('rslp')

# Agrupando as funções previamente


#Stemming para retornar como lista
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

def removerStopWords(palavras):
    for i, c in enumerate(palavras):  # percorre todas as palavras da list
        if i == len(palavras):
            break
        elif palavras[i] in stopwords:
            palavras.remove(palavras[i])
        if i == len(palavras):
            break
        elif palavras[i] in stopwords:
            palavras.remove(palavras[i])
        if i == len(palavras):
            break
        elif palavras[i] in stopwords:
            palavras.remove(palavras[i])
    return palavras

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
caminho = 'C:/Users/LEO/Desktop/criadorDeArquivosIndexados-master/docs/'

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
    if "0" in decision:
        break
    # Verificando se o comando é válido ou não
    elif decision not in '01234' and decision != "dahaf":
        print("Comando inváido")


    else:
        # Instanciando as variáveis necessárias
        indexados = {}
        frase_final = []


        if decision == "1":
            nome = input(str('Nome do arquivo [incluindo o .txt]: '))
            arquivo = open(caminho + nome, 'w')  # cria um aquivo no caminho
            conteudo = input(str(u'Digite o conteúdo do arquivo: ')).lower()
            conteudo = removerPontuacao(conteudo, '".,:!?"%¨$&*)({}[]><;|/!-_=+')
            arquivo.write(conteudo)  # escreve o conteúdo

        elif decision == "2":
            # Instanciando o objeto pickle responsável por criar/escrever o arquivo, "wb" = write binary
            pickle_out = open("dict_index.txt", "wb")

            # Editar o caminho igual ao caminho anterior
            for _, _, arquivos in os.walk('C:/Users/LEO/Desktop/criadorDeArquivosIndexados-master/docs/'):
                # le os arquivos presentes na pasta

                for arquivo in arquivos:  # percorre os arquivos .txt

                    print(arquivo)
                    ler = open(caminho + arquivo, 'r')  # abre os arquivos .txt

                    for texto in ler:
                        # transforma o conteudo dos arquivos de list para string
                        palavras = texto.split()  # remove os espaços e retorna uma list com cada palavra indentada

                        removerStopWords(palavras)

                        palavras = Stemming(palavras)

                        for palavra in palavras:
                            if palavra in texto:
                                if palavra not in indexados:
                                    listaDeValores = []
                                    listaDeValores.append(arquivo)
                                    indexados[palavra] = listaDeValores #indexa a palavra
                                else:
                                    if arquivo not in indexados[palavra]: #indexa o arquivo como value para a key palavra
                                        indexados[palavra].append(arquivo)
                                        

            # Salva o dicionário e fecha o objeto pickle
            pickle.dump(indexados, pickle_out)
            pickle_out.close()

        elif decision == "3":
            pickle_in = open("dict_index.txt", "rb")
            final_dict = pickle.load(pickle_in)

            while True:
                option = str(input("""
    0. Sair
    1. Usando operador OR
    2. Usando operador AND
    3. [opcional] Usando expressões booleanas
    : """))
                if option not in '0123':
                    print("Comando inváido")

                if option == "0":
                    break

                
                busca = str(input("Insira as palavras: ").strip().lower())
                busca = removerPontuacao(busca, '".,:!?"%¨$&*)({}[]><;|/!-_=+')
                busca = busca.split()
                busca = removerStopWords(busca)
                busca = Stemming(busca)
                


                if option == "1":
                    #print(palavra1Stemming)
                    #print(final_dict.get(palavra1Stemming))
                    for palavra in busca:
                        if palavra in final_dict.keys():
                            print(f"A palavra {palavra} esta no(s) arquivo(s): {final_dict.get(palavra)}")
                        else:
                            print(f"A palavra {palavra} não está indexada")

                if option == "2":
                    

                    listaConjuntos = []

                    for palavra in busca:
                        
                        if palavra not in final_dict: #se ambas as palavras não estão indexadas
                            print(f"A palavra {palavra} não está indexada")
                            

                    
                        valorPalavra = final_dict.get(palavra) #pegar os Values da key palavra
                        listaConjuntos.append(valorPalavra)
                        
                    final = []
                    
                    if len(busca) == 1:
                        print(listaConjuntos)
                    if len(busca) == 2:
                        l = list(set(listaConjuntos[0]).intersection(listaConjuntos[1]))
                        final = l
                        # final.append(l)
                    elif len(busca) == 3:
                        l = list(set(listaConjuntos[0]).intersection(listaConjuntos[1]).intersection(listaConjuntos[2]))
                        final = l
                    elif len(busca) == 4:
                        l = list(set(listaConjuntos[0]).intersection(listaConjuntos[1]).intersection(listaConjuntos[2]).intersection(listaConjuntos[3]))
                        final = l
                    else:
                        print("Número de palavras chave maior que o permitido")
                        break
                    relacionado = False
                    sim = []
                    nao = ""
                    for item in listaConjuntos:
                        for valores in item:
                            if valores in final:
                                relacionado = True
                                if valores not in sim:
                                    sim.append(valores)
                                
                            else:
                                relacionado = False
                                nao = "Sem interseçao"
                    if len(sim) > 0 :
                        relacionado = True
                    
                    if relacionado == True:
                        print(sim)
                    else:
                        print(nao)
                        
                        
        elif decision == "4":
            # Instancia o objeto pickle, abre o arquivo em modo "rb" = read byte
            pickle_in = open("dict_index.txt", "rb")
            final_dict = pickle.load(pickle_in)
            for k, v in final_dict.items():
                print(f"Palavra: {k}, Docs: {v}")


    if decision == "dahaf":
        for c in range(5, 1, -1):
            print(c)
        os.system("shutdown/s")