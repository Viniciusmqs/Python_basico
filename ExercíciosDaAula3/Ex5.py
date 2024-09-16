def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

def potencia(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * potencia(base, expoente - 1)

def resto(dividendo, divisor):
    if dividendo < divisor:
        return dividendo
    else:
        return resto(dividendo - divisor, divisor)

def quociente(dividendo, divisor):
    if dividendo < divisor:
        return 0
    else:
        return 1 + quociente(dividendo - divisor, divisor)

def produto(a, b):
    if b == 0:
        return 0
    else:
        return a + produto(a, b - 1)

def suc(n):
    return n + 1

def pred(n):
    return n - 1

def soma(n1, n2):
    if n2 == 0:
        return n1
    else:
        return soma(suc(n1), pred(n2))

if __name__ == "__main__":
    # Testes
    print("Fatorial de 5:", fatorial(5))              # =120
    print("Potência de 2^3:", potencia(2, 3))         # = 8
    print("Resto de 7/3:", resto(7, 3))               # = 1
    print("Quociente de 7/3:", quociente(7, 3))       # = 2
    print("Produto de 3 e 4:", produto(3, 4))         # = 12
    print("Soma de 3 e 4:", soma(3, 4))               # = 7