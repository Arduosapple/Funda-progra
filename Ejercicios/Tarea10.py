
import numpy as np

print("=== 1. Crear arrays ===")

lista = [1, 2, 3, 4, 5]
arr1 = np.array(lista)
print("Array desde lista:", arr1)

zeros = np.zeros(5)
print("Matriz de ceros:", zeros)

unos = np.ones(5)
print("Matriz de unos:", unos)

print("\n=== 2. Operaciones básicas ===")
arr2 = np.array([5, 4, 3, 2, 1])
print("arr1:", arr1)
print("arr2:", arr2)

suma = arr1 + arr2
print("Suma:", suma)

multiplicacion = arr1 * arr2
print("Multiplicación:", multiplicacion)

print("\n=== 3. Broadcasting ===")
broadcast1 = arr1 + 10
print("Broadcast con escalar:", broadcast1)


fila = np.array([1, 2, 3])
columna = np.array([[10], [20], [30]])
broadcast2 = fila + columna
print("Broadcast entre 1D y 2D:\n", broadcast2)

print("\n=== 4. Indexación y segmentación ===")

segmento = arr1[1:4]
print("Segmento [1:4]:", segmento)


mas_de_2 = arr1[arr1 > 2]
print("Elementos > 2:", mas_de_2)

indices = [0, 2, 4]
valores = arr1[indices]
print("Elementos en índices 0, 2 y 4:", valores)

print("\n=== 5. Concatenación y división ===")

concatenado = np.concatenate((arr1, arr2))
print("Concatenado:", concatenado)

dividido = np.split(concatenado, 2)
print("Dividido en 2 partes:")
for i, parte in enumerate(dividido):
    print(f"Parte {i+1}:", parte)

print("\n=== ¡Listo! ===")


np.random.seed(42)
consumo = np.random.randint(50, 200, size=(10, 7))

consumo_hogar5_viernes = consumo[4, 4]  
print("1. Consumo del hogar 5 el viernes:", consumo_hogar5_viernes)
consumo_ultimos3_domingo = consumo[-3:, 6]
print("2. Consumo de los últimos 3 hogares el domingo:", consumo_ultimos3_domingo)
fines_de_semana = consumo[:, 5:7]
promedio_fds = np.mean(fines_de_semana)
print("3. Promedio de consumo en fines de semana:", promedio_fds)
desviaciones = np.std(consumo, axis=0)
dia_max_std = np.argmax(desviaciones)
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
print(f"4. Día con mayor desviación estándar: {dias[dia_max_std]} ({desviaciones[dia_max_std]:.2f})")
print("   Esto indica que ese día hay mayor variabilidad en el consumo entre hogares.")
suma_por_hogar = np.sum(consumo, axis=1)
indices_menor = np.argsort(suma_por_hogar)[:3]
print("5. 3 hogares con menor consumo total:")
for idx in indices_menor:
    print(f"   Hogar {idx} - Total: {suma_por_hogar[idx]}")
hogar3_original = consumo[2]
hogar3_incrementado = hogar3_original * 1.10
total_nuevo_hogar3 = np.sum(hogar3_incrementado)
print(f"6. Nuevo consumo total del hogar 3 con +10% diario: {total_nuevo_hogar3:.2f}")


