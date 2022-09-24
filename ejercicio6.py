class Vehiculo():
    color = "Negro"
    Ruedas = 4
    Puertas = 5

class coche(Vehiculo):
    cilindrada = 2500
    velocidad = 250

a = coche()
print ('El coche es de color: ', a.color, ', tiene ', a.Puertas, ' y obviamente ', a.Ruedas, ' llantas')
print ('Este coche al tener una cilindrada de ', a.cilindrada, ' cc, puede alcanzar hasta ', a.velocidad, ' km/h.')