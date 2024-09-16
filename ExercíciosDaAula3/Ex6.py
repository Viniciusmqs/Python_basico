def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
if __name__ == '__main__':
    n = int(input("Digite o valor de n (n>= 3):"))
    if n < 3:
        print("n deve ser um número maior ou igual a 3.")
    else:
        print(f"O {n}-ésimo termo da série de Fibonacci é: {fibonacci(n)}")