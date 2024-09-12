import math


def calcular_raiz_quadrada(N, iteracoes):
    k = 1.0
    resultados = []
    
    for i in range(iteracoes):
        k = (k + N / k) / 2
        resultados.append(k)
    
    return resultados


N = float(input("Digite o valor de N: "))
iteracoes = 12


resultados = calcular_raiz_quadrada(N, iteracoes)


print("Iteração | Valor de k")
print("--------------------")
for i in range(iteracoes):
    print(f"{i + 1:9d} | {resultados[i]:.6f}")


raiz_quadrada = math.sqrt(N)
print(f"\nRaiz quadrada verdadeira de {N}: {raiz_quadrada:.6f}")