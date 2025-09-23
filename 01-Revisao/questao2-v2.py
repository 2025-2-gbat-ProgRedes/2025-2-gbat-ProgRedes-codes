def mesmos_digitos(a, b):
     return sorted(str(a)) == sorted(str(b))
 
n = 1
encontrados = 0
while encontrados < 10:
    if all([mesmos_digitos(n, i * n) for i in range(2,7)]):
        print (n, 2*n, 3*n, 4*n, 5*n, 6*n)
        encontrados += 1   
    n += 1