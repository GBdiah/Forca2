import pickle
import random
import os
import sys

l_usadas = ''
l_corretas = ''
l_erradas = ''

lista_facil = ['melhor', 'grande', 'claro', 'azul', 'vermelho', 'preto', 'branco', 'casa', 'tempo', 'felicidade', 'bondade', 'vida',
'caneta', 'cavalo', 'trem', 'golpe', 'cosmos']

lista_dificil = ['procrastinar', 'prolegomenos', 'vicissitudes', 'pernostico', 'oprobrio', 'idiossincrasia', 'elucubracoes',
'chistoso', 'acrimonia', 'combustivel', 'concurso', 'protesto', 'governo', 'paquiderme', 'tamandare']

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
            print('Oi? Isso não é uma letra.')
        elif palpite not in 'abdcefgijklmnopqrstuvwyz':
            print('Oi? Isso não é uma letra.')
        elif palpite in l_usadas:
            print('Letra ', palpite,' já utilizada. Tente Outra.')
        else:
            return palpite

def cont_partida():
    pass

def rank_geral():
    pass

def sair(opcao):
    pass


def nova_partida():


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
    
def esconder_palavra(palavra_original):
    pass

def um_jogador():
    pass

def dois_jogadores():
    pass

def palavra_valida(receber_palavra):
    valida = True
    for caractere in string:
        if not (caractere >= 'a' and caractere <= 'z'):
            valida = False
            break
    return valida

def receber_palavra(string):
   pass

while True:
    opcao = menu()
    
    if opcao == 1:
        nova_partida()
        if opcao == 1:
            um_jogador()
        elif opcao == 2:
            dois_jogadores()
        elif opcao == 3:
            menu()

    elif opcao == 2:
        pass

    elif opcao == 3:
        pass
    
    elif opcao == 4:
        break
