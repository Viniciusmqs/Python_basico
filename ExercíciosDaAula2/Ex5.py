def criptografar(numero):
    d1 = int(numero[0])
    d2 = int(numero[1])
    d3 = int(numero[2])
    d4 = int(numero[3])


    d1 = (d1 + 7) % 10
    d2 = (d2 + 7) % 10
    d3 = (d3 + 7) % 10
    d4 = (d4 + 7) % 10


    temp = d1 
    d1 = d3
    d3 = temp


    temp = d2
    d2 = d4
    d4 = temp


    return str(d1) + str(d2) + str(d3) + str(d4)


numero = input("Digite um número de 4 dígitos para criptografar: ")


while len(numero) != 4:
    numero = input("Digite um número de 4 dígitos para criptografar: ")


numero_criptografado = criptografar(numero)
print(f"Número criptografado: {numero_criptografado}")


def descriptografar(numero_criptografado):
    d1 = int(numero_criptografado[0])
    d2 = int(numero_criptografado[1])
    d3 = int(numero_criptografado[2])
    d4 = int(numero_criptografado[3])


    temp = d1
    d1 = d3
    d3 = temp


    temp = d2
    d2 = d4
    d4 = temp


    d1 = (d1 - 7) % 10
    d2 = (d2 - 7) % 10
    d3 = (d3 - 7) % 10
    d4 = (d4 - 7) % 10


    return str(d1) + str(d2) + str(d3) + str(d4)


numero_criptografado = input("Digite um número de 4 dígitos criptografado para descriptografar: ")


while len(numero_criptografado) != 4:
    numero_criptografado = input("Digite um número de 4 dígitos criptografado para descriptografar: ")


numero_original = descriptografar(numero_criptografado)
print(f"Número descriptografado: {numero_original}")
