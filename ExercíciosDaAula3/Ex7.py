def calcular_estatisticas(*numeros):
    if not numeros: 
        return ValueError("A lista de números não pode estar vazia.")
    
    media = sum(numeros) / len(numeros)
    valor_maximo = max(numeros)
    valor_minimo = min(numeros)
    
    return media, valor_maximo, valor_minimo

if __name__ == "__main__":
    numeros1 = [1, 2, 3, 4, 5]
    numeros2 = [10, 20, 30, 40, 50]
    numeros3 = [5, 15, 25, 35, 45, 55]
    
    media1, maximo1, minimo1 = calcular_estatisticas(*numeros1)
    print(f"Para a lista {numeros1}: Média = {media1}, maximo1 = { maximo1}, minimo1 = {minimo1}")
    
    media2, maximo2, minimo2 = calcular_estatisticas(*numeros2)
    print(f"Para a lista {numeros2}: Média = {media2}, Máximo = {maximo2}, Mínimo = {minimo2}")
    
    media3, maximo3, minimo3 = calcular_estatisticas(*numeros3)
    print(f"Para a lista {numeros3}: Média = {media3}, Máximo = {maximo3}, Mínimo = {minimo3}")