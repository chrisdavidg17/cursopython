Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('Por favor Ingrese su edad')
Por favor Ingrese su edad
>>> edad = input()
33
>>> print('Por favor ingrese su peso')
Por favor ingrese su peso
>>> peso = input()
80
>>> print('Por favor ingrese su altura')
Por favor ingrese su altura
>>> 186
186
>>> altura = input()
186
>>> imc = peso/(altura**)
SyntaxError: invalid syntax
>>> imc = peso/altura*altura
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    imc = peso/altura*altura
TypeError: unsupported operand type(s) for /: 'str' and 'str'
>>> peso1 = int(peso)
>>> altura1 = int(altura)
>>> imc = peso/altura*altura
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    imc = peso/altura*altura
TypeError: unsupported operand type(s) for /: 'str' and 'str'
>>> imc = peso1/altura1**2
>>> print ('Su Imc es: ' + imc)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print ('Su Imc es: ' + imc)
TypeError: can only concatenate str (not "float") to str
>>> print ('Su imc es: ', imc)
Su imc es:  0.002312406058503873
