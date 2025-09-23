# Coloque aqui o código de resposta aa questao 3

def leia_arq(nome_arquivo):
    fd = open (nome_arquivo)
    triangulo = []
    for linha in fd:
        triangulo.append([int(x) for x in linha.split()])
    fd.close()
    return triangulo

# O trinângulo elaborado como lista de listas.
def melhor_caminho():
    for lin in range(1, len(triangulo)):
        triangulo[lin][0] += triangulo[lin-1][0]
        for col in range(1, len(triangulo[lin]) - 1):
            triangulo[lin][col] += max(triangulo[lin][col-1], triangulo[lin-1][col])
        triangulo[lin][-1] += triangulo[lin-1][-1]
    return max(triangulo[-1])

try:
    triangulo = leia_arq("triangle.txt")
except FileNotFoundError:
    print ("Arquivo não acessível")
except ValueError:
    print ("Erro no formato do arquivo")
else:
    resultado = melhor_caminho()
    print(f"A soma máxima do maior caminho é {resultado}")