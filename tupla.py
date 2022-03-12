#convertir la tupla(50,45,20,30,40,87) en una lista que solo tenga numeros mayores 40   
numeros=(50,45,20,30,40,87)

listaNumeros=[]

for i in range(len(numeros)):
    if numeros[i]>40:
        listaNumeros.append(numeros[i])
print(listaNumeros)