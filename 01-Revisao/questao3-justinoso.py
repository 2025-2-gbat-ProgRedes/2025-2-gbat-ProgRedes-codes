# Coloque aqui o código de resposta aa questao 3

def leia_arq(nome_arquivo):
    fd = open (nome_arquivo)
    triangulo = []
    for linha in fd:
        triangulo.append([int(x) for x in linha.split()])
    fd.close()
    print (triangulo)
    return triangulo

# O trinângulo elaborado como lista de listas.
def melhor_caminho(linha, coluna, soma_atual):
    if linha == len(triangulo) -1: #Ao chegar na base no triângulo, realiza a parada das operações
        return soma_atual + triangulo [linha][coluna]

    #Explora as opções do lado esquerdo do triângulo
    caminho1 = melhor_caminho(linha + 1, coluna, soma_atual + triangulo[linha][coluna])

    #Explora as opções do lado direito do triângulo
    caminho2 = melhor_caminho(linha + 1, coluna + 1, soma_atual + triangulo[linha][coluna])

    #Retorna o maior resultado obtido dos dois caminhos
    return max(caminho1, caminho2)

triangulo = leia_arq("triangle.txt")
resultado = melhor_caminho(0,0,0)
print(f"A soma máxima do melhor caminho é {resultado}")