#Problema 2. Frecuencia de palabras en un texto.
#Escribe un programa que pida al usuario ingresar una frase o párrafo. Luego, el
#programa debe contar cuántas veces aparece cada palabra en el texto y mostrar
#las palabras junto con su frecuencia.
#Requisitos:
#1. Eliminar los signos de puntuación y conver&r todas las palabras a minúsculas para evitar diferencias.
#2. Usar un diccionario donde la clave sea la palabra y el valor sea su frecuencia.
#3. Mostrar las palabras y sus frecuencias de forma ordenada por la palabra.

#"ESTE es el texto que quiero METER y que, además, estoy probando. Este texto es para el ejercicio que tengo que hacer"
parrafo = input("Introduce un parrafo: ")
print(parrafo)
parrafo_sin_signos_minuscula = parrafo.replace(",","").replace(".","").lower()
print(parrafo_sin_signos_minuscula)
diccionario = parrafo_sin_signos_minuscula.split()
diccionario.sort()
print(diccionario)
dic = {diccionario[0] : diccionario.count(diccionario[0])}
for a in diccionario:
    dic[a] = diccionario.count(a)
print("Aquí sacamos el resultado:")
for a in dic.items():
    print(a)

