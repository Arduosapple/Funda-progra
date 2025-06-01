'''''''''
Clase:        Fundamentos de programacion
Tema:         Variables, tipos, entradas y salidas
Ejercicio:    Calculo de la propina
Descripcion:  Pide al usuario el total de una cuenta y el porcentaje de propina y da el total a pagar

Autor:        Ever Montes
Fecha:        2025-05-15
Estado:       [ Terminado ]
''''''''''

# Solicita datos al usuario
total_cuenta = float(input("Ingrese el total de la cuenta: $"))
porcentaje_propina = float(input("Ingrese el porcentaje de propina (por ejemplo, 10 para 10%): "))

# Calcula propina y total
propina = total_cuenta * (porcentaje_propina / 100)
total_con_propina = total_cuenta + propina

# Muestra resultados
print(f"\nTotal de la cuenta: ${total_cuenta:.2f}")
print(f"Propina: ${propina:.2f}")
print(f"Total de la cuenta con propina ({porcentaje_propina:.0f}%): ${total_con_propina:.2f}")
