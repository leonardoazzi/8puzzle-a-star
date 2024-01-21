import numpy as np

BLANK_SPACE = "_"

class Action:
    def __init__(self, name:str, offset:tuple):
        self.name = name
        self.offset = offset

# possible_actions(): Tuple[int, int] -> List
# Objetivo: recebe uma posição na matriz 3x3 e devolve os movimentos possíveis
def possible_actions(grid, position:tuple[int,int]):
    pos_row = position[0]
    pos_col = position[1]
 
    esquerda = Action("esquerda", (0, -1))
    direita = Action("direita", (0, 1))
    acima = Action("acima", (-1, 0))
    abaixo = Action("abaixo", (1, 0))

    adjacents_moves = {esquerda, direita, acima, abaixo}

    possibilities = []

    for move in adjacents_moves:
        possible_grid = np.copy(grid)

        row_off = move.offset[0]
        col_off = move.offset[1]
        
        row = pos_row + row_off
        col = pos_col + col_off

        if (row >= 0 and row <= 2) and (col >= 0 and col <= 2):
            temp = possible_grid[pos_row, pos_col]
            possible_grid[pos_row, pos_col] = possible_grid[row, col]
            possible_grid[row,col] = temp

            possibilities.append((possible_grid, move.name))
        
        # else: movimento impossível

    return possibilities

# decod_state(state): String -> None
# Transforma o estado em um array de caracteres e converte este para
# uma matriz 3x3 do jogo.
def decod_state(state:str):
    estado = np.array(list(state))
    state_grid = estado.reshape(3,3)

    return state_grid

# cod_state(game_grid): ndarray -> str
# Transforma uma matriz de jogo em uma string em ordem linear
def cod_state(game_grid:np.ndarray[int,int])->str:
    state_arr = game_grid.flatten()
    state_list = state_arr.tolist()
    state_str = ''.join(state_list)

    return state_str
        
def sucessor(estado:str):
    sucessors_set = set()

    state_grid = decod_state(estado)

    # Busca a posição do espaço em branco na matriz e retorna
    # uma lista de ações possíveis
    for idx_row, row in enumerate(state_grid):
        for idx_col, col in enumerate(row):
            if col == BLANK_SPACE:
                actions = possible_actions(state_grid, (idx_row, idx_col))

    for grid, movement in actions:
        coded_state = cod_state(grid)
        sucessors_set.add((movement, coded_state))

    return sucessors_set