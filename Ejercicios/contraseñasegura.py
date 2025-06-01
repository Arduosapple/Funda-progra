'''
Clase:        Fundamentos de la programacion
Tema:         Bloque condicional
Ejercicio:    Contraseña segura
Descripción:  solicitar una cadena de texto y comprobar si esa seria una contraseña segura o no

Autor:        Ever Montes
Fecha:        2025-05-15
Estado:       [ Terminado ]
'''
# Solicita la contraseña
contraseña = input("Ingrese una contraseña: ")

# Verificaciones
tiene_longitud = len(contraseña) >= 8
tiene_numero = any(c.isdigit() for c in contraseña)
tiene_mayuscula = any(c.isupper() for c in contraseña)

# Evaluación
if tiene_longitud and tiene_numero and tiene_mayuscula:
    print("Contraseña segura")
else:
    print("Contraseña no segura")
