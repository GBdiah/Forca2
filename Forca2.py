import pickle
import random
import os
import sys

numero_recordes = 10
arquivo_recorde = "recorde.txt"
nome = 'nome'
pontuacao = 'pontuacao'
l_usadas = []
l_corretas = []
l_erradas = []
linhas = '_' * len(palavra_escolhida)
palavra = ''

lista_facil = ['melhor', 'grande', 'claro', 'azul', 'vermelho', 'preto', 'branco', 'casa', 'tempo', 'felicidade', 'bondade', 'vida',
'caneta', 'cavalo', 'trem', 'golpe', 'cosmos']

lista_dificil = ['procrastinar', 'prolegomenos', 'vicissitudes', 'pernostico', 'oprobrio', 'idiossincrasia', 'elucubracoes',
'chistoso', 'acrimonia', 'combustivel', 'concurso', 'protesto', 'governo', 'paquiderme', 'tamandare']

#--------------------------------FUNÇÕES------------------------------------------#

def menu():
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

def escolher_palavra(palavra): #Escolher palavra aleatória, depois que o jogo salvo for criado, atualizar para não repetir palavra prévia
    palavra = lista[random.randint(0,len(lista)-1)]
    return palavra
    
def letras_usadas(l_usadas): #Recebe o palpite e verifica se a letra já foi usado, não remove vidas, nem autentica se o palpite é correto, só verifica se ele não foi utilizado
    while True:
        print('Entre uma letra (0 para sair).', vidas, ' tentativas restantes')
        palpite = input()
        if len(palpite) != 1:
            print('Oi? Isso não é uma letra.', end='\n\n')
        elif palpite not in 'abdcefgijklmnopqrstuvwyz':
            print('Oi? Isso não é uma letra.', end='\n\n')
        elif palpite in l_usadas:
            print("Letra '", palpite,"' já utilizada. Tente Outra.", sep='', end='\n\n')
        else:
            l_usadas.append(palpite)
            return palpite
            
def de_novo(palavra):
    input('Pressione ENTER para continuar...')
    um_jogador(palavra)
    
def cont_partida():
    pass

def rank_geral():
    pass

def sair(opcao):
    pass

def limpar_tela():
    try:
        os.system('cls')
    except:
        os.system('clean')


def nova_partida():#Lembrar de passar a informação de quantos jogadores são, número de vida, lista de palavras selecionadas, e pontuação a ser dada(se um jogador).


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
    facil = 'F'
    dificil = 'D'
    print('---------------------------')
    print('         DIFICULDADE       ')
    print('---------------------------')
    print('F- FÁCIL')
    print('D- DIFÍCIL')

    while True:
        opcao = str(input('OPÇÃO DESEJADA: '))
        if opcao == facil and opcao == dificil:
            return opcao
    
def esconder_palavra(p_escolhida, linhas):
    for i in range(len(palavra)): # print dos underlines e das letras corretas
        if palavra[i] in l_corretas:
            linhas = linhas[:i] + palavra[i] + linhas[i+1:]
        print('Palavra:', end=' ')
    for letra in linhas:
        print(letra, end=' ')
    print(end='\n\n')
    return  palavra_escondida

def um_jogador(palavra):#incompleto
    while jogo_completo == False:
        escolher_palavra(palavra)
        print('Letras já utilizadas:', end=' ') # print das letras utilizadas
        for i in range(0, len(l_usadas)):
            print(l_usadas[i], end=' ')
        print(end='\n\n')
        
        esconder_palavra(palavra, linhas)    

def dois_jogadores():
    pass
'''
--------------DOIS JOGADORES ----------------
'''
def palavra_valida(receber_palavra):
    valida = True
    for caractere in string:
        if not (caractere >= 'a' and caractere <= 'z'):
            valida = False
            break
    return valida

def receber_palavra(string):
   pass
   
#--------------------------------FUNÇÕES------------------------------------------#

while True:
    opcao = menu()
    
    if opcao == 1:
        nova_partida()
        if opcao == 1:
            menu_dificuldade()
            if opcao == F:
                vidas = 5
                lista = lista_facil
                um_jogador(palavra)
            elif opcao == D:
                vidas = 3
                lista = lista_dificil
                um_jogador(palavra)
        elif opcao == 2:
            pass
        elif opcao == 3:
            menu()
            

    elif opcao == 2:
        pass

    elif opcao == 3:
        pass
    
    elif opcao == 4:
        break

if palpite in palavra: #Verifica se o palpite está na palavra, falta implementar a parte em que mostra as letras já utilizadas e a palavra em sí. PS. criei a varíavel joao só pela zuera
    letras_corretas.append(palpite)
    acertoupalavra = True
    for i in range(len(palavra)):
        if palavra[i] not in letras_corretas:
            acertoupalavra = False
            break
        if acertoupalavra:
            print('Parabéns! Você ganhou. A palavra era ', palavra,'. Pressione enter para continuar...')
            jogo_completo = True
        else:
            print('Letra ', palpite, 'não existe na palavra :(')
            letras_erradas.append(palpite)
            (joao-1)
            
            if joao = 0
            print('Jogo encerrado. Você perdeu. A palavra era ', palavra,'.Pressione enter para continuar...')
            jogo_completo = True
