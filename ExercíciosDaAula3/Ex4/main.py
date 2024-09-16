from operacoes import soma, subtracao, multiplicacao, divisao, resto, potencia, raiz, fatorial, seno, cosseno, tangente, logaritmo

def aplicar_operacao(num1=None, num2=None, operacao=None):
    if operacao is None:
        raise ValueError("A operação deve ser fornecida.")
    
    if num1 is not None and num2 is not None:
        return operacao(num1, num2)
    elif num1 is not None:
        return operacao(num1)
    else:
        raise ValueError("Pelo menos um número deve ser fornecido.")

# Testando a função aplicar_operacao com várias operações
print("Soma: ", aplicar_operacao(5, 3, soma))           # Saída: 8
print("Subtração: ", aplicar_operacao(5, 3, subtracao)) # Saída: 2
print("Multiplicação: ", aplicar_operacao(5, 3, multiplicacao)) # Saída: 15
print("Divisão: ", aplicar_operacao(6, 3, divisao))     # Saída: 2.0
print("Resto: ", aplicar_operacao(7, 3, resto))         # Saída: 1
print("Potência: ", aplicar_operacao(2, 3, potencia))   # Saída: 8
print("Raiz quadrada: ", aplicar_operacao(9, operacao=raiz))  # Saída: 3.0
print("Fatorial: ", aplicar_operacao(5, operacao=fatorial))  # Saída: 120
print("Seno: ", aplicar_operacao(30, operacao=seno))    # Saída: 0.49999 (aproximado)
print("Cosseno: ", aplicar_operacao(60, operacao=cosseno))  # Saída: 0.49999 (aproximado)
print("Tangente: ", aplicar_operacao(45, operacao=tangente)) # Saída: 1.0
print("Logaritmo: ", aplicar_operacao(100, 10, logaritmo))  # Saída: 2.0