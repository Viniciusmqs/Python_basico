x = float(input("Digite o valor de x (em radianos): "))
termos = int(input("Digite o número de termos para a aproximação: "))


soma = 0
fatorial = 1
potenciaX = 1


for i in range(termos):
    if i > 0:
        fatorial *= (2 * i) * (2 * i - 1)
        potenciaX *= x * x


    termo = potenciaX / fatorial
    if i % 2 == 0:
        soma += termo
    else:
        soma -= termo


print(f"O valor aproximado de cos({x}) é: {soma}")
