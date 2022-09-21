Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> hello
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    hello
NameError: name 'hello' is not defined. Did you mean: 'help'?
>>> print ("Hello")
Hello
>>> git status
SyntaxError: invalid syntax
>>> a = ("Hello World")
>>> print a
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print (a)
Hello World
