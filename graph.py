import heapq
from collections import defaultdict
from solucao import Nodo, sucessor, expande
import heuristicas

# Adiciona um vértice disconexo ao grafo se for um novo vértice
# v: vértice
def add_vertex(graph, v):
	if v not in graph:
		graph[v] = []

# Adiciona uma aresta ponderada entre dois vértices
# u: vértice de origem da aresta
# v: vértice de destino da aresta
# p: peso da aresta
def add_edge(graph, u, v, p):
	graph[u].append([v, p]) 

# update_weight: Any, Any, int -> Dict
# Busca o vértice u como chave no dicionário e busca o vértice v como item 
# na lista de valores. Atualiza o w da lista.
def update_weight(graph, u, v, new_weight):
	for idx, edge in enumerate(graph[u]):
		neighbour, _ = edge
		if neighbour == v:
			graph[u][idx][1] = new_weight

# astar_generic: Any -> int
# Implementa o algoritmo A* de busca informada para menor caminho em um grafo.
def astar_generic(start_node, end_node):
	graph = defaultdict(list)
	
	add_vertex(graph, start_node)
	
	distances = {v: float('infinity') for v in graph}
	pred = {v: None for v in graph}

	distances[start_node] = 0
	pq = []
	visited = set()

	for v in distances:
		heapq.heappush(pq, (distances[v], id(v), v))

	while len(pq) > 0:
		_, _, current_node = heapq.heappop(pq)

		vizinhos = expande(current_node)
		for nodo in vizinhos:
			add_edge(graph, current_node, nodo, nodo.custo)

		if current_node not in visited:
			visited.add(current_node)
			if current_node == end_node: return pred

			for neighbour, weight in graph[current_node]:
				if neighbour in visited: continue
				#TODO
				updated_distance = distances[current_node] + weight # + heuristicas.heuristica_hamming(neighbour.estado)
				if neighbour not in distances:
					distances[neighbour] = float('infinity')
					print(neighbour.estado, "\n")
					if updated_distance < distances[neighbour]:
						distances[neighbour] = updated_distance
						pred[neighbour] = current_node
						heapq.heappush(pq, (updated_distance, id(neighbour), neighbour))

	return None

n1 = Nodo("_12345678", None, None, 0)
n2 = Nodo("12345678_", None, None, 0)
print(astar_generic(n1,n2))