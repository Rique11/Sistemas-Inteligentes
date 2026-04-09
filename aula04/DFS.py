#Busca em Profundidade
inicial = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]  # 0 representa o espaço vazio
]

objetivo = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]


def conferePosicaoZero(estado):
    print("ESTADO: ", estado)
    for i in range(3):
        for j in range(3):
            if estado[i][j] == 0: #Acha a posicao do zero na matriz
                return (i, j)

def defineMovimentosPossiveis(posicao_zero):
    movimentos = []
    i, j = posicao_zero
    if i > 0: # Pode mover para cima
        movimentos.append((i - 1, j))
    if i < 2: # Pode mover para baixo
        movimentos.append((i + 1, j))
    if j > 0: # Pode mover para a esquerda
        movimentos.append((i, j - 1))
    if j < 2: # Pode mover para a direita
        movimentos.append((i, j + 1))
    return movimentos

def trocaZeroDeLugar(estado, posicao_zero, nova_posicao):
    i_nova, j_nova = nova_posicao
    novo_estado = []
    for i in range(3):
        nova_linha = []
        for j in range(3):
            if (i, j) == posicao_zero:
                nova_linha.append(estado[i_nova][j_nova])
            elif (i, j) == nova_posicao:
                nova_linha.append(0)
            else:
                nova_linha.append(estado[i][j])
        novo_estado.append(nova_linha)
    return novo_estado

def dfs():
    abertos = [inicial]
    fechados = []
    while(abertos):
        estado_atual = abertos.pop(0)
        if estado_atual == objetivo: 
            return estado_atual
        else: 
            fechados.append(estado_atual)
            posicao_zero = conferePosicaoZero(estado_atual)
            movimentos_possiveis = defineMovimentosPossiveis(posicao_zero)
            filhos = []
            for movimento in movimentos_possiveis:
                possivel_filho = trocaZeroDeLugar(estado_atual, posicao_zero, movimento)
                if possivel_filho not in fechados and possivel_filho not in abertos:
                    filhos.append(possivel_filho)
                for filho in filhos: 
                    abertos.insert(0, filho)
    return False
def main():
    resultado = dfs()
    if resultado: 
        print("Quebra cabeça resolvido!")
    else:
        print("Deu ruim")



main()