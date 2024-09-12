cod = int(input("Informe o codigo entro 1 e 10: "))
while (cod < 1 or cod > 10):
    cod = int(input("Informe o codigo entro 1 e 10: "))


peso = float(input("Informe o peso em quilos: "))


codPais =  int(input("Informe o cod do pais entre 1 e 3: "))
while (codPais < 1 or codPais > 3):
    codPais =  int(input("Informe o cod do pais entre 1 e 3: "))


gramas = peso * 1000
preco = 0
if (cod >= 1 and cod <= 4):
    preco = gramas * 10
elif(cod >= 5 and cod <= 7):
    preco = gramas * 25
else:
    preco = gramas * 35


imposto = 0
match codPais:
    case 1:
        imposto = 0
    case 2:
        imposto = preco * 0.15
    case 3:
        imposto = preco * 0.25


valorTotal = preco + imposto
        
print(f"Gramas: {gramas}, Preco Total {preco}, Valor do Imposto: {imposto}, Valor Total: {valorTotal} ")