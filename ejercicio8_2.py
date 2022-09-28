import pickle
class vehiculo():
    marca = ''
    modelo = 0

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

#v1 = vehiculo ('Mazda', 2021)


#f = open ('clases.bin', 'wb')
#pickle.dump (v1, f)
#f.close ()

f = open ('clases.bin', 'rb')
mazda = pickle.load(f)
f.close()

print(type(mazda))