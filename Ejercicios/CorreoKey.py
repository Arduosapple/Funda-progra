'''
Clase:        Fundamentos de la programacion
Tema:         Variables, tipos, entradas y salidas
Ejercicio:    Generador de correo Key
Descripción:  generar el correo para todos los nuevos estudiantes

Autor:        Ever Montes
Fecha:        2025-05-15
Estado:       [ Terminado ]
'''
# Solicita el nombre completo
nombre_completo = input("Ingrese su nombre completo (2 nombres y 2 apellidos): ")

# Divide el nombre por espacios
partes = nombre_completo.strip().lower().split()

# Extrae primer nombre y primer apellido
primer_nombre = partes[0]
primer_apellido = partes[2]

# Construye el correo
correo = f"{primer_nombre}.{primer_apellido}@keyinstitute.edu.sv"

# Muestra el resultado
print(f"\nEl correo que se debe asignar al usuario ingresado es: {correo}")
