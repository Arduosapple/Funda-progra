'''
Clase:        Fundamentos de la programacion
Tema:         Bloque condicional
Ejercicio:    El numero magico
Descripción:  verificar su¿i un numero es divisible entre 7 pero no por 5 y eso se conoce como numero magico

Autor:        Ever Montes
Fecha:        2025-05-15
Estado:       [ Terminado ]
'''
# Solicita al usuario un número entero
numero = int(input("Ingresa un número entero: "))

# Condiciones usando booleanos
es_divisible_7 = numero % 7 == 0
es_divisible_5 = numero % 5 == 0

# Verifica si es mágico: divisible por 7 y NO divisible por 5
es_magico = es_divisible_7 and not es_divisible_5

# Muestra el resultado
if es_magico:
    print(f"El número {numero} ES un número mágico.")
else:
    print(f"El número {numero} NO es un número mágico.")
