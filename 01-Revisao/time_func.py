import timeit, sys

def calc_fat(n):
    if n >= 0:
        fat = 1
        for x in range(n, 1, -1):
            fat *= x
        print (f"O fatorial de {n} é {fat}")
    else:
        raise ValueError ("Fatorial deve ser de número >= 0")

sys.set_int_max_str_digits(32000)
n = int(input("Calcular o fatorial de? "))
print(f"Tempo {timeit.timeit (lambda: calc_fat(n), number=1)}s.")
