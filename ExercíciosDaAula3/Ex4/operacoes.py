import math

# Função de soma
def soma(a, b):
    return a + b

# Função de subtração
def subtracao(a, b):
    return a - b

# Função de multiplicação
def multiplicacao(a, b):
    return a * b

# Função de divisão
def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

# Função de resto
def resto(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a % b

# Função de potência
def potencia(a, b):
    return a ** b

# Função de raiz quadrada
def raiz(a):
    if a < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
    return a ** 0.5

# Função de fatorial
def fatorial(a):
    if a < 0 or int(a) != a:
        raise ValueError("Fatorial só está definido para números inteiros não negativos.")
    resultado = 1
    for i in range(2, int(a) + 1):
        resultado *= i
    return resultado

# Funções trigonométricas
def seno(x):
    # Implementação simples usando série de Taylor (precisa de mais precisão para grandes valores de x)
    x_rad = x % 360
    x_rad = x_rad * (math.pi / 180)
    seno = 0
    for n in range(10):
        termo = ((-1) ** n) * (x_rad ** (2 * n + 1)) / fatorial(2 * n + 1)
        seno += termo
    return seno

def cosseno(x):
    # Implementação simples usando série de Taylor (precisa de mais precisão para grandes valores de x)
    x_rad = x % 360
    x_rad = x_rad * (math.pi / 180)
    cosseno = 0
    for n in range(10):
        termo = ((-1) ** n) * (x_rad ** (2 * n)) / fatorial(2 * n)
        cosseno += termo
    return cosseno

def tangente(x):
    return seno(x) / cosseno(x)

def logaritmo(a, base=10):
    if a <= 0 or base <= 0:
        raise ValueError("Logaritmo não definido para valores menores ou iguais a zero.")
    return math.log(a, base)