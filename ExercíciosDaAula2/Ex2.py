num = input("Digite um numero com no mínimo 4 e no máximo 6 digitos: ")


while (len(num) < 4 or len(num) > 6):
    num = input("Digite um numero com no mínimo 4 e no máximo 6 digitos: ")


soma = 0   
for x in num:
    soma += int(x)


soma %= 10


if len(num) == 4:
    print (f"00{num}-{soma}")
elif len(num) == 5:
    print (f"0{num}-{soma}")
else:
    print(f"{num}-{soma}")
