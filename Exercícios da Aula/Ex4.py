numero = input("Insira um número de cinco dígitos: ")

# Verifica se o número tem cinco dígitos
if len(numero) == 5 and numero.isdigit():
    print("   ".join(numero))
else:
    print("Número inválido! Insira exatamente cinco dígitos.")