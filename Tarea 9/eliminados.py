def eliminar_duplicados(lista):
    vistos = set()
    resultado = []
    for num in lista:
        if num not in vistos:
            resultado.append(num)
            vistos.add(num)
    return resultado

# Ejemplo de uso
lista_original = [4, 2, 4, 3, 2, 1, 3, 5]
lista_sin_duplicados = eliminar_duplicados(lista_original)
print(lista_sin_duplicados)  # Salida: [4, 2, 3, 1, 5]
