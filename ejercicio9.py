lista = []
i = 0

for i in range (5):
    pais = input('Ingrese un pais \n')
    lista.append(pais)
    i + 1

lista1 = set(lista)
orden = sorted(lista1)
print (orden)
