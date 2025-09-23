def hanoi (n, de, para):
    if n == 1:
        print (f"Mova o disco {n} de {de} para {para}")
    else:
        interm = 6 - de - para
        hanoi (n-1, de, interm)
        print (f"Mova o disco {n} de {de} para {para}")
        hanoi (n-1, interm, para)
        
hanoi(4, 1, 3)
    