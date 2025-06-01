def encontrar_lideres(lista):
    lideres = []
    max_derecha = float('-inf')
    for numero in reversed(lista):
        if numero > max_derecha:
            lideres.append(numero)
            max_derecha = numero
    lideres.reverse()
    return lideres

entrada = input()
numeros = list(map(int, entrada.split()))
lideres = encontrar_lideres(numeros)
print(lideres)
