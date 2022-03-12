# Creando tuplas en python 
estudiantes=('juan','pablo')
print(estudiantes)

#estudiantes.append('marta')
#print(estudiantes)

for estudiante in estudiantes:
    print(estudiante)

# convertir tupla en lista 
listaEstudiantes = list(estudiantes)
print(listaEstudiantes)
listaEstudiantes.append("Juanpa")
tuplaEstudiantes = tuple(listaEstudiantes)
print(tuplaEstudiantes)