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

