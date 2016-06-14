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
palavra = ''
palpite = ''

lista_facil = ['melhor', 'grande', 'claro', 'azul', 'vermelho', 'preto', 'branco', 'casa', 'tempo', 'felicidade', 'bondade', 'vida',
'caneta', 'cavalo', 'trem', 'golpe', 'cosmos']

lista_dificil = ['procrastinar', 'prolegomenos', 'vicissitudes', 'pernostico', 'oprobrio', 'idiossincrasia', 'elucubracoes',
'chistoso', 'acrimonia', 'combustivel', 'concurso', 'protesto', 'governo', 'paquiderme', 'tamandare']

#--------------------------------FUNÇÕES------------------------------------------#
def verificar_recorde(pontuacao): #verifica a pontuação do cara e onde ele será inserido no ranking
    posicao_recorde = 0
    if pontuacao > 0:
        ranking = carregar_ranking()
        posicao = posicao_recorde(ranking, pontuacao)
        if posicao < numero_recordes:
            posicao_recorde = posicao + 1
        
def inserir_recorde(nome, pontuacao):
    ranking = carregar_ranking()
    
    posicao = posicao_recorde(ranking, pontuacao)
    if posicao < numero_recorde:
        recorde = {_nome:nome, _pontuacao:pontuacao}
        ranking.insert(posicao, recorde)
        ranking = ranking[:numero_recorde]
        salvar_ranking(ranking)
        
def posicao_recorde(ranking, pontuacao): #determina a posição do recorde que vai ser usada pelo verificar_recorde antes de ser inserida
    posicao = len(ranking)
    for i in range(len(ranking)):
        registro = ranking[i]
        if registro[_pontuacao] < pontuacao:
            posicao = i
            break
    return posicao
        
def carregar_ranking(): #Carregar o ranking do arquivo contendo o mapa dos rankings
    ranking = []
    
    try:
        arquivo = open(arquivo_recorde, "rb")
        ranking = pickle.load(arq)
        arquivo.close()
    except:
        pass
    return ranking
    
def salvar_ranking():
    try:
        arquivo = open(arquivo_recorde, "wb")
        pickle.dump(ranking, arquivo)
        arquivo.close()
    except:
        pass
    
def obter_ranking(): # A ser utilizado quando o usuário quiser acessar direto do menu, falta dar o print com o menu em sí
    return carregar_ranking
    
def jogar_denovo(): #Função de jogar denovo, como já dito lá embaixo, falta ainda implementar a pontuação para carregar pros próximos jogos
    input('')


    
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
    print('2- CONTINUAR PARTIDA')
    print('3- RANKING GERAL')
    print('4- SAIR DO JOGO')

    while True:
        opcao = int(input('OPÇÃO DESEJADA: '))
        if opcao >= 0 and opcao <= 4:
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
    while len(sorteadas) < len(lista):
        palavra = lista[random.randint(0, len(lista)-1)] 
        if not(palavra in sorteadas):
            sorteadas.append(palavra)
        return palavra
    

    
def cont_partida():
    pass

def rank_geral():
    pass

def sair(opcao):
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
   pass
   
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
                    lista = lista_facil
                    jogo_completo = False
                    while jogo_completo == False:
                        palavra = sorteia()
                        print('Letras já utilizadas:', end=' ') # print das letras utilizadas
                        for i in range(0, len(l_usadas)):
                            print(l_usadas[i], end=' ')
                        print(end='\n\n')

                        esconder_palavra(l_corretas, palavra)


                        palpite = letras_usadas(l_usadas)

                        if palpite in palavra:
                            print("Boa! A letra '", palpite, "' existe na palavra :)", sep='', end='\n\n')
                            l_corretas.append(palpite)
                            acertoupalavra = True
                            for i in range(len(palavra)):
                                if palavra[i] not in l_corretas:
                                    acertoupalavra = False
                                    break
                        if palpite == ('0'):
                            break##VERIFICAR PONTUAÇÃO E ADICIONAR NO RANKING
                        
                            if acertoupalavra:
                                print("Parabéns! Você ganhou. A Palavra era '", palavra, "'.", sep='')
                                print ("Pressione enter para continuar...", end='\n\n')
                                jogo_completo = True

                        elif palpite not in l_corretas: #Letras erradas para a contagem da derrota já q vidas por algum motivo é imutável para mim
                            if palpite in 'abcdefghijklmnopqrstuvwxyzçôóõíé': 
                                if palpite not in letras_erradas:
                                    print("Letra '", palpite,"' não existe na palavra :(", sep='', end='\n\n')
                                    l_erradas.append(palpite)
                                    joao = joao - 1
                            
                        if joao == 0:
                            print ("Jogo encerrado. Você perdeu. A palavra era '", palavra,"'.", sep='')
                            print ("Pressione enter para continuar...", end='\n\n')
                            input('')
                            jogo_completo = True
                                    
                                    
                        elif jogo_completo == True: 
                            l_usadas = []
                            l_corretas = []
                            l_erradas = []
                            jogo_completo = False
                            palavra = sorteia()
                        else:
                            break
                        
                elif opcao == 2:
                    vidas = 3
                    lista = lista_dificil
                    joao = vidas
                    jogo_completo = False
                    letras_erradas = []
                    letras_corretas = []
                    letras_usadas = []
                    palavra = lista[random.randint(0,len(lista)-1)]
                    linhas = '_' * len(palavra)
                    while jogo_completo == False:

                        print('Letras já utilizadas:', end=' ') # print das letras utilizadas
                        for i in range(0, len(letras_usadas)):
                            print(letras_usadas[i], end=' ')
                        print(end='\n\n')
             
                        
                        for i in range(len(palavra)): # print dos underlines e das letras corretas
                            if palavra[i] in letras_corretas:
                                linhas = linhas[:i] + palavra[i] + linhas[i+1:]
                        print('Palavra:', end=' ')
                        for letra in linhas:
                            print(letra, end=' ')
                        print(end='\n\n')

                        print ('Entre uma letra (0 para sair).', (joao-len(letras_erradas)), 'tentativas restantes.')
                        palpite = input ('> ')
                        print()
                        
                        while palpite in letras_usadas:
                            print ("Letra '",palpite ,"' já utilizada. Tente Outra.", sep='', end='\n\n')
                            print ('Entre uma letra (0 para sair).', (joao-len(letras_erradas)), 'tentativas restantes.')
                            palpite = input ('> ')
                            print()
                          
                        
                          
                        if palpite == '0':
                            break

                        if len(palpite)!= 1:
                            print ('Oi? Isso não é só uma letra.', end='\n\n')
                            
                        elif palpite in letras_erradas:
                            print ("Letra '",palpite ,"' já utilizada. Tente Outra.", sep='', end='\n\n')
                        elif palpite not in 'abcdefghijklmnopqrstuvwxyzçôóõíé':
                            print ('Oi? Isso não é uma letra.', end='\n\n')
                            
                        elif palpite in letras_usadas:
                            print ("Letra '",palpite ,"' já utilizada. Tente Outra.", sep='', end='\n\n')
                        else:
                            letras_usadas.append(palpite)
                            if palpite in palavra: # verificação das letras na palavra
                                print("Boa! A letra '", palpite, "' existe na palavra :)", sep='', end='\n\n')
                                letras_corretas.append(palpite)
                                
                                palavra_completa = True # Verificar se o jogador ganhou
                                for (i) in range (len(palavra)):
                                    if palavra[i] not in letras_corretas:
                                        palavra_completa = False
                                        break
                                if palavra_completa:
                                    print("Parabéns! Você ganhou. A Palavra era '", palavra, "'.", sep='')
                                    print ("Pressione enter para continuar...", end='\n\n')
                                    jogo_completo = True
                                        
                        if palpite not in letras_corretas: #Letras erradas para a contagem da derrota já q vidas por algum motivo é imutável para mim
                            if palpite in 'abcdefghijklmnopqrstuvwxyzçôóõíé': 
                                if palpite not in letras_erradas:
                                    print("Letra '", palpite,"' não existe na palavra :(", sep='', end='\n\n')
                                    letras_erradas.append(palpite)
                                    
                        if len(letras_erradas) == joao :
                            print ("Jogo encerrado. Você perdeu. A palavra era '", palavra,"'.", sep='')
                            print ("Pressione enter para continuar...", end='\n\n')
                            jogo_completo = True
                            
                        if jogo_completo:
                            jogar_denovo = input ('')
                            print()
                            if jogar_denovo == (''):
                                jogo_completo = False
                                joao = vidas
                                letras_erradas = []
                                letras_corretas = []
                                letras_usadas = []
                                palavra = lista[random.randint(0,len(lista)-1)]
                                linhas = '_' * len(palavra)
                            else:
                                break
            if opcao == 3:
                voltar = True
    elif opcao == 2:
        cont_partida()
    elif opcao == 3:
        print("\n")
        print("--------------------")
        print("RANKING DE PONTUAÇÃO")
        print("--------------------")
        recordes = ranking.obter_ranking()

        if len(recordes) > 0:

            for idx in range(len(recordes)):
                recorde = recordes[idx]
                nome = ranking.obter_nome(recorde)
                pont = str(ranking.obter_pontuacao(recorde))

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
    elif opcao == 4:
        sair = True
