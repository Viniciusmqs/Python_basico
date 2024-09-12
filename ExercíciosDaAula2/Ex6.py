n = int(input("Digite um valor inteiro e positivo para N: "))


while n <= 0:
    n = int(input("Digite um valor inteiro e positivo para N: "))


soma = 1
fatorial = 1


for i in range(2, n + 1):
    fatorial *= i
    soma += 1 / fatorial


print(f"A soma E é: {soma}")