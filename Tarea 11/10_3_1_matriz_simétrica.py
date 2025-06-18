
'''
Clase:        Clase 10
Tema:         Matrices
Ejercicio:    10.3.1. Matriz simétrica
Descripción:  Dada una matriz cuadrada ingresada por el
              usuario, comprueba si la matriz cuadrada es
              simétrica respecto a su diagonal principal.

Autor:        Ever Montes
Fecha:        2025-06-17
Estado:       [ Terminado ]
'''

matriz_final = []
n = int(input("Ingrese la dimensión de la matriz: "))

def simetrica(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[j][i]:
                return False
        return True

for m in range(n):
    fila = list(map(int, input().split(',')))
    matriz_final.append(fila)


if simetrica(matriz_final):
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")