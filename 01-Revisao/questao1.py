import math, timeit
        
def eh_curioso(n):
    n_orig = n
    soma_fatorial = 0
    while n > 0:
        d = n % 10
        n = n // 10
        soma_fatorial += fats[d]
    return soma_fatorial == n_orig

def gen_curiosos():
    n = 10
    while n <= 2540160:
        if eh_curioso(n):
            print (n)
        n += 1
    
fats = [math.factorial(n) for n in range(0, 10)]
t1 = timeit.default_timer()
gen_curiosos()
print (f"Tempo: {timeit.default_timer()-t1}s")