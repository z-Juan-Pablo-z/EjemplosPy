numeros=[]
tamaño=5
for i in range(tamaño):
    numero=int(input("Digite un numero para la lista "))
    numeros.append(numero)
busqueda=int(input("Digite el numero de busqueda "))
if(busqueda in numeros):
    print("Si esta en la lista1 ")
    print(numeros[busqueda])
else:
    print("no se encuentra en la lista ")