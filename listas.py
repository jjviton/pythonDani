lista = [1,"Dos", 3]  #un conjunto de datos ordenados

buscar = 0

if buscar in lista:
    print (lista.index(buscar))
else:
    print ("No esta en la lista")

iterable = [1,2,3,4]
lista.extend(iterable)

print (lista.pop(1))

lista.remove(3)

lista.reverse()

print (lista.count(1))

print (lista[0])
