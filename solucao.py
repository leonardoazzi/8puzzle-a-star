from typing import Iterable, Set, Tuple, List
import numpy as np
from gameLogic import decod_state, possible_actions, cod_state, BLANK_SPACE
import heapq
import heuristicas

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado:str, pai:"Nodo", acao:str, custo:int):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo

    def __lt__(self, other):
        # Define a lógica de comparação
        return (self.custo, self.estado) < (other.custo, other.estado)
    

def custo_minimo(lista_nodos: List[Nodo]) -> Nodo:
    if not lista_nodos:
        return None  # Retorna None se a lista estiver vazia

    nodo_menor_custo = lista_nodos[0]

    for nodo in lista_nodos[1:]:
        if nodo.custo < nodo_menor_custo.custo:
            nodo_menor_custo = nodo

    return nodo_menor_custo

def esta_na_lista(lista, estado):
    for _, nodo in lista:
        if nodo.estado == estado:
            return True
    return False


def sucessor(estado: str) -> Set[Tuple[str, str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação, estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    sucessors_set = set()

    state_grid = decod_state(estado)

    # Encontrar a posição do espaço em branco
    for idx_row, row in enumerate(state_grid):
        for idx_col, col in enumerate(row):
            if col == BLANK_SPACE:
                blank_position = (idx_row, idx_col)
                break

    # Calcular as ações possíveis para a posição do espaço em branco
    actions = possible_actions(state_grid, blank_position)

    for grid, movement in actions:
        coded_state = cod_state(grid)
        sucessors_set.add((movement, coded_state))

    return sucessors_set


def expande(nodo:Nodo)->Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    conj_vizinhos = set()

    lista_pares = sucessor(nodo.estado)
    novo_custo = nodo.custo + 1

    for pares in lista_pares:
        movement = pares[0]
        state = pares[1]
        nodo_expandido = Nodo(state, nodo, movement, novo_custo)
        conj_vizinhos.add(nodo_expandido)

    return conj_vizinhos


def astar_hamming(estado: str) -> list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None.
    :param estado: str
    :return:
    """
    X = set()
    #fronteira formada por tuplas na forma (custo acumulado, nodo)
    #assim o método heappop utiliza o custo acumulado para definir o elemento de maior prioridade
    F = [(heuristicas.heuristica_hamming(estado), Nodo(estado, None, None, 0))]

    while F:
        _, v = heapq.heappop(F)

        if v.estado == "12345678_":
            caminho = []
            print("CUSTO HAMMING: ",v.custo)
            while v:
                caminho.append(v.acao)
                v = v.pai
            return list(reversed(caminho[:-1]))

        if v.estado not in X:
            X.add(v.estado)
            vizinhos = expande(v)
            for vizinho in vizinhos:
                if vizinho not in X:
                    heapq.heappush(F, (vizinho.custo + heuristicas.heuristica_hamming(vizinho.estado), vizinho))

    return None
 


def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    X = set()
    #fronteira formada por tuplas na forma (custo acumulado, nodo)
    #assim o método heappop utiliza o custo acumulado para definir o elemento de maior prioridade
    F = [(heuristicas.heuristica_manhattan(estado), Nodo(estado, None, None, 0))]

    while F:
        _, v = heapq.heappop(F)

        if v.estado == "12345678_":
            caminho = []
            print("CUSTO MANHATTAN: ",v.custo)
            while v:
                caminho.append(v.acao)
                v = v.pai
            return list(reversed(caminho[:-1]))

        if v.estado not in X:
            X.add(v.estado)
            vizinhos = expande(v)
            for vizinho in vizinhos:
                if vizinho not in X:
                    heapq.heappush(F, (vizinho.custo + heuristicas.heuristica_manhattan(vizinho.estado), vizinho))

    return None

#opcional,extra
def bfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def dfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def astar_new_heuristic(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

"""gabarito_hamming = astar_hamming("2_3541687")
gabarito_manhattan = astar_manhattan("2_3541687")

for i,j in zip(gabarito_hamming, gabarito_manhattan):
    print(i + "         " + j)"""