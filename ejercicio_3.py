'''
Problema 3. Intersección y unión de conjuntos
Escribe un programa que permita al usuario crear dos conjuntos de números
enteros. Luego, el programa debe calcular y mostrar:
1. La intersección de ambos conjuntos (elementos comunes).
2. La unión de ambos conjuntos (todos los elementos sin duplicados).
3. La diferencia simétrica (elementos que están en uno u otro conjunto,
pero no en ambos).
'''

conjunto1 = []
conjunto2 = []
interseccion = []
union = []
diferencia_simetrica = []
i = 1
while i != 0:
    i = (int(input("Introduzca un número distinto de 0 para agregar al conjunto1: ")))
    if (i != 0):
        conjunto1.append(i)
    print("Si introduce el número 0 terminará de añadir números al conjunto1")
i = 1
while i != 0:
    i = (int(input("Introduzca un número distinto de 0 para agregar al conjunto2: ")))
    if (i != 0):
        conjunto2.append(i)
    print("Si introduce el número 0 terminará de añadir números al conjunto2")
print(f"conjunto1 --> {conjunto1}")
print(f"conjunto2 --> {conjunto2}")

for a in conjunto1:
    if a in conjunto2:
        interseccion.append(a)
    else:
        diferencia_simetrica.append(a)
    union.append(a)

for b in conjunto2:
    if b not in union:
        union.append(b)
    if b not in conjunto1:
        diferencia_simetrica.append(b)


print(f"interseccion--> {interseccion}")
print(f"unión --> {union}")
print(f"diferencia simétrica --> {diferencia_simetrica}")

