def anual ():
    print('Ingres un año:')
    year = input()
    print('Cuantos dias tiene el ', year, '?')
    dias = input()
    dias1 = int (dias)
    if dias1 == 365 or dias1  == 366:
        bis = dias1 % 2
        if bis == 0:
            print ("El año ", year, 'es biciesto')
        else:
            print ('El año', year, 'es normal')
    else:
        print('No es un numero valido')

anual()