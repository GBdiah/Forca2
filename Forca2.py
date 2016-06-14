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
p_usadas = []
palavra = ''
linhas = '_' * len(palavra)
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
    print ('Parabéns! Você ganhou. A palavra era ', palavra,'. Pressione enter para continuar...')
    return input().startswitch('')

def escolher_palavra(palavra): #Escolher palavra aleatória, depois que o jogo salvo for criado, atualizar para não repetir palavra prévia
    palavra = lista[random.randint(0,len(lista)-1)]
    return palavra
    
def limpar_tela():
    try:
        os.system('cls')
    except:
        os.system('clean')

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
        
def nova_partida():
    '''
    Lembrar de passar a informação de quantos jogadores são, número de vida,
    lista de palavras selecionadas, e pontuação a ser dada(se um jogador).
    '''
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
        print('Entre uma letra (0 para sair).', vidas, ' tentativas restantes')
        palpite = input()
        if len(palpite) != 1:
            print('Oi? Isso não é uma letra.', end='\n\n')
        elif palpite not in 'abdcefgijklmnopqrstuvwyzx':
            print('Oi? Isso não é uma letra.', end='\n\n')
        elif palpite in l_usadas:
            print("Letra '", palpite,"' já utilizada. Tente Outra.", sep='', end='\n\n')
        else:
            l_usadas.append(palpite)
        return palpite
            
def de_novo(palavra):
    input('Pressione ENTER para continuar...')
    um_jogador(palavra)

def sorteia(lista, sorteadas):
    while len(sorteadas) < len(lista):
        indice = random.randint(0, len(lista)-1) 
        if not(indice in sorteadas):
            sorteadas.append(indice)
        return (palavra)
    

    
def cont_partida():
    pass

def rank_geral():
    pass

def sair(opcao):
    pass


def esconder_palavra(p_escolhida, linhas):
    for i in range(len(palavra)): # print dos underlines e das letras corretas
        if palavra[i] in l_corretas:
            linhas = linhas[:i] + palavra[i] + linhas[i+1:]
        print('Palavra:', end=' ')
    for letra in linhas:
        print(letra, end=' ')
    print(end='\n\n')
    return  palavra_escondida

def um_jogador(l_usadas, palpite, palavra, acertoupalavra ):#incompleto
    jogo_completo = True
    while (not jogo_completo):
        escolher_palavra(lista)
        print('Letras já utilizadas:', end=' ') # print das letras utilizadas
        for i in range(0, len(l_usadas)):
            print(l_usadas[i], end=' ')
        print(end='\n\n')

        esconder_palavra(palavra, linhas)


        pegar_palpite(l_usadas, vidas)

        if palpite in palavra: 
            letras_corretas.append(palpite)
            acertoupalavra = True
            for i in range(len(palavra)):
                if palavra[i] not in letras_corretas:
                    acertoupalavra = False
                    break
            if acertoupalavra:
                print("Parabéns! Você ganhou. A Palavra era '", palavra, "'.", sep='')
                print ("Pressione enter para continuar...", end='\n\n')
                jogo_completo = True
            else:
                print("Letra '", palpite,"' não existe na palavra :(", sep='', end='\n\n')
                l_erradas.append(palpite)
                (joao-1)
            
                if joao == 0:
                    print ("Jogo encerrado. Você perdeu. A palavra era '", palavra,"'.", sep='')
                    print ("Pressione enter para continuar...", end='\n\n')
                    jogo_completo = True
                    p_usadas.append(palavra)
            if jogo_completo == True: 
                if jogar_denovo():
                    letras_usadas = []
                    letras_corretas = []
                    letras_erradas = []
                    jogo_completo = False
                    palvra = escolherpalavra(palavra)
                else:
                    sys.exit()
       

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
                    vidas = 5
                    lista = lista_facil
                    um_jogador()
                elif opcao == 2:
                    vidas = 3
                    lista = lista_dificil
                    opcao = um_jogador()
            if opcao == 3:
                voltar = True
    elif opcao == 2:
        cont_partida()
    elif opcao == 3:
        ranking()
    elif opcao == 4:
        sair = True
