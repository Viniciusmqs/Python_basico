def calcular_digito(cpf_parcial, pesos):
    soma = sum(int(cpf_parcial[i]) * pesos[i] for i in range(len(cpf_parcial)))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

def cpf(n, d):
    n_str = str(n)
    d_str = str(d)
    
    #Se o resto for menor que 2, o segundo dígito verificador será 0.
    #Se o resto for maior ou igual a 2, o segundo dígito verificador será 11 - resto.
    
    dv1 = calcular_digito(n_str, pesos=range(10, 1, -1))
    cpf_completo = n_str + str(dv1)

    dv2 = calcular_digito(cpf_completo, pesos=range(11, 1, -1))

    return d_str == f"{dv1}{dv2}"

print(cpf(345702159, 71))