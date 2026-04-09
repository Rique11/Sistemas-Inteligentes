# Busca com backtracking aula 03 SI 
grafo = {
    'A': ['B', 'C', 'D', 'E'],
    'B': ['A', 'C', 'D', 'E'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['A', 'B', 'C', 'E'],
    'E': ['A', 'B', 'C', 'D'],
}

grafo1 = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

def objetivoConcluido(LE, grafo):
    vertices_grafo = set(grafo.keys()) 
    print("RESULTADO: " , LE)
    if len(LE) == len(grafo) + 1 and LE[0] == LE[-1] and vertices_grafo.issubset(LE):
        return True
    else: return False

def buscaBacktracking(grafo, inicial):
    LE = []
    LNE = [inicial]
    BSS = []
    EC = inicial
    while(LNE != []):
        print(grafo[EC])
        if objetivoConcluido(LE, grafo):
            return LE
        if grafo[EC] == []:
            while(LE != [] and EC == LE[0]): 
                BSS.append(EC)
                LE.pop(0)
                LNE.pop(0)
                EC = LNE[0]
                LE.append(EC)
        else: 
            for filho in grafo[EC]:
                print(filho)
                if filho not in BSS and filho not in LNE:
                    print("PASSOU AQUI ")
                    LNE.append(filho)
            EC = LNE.pop(0)
            LE.append(EC)
            print("LNE: ", LNE)
     
    return False


def main():
    teste = buscaBacktracking(grafo, 'A')
    print(teste)


main()