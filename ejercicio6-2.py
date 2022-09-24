class alumno:
    nota = 0
    def __init__(self,nombre, nota):
        print('Hola, ', nombre)
        self.nota = nota

    def final(self):
        nota = self.nota
        if nota >= 3 and nota <= 5:
            print ('Felicitaciones, aprobaste')
            print ('Tu nota final fue: ', nota)
        elif nota < 3:
            print ('No aprobaste')
            print ('Tu nota final fue: ', nota)
        else:
            print ('Numero no valido, debe ser un numero entre 0 y 5')


a = alumno('Christian', 4)
a.final()