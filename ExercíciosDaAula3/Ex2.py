def formatar_data(dia=1, mes=1, ano=2020):
    return f"{dia:02d}/{mes:02d}/{ano}"

print(formatar_data(dia=5, mes=10, ano=2023))  # Saída: 05/10/2023
print(formatar_data(mes=12, dia=25, ano=2020))  # Saída: 25/12/2020
print(formatar_data(ano=1999, dia=31, mes=7))   # Saída: 31/07/1999
print(formatar_data())
    
     