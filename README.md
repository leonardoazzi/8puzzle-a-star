# 8puzzle-a-star
A* Search Algorithm implemented to solve the 8-puzzle game, with Manhattan and Hamming heuristics.

O 8-puzzle é composto por uma moldura 3x3 contendo um conjunto de peças numeradas de 1 a 8 eum espaço vazio. Uma peça vizinha ao espaço vazio pode ser deslizada para ele. O objetivo é alcançar um estado onde as peças numeradas estão em ordem.

![image](https://github.com/leonardoazzi/8puzzle-a-star/assets/13557537/7cacde04-90bf-4c9a-9bc0-f9eff121c853)

## Bibliotecas:
`numpy==1.26.3`

## Benchmark
ENTRADA: "2_3541687"

### Heurística de Hamming
- Nodos expandidos com hamming: 14093
- Custo: 23
- Tempo de execução: 0.3370978832244873 seconds

### Heurística de Manhattan
- Nodos expandidos com manhattan: 1837
- Custo: 23
- Tempo de execução: 0.5931434631347656 seconds

---
Universidade Federal do Rio Grande do Sul

Instituto de Informática - Departamento de Informática Aplicada

Inteligência Artificial - Prof. Joel Luís Carbonera (2023/2)
