from gameLogic import decod_state, possible_actions, cod_state, BLANK_SPACE
import numpy as np

def heuristica_hamming(estado:str)->int:
    return sum(char1 != char2 for char1, char2 in zip(estado, "12345678_"))

def heuristica_manhattan(estado:str)->int:
    tabuleiro_atual = decod_state(estado)
    objetivo = decod_state("12345678_")

    soma_manhattan = 0

    #percorre o tabuleiro no estado atual o comparando com o objetivo
    #cada iteração verifica quantos movimentos são necessarios para levar uma peça até a posição desejada
    #a quantidade de movimentos é dado pela expressão |x_atual - x_objetivo| + |y_atual - y_objetivo|
    #ao final da iteração adiciona a quantidade de movimentos a uma variável acumuladora (soma_manhattan)
    for i in range(3):
        for j in range(3):
            if tabuleiro_atual[i,j] != BLANK_SPACE:
                valor_atual = tabuleiro_atual[i,j]
                pos_objetivo = np.where(objetivo == valor_atual)
                soma_manhattan += (abs(i - pos_objetivo[0]) + abs(j - pos_objetivo[1]))
                
    #o valor retornado pela função é a soma de quantos movimentos são necessarios para levar todas as peças até as posições desejadas
    return soma_manhattan
                                   
