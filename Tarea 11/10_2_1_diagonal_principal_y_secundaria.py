
"""

'''
Clase:        Clase 10
Tema:         Matrices
Ejercicio:    10.2.1. Diagonal principal y secundaria
Descripción:  Dada una matriz cuadrada ingresada por el
              usuario, crea dos listas, una con los
              elementos de la diagonal principal y la otra
              con los elementos de la diagonal
              secundaria.

Autor:        Ever Montes
Fecha:        2025-06-17
Estado:       [ Terminado ]
"""


def diagonales_matriz():
    N = int(input("Introduce el tamaño de la matriz: "))

    matriz = []
    for i in range(N):
        fila = list(map(int, input(f"Fila {i + 1}: ").split(',')))
        matriz.append(fila)


    diagonal_principal = []
    diagonal_secundaria = []

    for i in range(N):
        diagonal_principal.append(matriz[i][i])
        diagonal_secundaria.append(matriz[i][N - 1 - i])
    print("Diagonal principal:", diagonal_principal)
    print("Diagonal secundaria:", diagonal_secundaria)
diagonales_matriz()