import timeit

def mesmos_digitos(a, b):
     return sorted(str(a)) == sorted(str(b))

def encontra_validos(limite):
    n = 1
    encontrados = 0
    while encontrados < limite:
        n2 = 2 * n
        n3 = 3 * n
        n4 = 4 * n
        n5 = 5 * n
        n6 = 6 * n
        if (mesmos_digitos(n, n2) and
            mesmos_digitos(n, n3) and
            mesmos_digitos(n, n4) and
            mesmos_digitos(n, n5) and
            mesmos_digitos(n, n6)):
            print (n, n2, n3, n4, n5, n6)
            encontrados += 1       
        n += 1

encontra_validos(10)