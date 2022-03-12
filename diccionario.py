estudiante={
    'nombre':'Juan',
    'edad':34,
    'futbolista':True
}
#acceder a todas las llaves o atributos del diccionario
print(estudiante)
#acceder a solo un atributo o llave del diccionario
print(estudiante['nombre'])

#recorrer un diccionario y obtener sus valores
for valor in estudiante.values():
    print(valor)