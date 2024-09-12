def converte_temperatura(valor, de, para):
    match (de, para):
        case ('celsius', 'fahrenheit'):
            return (valor * 9/5) + 32
        case ('fahrenheit', 'celsius'):
            return (valor - 32) * 5/9
        case ('celsius', 'kelvin'):
            return valor + 273.15
        case ('kelvin', 'celsius'):
            return valor - 273.15
        case ('fahrenheit', 'kelvin'):
            return (valor - 32) * 5/9 + 273.15
        case ('kelvin', 'fahrenheit'):
            return (valor - 273.15) * 9/5 + 32
        case _:
            return "Conversão inválida"


def converte_distancia(valor, de, para):
    match (de, para):
        case ('metros', 'quilômetros'):
            return valor / 1000
        case ('quilômetros', 'metros'):
            return valor * 1000
        case ('metros', 'milhas'):
            return valor / 1609.34
        case ('milhas', 'metros'):
            return valor * 1609.34
        case ('quilômetros', 'milhas'):
            return valor / 1.60934
        case ('milhas', 'quilometros'):
            return valor * 1.60934
        case _:
            return "Conversão inválida"


def converte_tempo(valor, de, para):
    match (de, para):
        case ('segundos', 'minutos'):
            return valor / 60
        case ('minutos', 'segundos'):
            return valor * 60
        case ('minutos', 'horas'):
            return valor / 60
        case ('horas', 'minutos'):
            return valor * 60
        case ('segundos', 'horas'):
            return valor / 3600
        case ('horas', 'segundos'):
            return valor * 3600
        case _:
            return "Conversão inválida"


def transforma(tipo, valor, de, para):
    match tipo:
        case 'a':
            return converte_temperatura(valor, de, para)
        case 'b':
            return converte_distancia(valor, de, para)
        case 'c':
            return converte_tempo(valor, de, para)
        case _:
            return "Tipo de conversão inválido"


print("Tipos de conversão:")
print("A: temperatura (Celsius, Fahrenheit, Kelvin)")
print("B: distância (Metros, Quilometros, Milhas)")
print("C: tempo (Segundos, Minutos, Horas)")


tipo = input("Informe o tipo de conversão (A, B ou C): ")
valor = float(input("Informe o valor a ser convertido: "))
de = input("Informe a unidade de origem: ")
para = input("Informe a unidade de destino: ")


resultado = transforma(tipo, valor, de, para)


print(f"Resultado: {resultado}")