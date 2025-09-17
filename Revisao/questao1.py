import math, time
        
def eh_curioso(n):
    n_orig = n
    soma_fatorial = 0
    while n > 0:
        d = n % 10
        n = n // 10
        soma_fatorial += fats[d]
        if soma_fatorial > n_orig: return False
    return soma_fatorial == n_orig

fats = [math.factorial(n) for n in range(0, 10)]

n = 10
while n <= 2540160:
    if eh_curioso(n):
        print ("\n",n)
    n += 1
    if n % 1000 == 0:
        print (end=".", flush=True)