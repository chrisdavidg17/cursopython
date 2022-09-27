import time

hora = time.strftime('%H')
minutos = time.strftime('%M')

print (hora, ':', minutos)

if int(hora)>= 18:
    print ('Es hora de irse a casa')
else:
    print ('Faltan {} horas y {} mintutos para irte a casa'.format(18-int(hora), 59-int(minutos)))