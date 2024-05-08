from collections import deque

nodos = 10000
vis = [False] * nodos
grafo = [[] for _ in range(nodos)]
niveles = [0] * nodos

def BFS(nodoInicial):
    cola = deque()
    cola.append(nodoInicial)

    while cola:
        nodoActual = cola.popleft()
        if vis[nodoActual]:
            continue
        vis[nodoActual] = True
        for amigo in grafo[nodoActual]:
            if not vis[amigo]:
                niveles[amigo] = niveles[nodoActual] + 1
                cola.append(amigo)
        # for i in range(9):
        #     print(niveles[i], end=" ")
        # print()

def main():
    # Se asume que la entrada se leerá desde el archivo input.txt
    with open("input.txt", "r") as f:
        nodos, aristas = map(int, f.readline().split())
        for _ in range(aristas):
            nodoInicial, nodoFinal = map(int, f.readline().split())
            grafo[nodoInicial].append(nodoFinal)

        S, T = map(int, f.readline().split())
        BFS(S)
        if vis[T]:
            print(f"Sí se puede llegar de {S} a {T}")
            print(f"El nivel de {T} es {niveles[T]}")
        else:
            print(f"No se puede llegar de {S} a {T}")

if __name__ == "__main__":
    main()
