import pickle
import random
import os
import sys

numero_recordes = 10
arquivo_recorde = "recorde.txt"
_nome = 'nome'
_pontuacao = 'pontuacao'
sorteadas = []
l_usadas = []
l_corretas = []
l_erradas = []



lista_facil = ['melhor', 'grande', 'claro', 'azul', 'vermelho', 'preto', 'branco', 'casa', 'tempo', 'felicidade', 'bondade', 'vida',
'caneta', 'cavalo', 'trem', 'golpe', 'cosmos']

lista_dificil = ['procrastinar', 'prolegomenos', 'vicissitudes', 'pernostico', 'oprobrio', 'idiossincrasia', 'elucubracoes',
'chistoso', 'acrimonia', 'combustivel', 'concurso', 'protesto', 'governo', 'paquiderme', 'tamandare']

#--------------------------------FUNÇÕES------------------------------------------#
def fill(word, size):
    strlen = len(word)
    newstr = word

    for idx in range(size - strlen):
        newstr += " "

    return newstr
    
def obter_nome(recorde):
    return recorde[_nome]

def obter_pontuacao(recorde):
    return recorde[_pontuacao]

def inserir_recorde(nome, pontuacao):
    ranking = __carregar_ranking()

    posicao = __posicao_recorde(ranking, pontuacao)
    if posicao < numero_recordes:
        recorde = {_nome:nome, _pontuacao:pontuacao}

        ranking.insert(posicao, recorde)
        ranking = ranking[:numero_recordes]
        __salvar_ranking(ranking)

def verificar_recorde(pontuacao):
    pos_recorde = 0

    if pontuacao > 0:
        ranking = __carregar_ranking()

        posicao = __posicao_recorde(ranking, pontuacao)
        if posicao < numero_recordes:
            pos_recorde = posicao + 1

    return pos_recorde

def obter_ranking():
    return __carregar_ranking()

def __posicao_recorde(ranking, pontuacao):
    posicao = len(ranking)

    for idx in range(len(ranking)):
        reg = ranking[idx]
        if reg[_pontuacao] < pontuacao:
            posicao = idx
            break

    return posicao

def __carregar_ranking():
    ranking = []

    try:
        arq = open(arquivo_recorde, "rb")
        ranking = pickle.load(arq)
        arq.close()
    except:
        pass

    return ranking

def __salvar_ranking(ranking):
    try:
        arq = open(arquivo_recorde, "wb")
        pickle.dump(ranking, arq)
        arq.close()
    except:
        pass

def __gerar_ranking():
    num_recorde = verificar_recorde(pontuacao)
    if num_recorde > 0:
        print("Parabéns! Você quebrou o recorde de número " + str(num_recorde) + "!")
        nome = input('Digite seu nome: ')

        inserir_recorde(nome, pontuacao)
    else:
        print("Que pena! Você não quebrou o recorde.")
        input()

    
def limpar_tela():
    try:
        os.system('cls')
    except:
        os.system('clean')

def menu():
    limpar_tela()
    print('---------------------------')
    print('       JOGO DA FORCA       ')
    print('---------------------------')
    print('1- INICIAR NOVA PARTIDA')
    print('2- RANKING GERAL')
    print('3- SAIR DO JOGO')

    while True:
        opcao = int(input('OPÇÃO DESEJADA: '))
        if opcao >= 0 and opcao <= 3:
            return opcao
        print('DESCULPE, A OPÇÃO DESEJADA É INVÁLIDADA.')
        
def nova_partida():
    '''
    Lembrar de passar a informação de quantos jogadores são, número de vida,
    lista de palavras selecionadas, e pontuação a ser dada(se um jogador).
    '''
    limpar_tela()
    print('---------------------------')
    print('        NOVA PARTIDA       ')
    print('---------------------------')
    print('1- UM JOGADOR')
    print('2- DOIS JOGADORES')
    print('3- VOLTAR')

    while True:    
        opcao = int(input('OPÇÃO DESEJADA: '))
        if opcao >=0 and opcao <= 3:
            return opcao
        print('DESCULPE, A OPÇÃO DESEJADA É INVÁLIDADA.')

def menu_dificuldade():#Leia comentário nova_partida
    
    limpar_tela()
    print('---------------------------')
    print('         DIFICULDADE       ')
    print('---------------------------')
    print('1- FÁCIL')
    print('2- DIFÍCIL')

    while True:
        opcao = int(input('OPÇÃO DESEJADA: '))
        if opcao >= 0 and opcao <= 2:
            return opcao        


    
def letras_usadas(l_usadas): #Recebe o palpite e verifica se a letra já foi usado, não remove vidas, nem autentica se o palpite é correto, só verifica se ele não foi utilizado
    
    while True:
        
        print('Entre uma letra (0 para sair).', joao, ' tentativas restantes.')
        palpite = input('> ')
        print ()
        while palpite in l_usadas:
            print ("Letra '",palpite ,"' já utilizada. Tente Outra.", sep='', end='\n\n')
            print ('Entre uma letra (0 para sair).', (joao), 'tentativas restantes.')
            palpite = (str(input('> ')))
            print()

        
        
        if len(palpite) != 1:
            print('Oi? Isso não é uma letra.', end='\n\n')
        
        elif palpite not in 'abcdefghijklmnopqrstuvwxyzçôóõíé':
            print('Oi? Isso não é uma letra.', end='\n\n')
        elif palpite in l_usadas:
            print("Letra '", palpite,"' já utilizada. Tente Outra.", sep='', end='\n\n')
        else:
            l_usadas.append(palpite)
        return palpite
            

    

def sorteia():
    while len(lista) > 0:
        palavra = lista[random.randint(0, len(lista)-1)] 
        if not(palavra in sorteadas):
            sorteadas.append(palavra)
        return palavra
    

def rank_geral():
    pass


def esconder_palavra(l_corretas, palavra):
    linhas = '_' * len(palavra)
    for i in range(len(palavra)): # print dos underlines e das letras corretas
        if palavra[i] in l_corretas:
            linhas = linhas[:i] + palavra[i] + linhas[i+1:]
    print('Palavra:',end=' ')
    for letra in linhas:
        print(letra, end=' ')
    print(end='\n\n')
    return linhas


'''
--------------DOIS JOGADORES ----------------
'''       

def dois_jogadores():
    pass



def receber_palavra(string):
    print('Entre com a palavra que deve ser utilizada nessa partida.')
    palavra = input('>')
    return palavra
   
#--------------------------------FUNÇÕES------------------------------------------#

sair = False
while (not sair):
    opcao = menu()

    if opcao == 1:
        voltar = False
        while (not voltar):
            opcao = nova_partida()
            if opcao == 1:
                opcao = menu_dificuldade()
                if opcao == 1:
                    limpar_tela()
                    vidas = 5
                    joao = vidas
                    lista = list(lista_facil)
                    jogo_completo = False
                    palavra = sorteia()
                    pontuacao = 0
                    while jogo_completo == False:
                        limpar_tela()
                        print('Letras já utilizadas:', end=' ') # print das letras utilizadas
                        for i in range(0, len(l_usadas)):
                            print(l_usadas[i], end=' ')
                        print(end='\n\n')

                        esconder_palavra(l_corretas, palavra)


                        palpite = letras_usadas(l_usadas)

                        if palpite == ('0'):
                            __gerar_ranking()
                            break



                        if palpite in palavra:
                            print("Boa! A letra '", palpite, "' existe na palavra :)", sep='', end='\n\n')
                            l_corretas.append(palpite)
                            acertoupalavra = True
                            for i in range(len(palavra)):
                                if palavra[i] not in l_corretas:
                                    acertoupalavra = False
                                    break
                                                
                            if acertoupalavra:
                                print("Parabéns! Você ganhou. A Palavra era '", palavra, "'.", sep='')
                                print ("Pressione enter para continuar...", end='\n\n')
                                input()
                                pontuacao = pontuacao + (1000 + (joao * 100))                                
                                jogo_completo = True


                        elif palpite not in l_corretas: #Letras erradas para a contagem da derrota já q vidas por algum motivo é imutável para mim
                            if palpite in 'abcdefghijklmnopqrstuvwxyzçôóõíé': 
                                if palpite not in l_erradas:
                                    print("Letra '", palpite,"' não existe na palavra :(", sep='', end='\n\n')
                                    l_erradas.append(palpite)
                                    joao = joao - 1
                            
                        if joao == 0:
                            print ("Jogo encerrado. Você perdeu. A palavra era '", palavra,"'.", sep='')
                            print ("Pressione enter para continuar...", end='\n\n')
                            input('')
                            __gerar_ranking()
                            l_usadas = []
                            l_corretas = []
                            l_erradas = []
                            sorteadas = []
                            voltar = True
                            break
                                    
                                    
                        if jogo_completo == True:
                            lista.remove(palavra)
                            l_usadas = []
                            l_corretas = []
                            l_erradas = []
                            joao = 5
                            jogo_completo = False
                            palavra = sorteia()
                            if len(lista) == 0:
                                print('Não existem mais palavras para serem sorteadas :(')
                                print('Pressione enter para continuar...')
                                input()
                                __gerar_ranking()
                                
                                voltar = True
                                break
                  
                elif opcao == 2:
                    limpar_tela()
                    vidas = 3
                    joao = vidas
                    lista = list(lista_dificil)
                    jogo_completo = False
                    palavra = sorteia()
                    pontuacao = 0
                    while jogo_completo == False:
                        limpar_tela()
                        print('Letras já utilizadas:', end=' ') # print das letras utilizadas
                        for i in range(0, len(l_usadas)):
                            print(l_usadas[i], end=' ')
                        print(end='\n\n')

                        esconder_palavra(l_corretas, palavra)


                        palpite = letras_usadas(l_usadas)

                        if palpite == ('0'):
                            __gerar_ranking()
                            break 



                        if palpite in palavra:
                            print("Boa! A letra '", palpite, "' existe na palavra :)", sep='', end='\n\n')
                            l_corretas.append(palpite)
                            acertoupalavra = True
                            for i in range(len(palavra)):
                                if palavra[i] not in l_corretas:
                                    acertoupalavra = False
                                    break
                                                
                            if acertoupalavra:
                                print("Parabéns! Você ganhou. A Palavra era '", palavra, "'.", sep='')
                                print ("Pressione enter para continuar...", end='\n\n')
                                input()
                                pontuacao = pontuacao + (2000 + (joao * 100))                                
                                jogo_completo = True


                        elif palpite not in l_corretas: #Letras erradas para a contagem da derrota já q vidas por algum motivo é imutável para mim
                            if palpite in 'abcdefghijklmnopqrstuvwxyzçôóõíé': 
                                if palpite not in l_erradas:
                                    print("Letra '", palpite,"' não existe na palavra :(", sep='', end='\n\n')
                                    l_erradas.append(palpite)
                                    joao = joao - 1
                            
                        if joao == 0:
                            print ("Jogo encerrado. Você perdeu. A palavra era '", palavra,"'.", sep='')
                            print ("Pressione enter para continuar...", end='\n\n')
                            input('')
                            __gerar_ranking()
                            l_usadas = []
                            l_corretas = []
                            l_erradas = []
                            sorteadas = []
                            voltar = True
                            break
                                    
                                    
                        if jogo_completo == True:
                            lista.remove(palavra)
                            l_usadas = []
                            l_corretas = []
                            l_erradas = []
                            joao = 3
                            jogo_completo = False
                            palavra = sorteia()
                            if len(lista) == 0:
                                print('Não existem mais palavras para serem sorteadas :(')
                                print('Pressione enter para continuar...')
                                input()
                                __gerar_ranking()
                                voltar = True
                                break
    
            if opcao == 2:
                limpar_tela()
                lista = []
                vidas = 5
                joao = vidas
                print('Digite a palavra para desafiar seu amigo!')
                lista.append(input('>'))
                jogo_completo = False
                palavra = sorteia()
                pontuacao = 0
                while jogo_completo == False:
                    limpar_tela()
                    print('Letras já utilizadas:', end=' ') # print das letras utilizadas
                    for i in range(0, len(l_usadas)):
                        print(l_usadas[i], end=' ')
                    print(end='\n\n')

                    esconder_palavra(l_corretas, palavra)

                    palpite = letras_usadas(l_usadas)

                    if palpite == ('0'):
                        break

                    if palpite in palavra:
                        print("Boa! A letra '", palpite, "' existe na palavra :)", sep='', end='\n\n')
                        l_corretas.append(palpite)
                        acertoupalavra = True
                        for i in range(len(palavra)):
                            if palavra[i] not in l_corretas:
                                acertoupalavra = False
                                break

                        if acertoupalavra:
                            print("Parabéns! Você ganhou. A Palavra era '", palavra, "'.", sep='')
                            print ("Pressione enter para continuar...", end='\n\n')
                            input()
                            pontuacao = pontuacao + (1000 + (joao * 100))                                
                            jogo_completo = True

                    elif palpite not in l_corretas: #Letras erradas para a contagem da derrota já q vidas por algum motivo é imutável para mim
                        if palpite in 'abcdefghijklmnopqrstuvwxyzçôóõíé': 
                            if palpite not in l_erradas:
                                print("Letra '", palpite,"' não existe na palavra :(", sep='', end='\n\n')
                                l_erradas.append(palpite)
                                joao = joao - 1

                    if joao == 0:
                        print ("Jogo encerrado. Você perdeu. A palavra era '", palavra,"'.", sep='')
                        print ("Pressione enter para continuar...", end='\n\n')
                        input('')
                        l_usadas = []
                        l_corretas = []
                        l_erradas = []
                        sorteadas = []
                        voltar = True
                        break
                                    
                                    
                    if jogo_completo == True:
                        lista.remove(palavra)
                        l_usadas = []
                        l_corretas = []
                        l_erradas = []
                        joao = 5
                        print('Digite a palavra para desafiar seu amigo!')
                        lista.append(input('>'))
                        jogo_completo = False
                        palavra = sorteia()
                        
                    
            if opcao == 3:
                voltar = True
    
    elif opcao == 2:
        limpar_tela()
        print("\n")
        print("--------------------")
        print("RANKING DE PONTUAÇÃO")
        print("--------------------")
        recordes = obter_ranking()

        if len(recordes) > 0:

            for idx in range(len(recordes)):
                recorde = recordes[idx]
                nome = obter_nome(recorde)
                pont = str(obter_pontuacao(recorde))

                print("#%02d " % (idx+1), end="")
                print(fill(nome, 30), end="")
                print("%8s" % pont)
            print()
            print('Pressione enter para continuar...')
            input()
        else:
            print('Nenhum registro a exibir.', end='\n\n')
            print('Pressione enter para continuar...')
            input()

        print("\n")
    elif opcao == 3:
        sair = True
