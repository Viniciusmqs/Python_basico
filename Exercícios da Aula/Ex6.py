total_segundos = int(input("Insira o tempo em segundos: "))

dias = total_segundos // 86400
horas = (total_segundos % 86400) // 3600
minutos = (total_segundos % 3600) // 60
segundos = total_segundos % 60

print(f"{dias} dias, {horas} horas, {minutos} minutos, {segundos} segundos")