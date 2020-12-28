Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name="Archana"
>>> name=name.upper()
>>> print(name)
ARCHANA
>>> print(name.lower())
archana
>>> print(name[0])
A
>>> print(name[5])
N
>>> print(name[9])
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(name[9])
IndexError: string index out of range
>>> print(name[0:5])
ARCHA
>>> print(name[:4])
ARCH
>>> print(name[1:6])
RCHAN
>>> print(name[-2])
N
>>> print(name)
ARCHANA
>>> 2>8
False
>>> 3<8
True
>>> 3=3
SyntaxError: cannot assign to literal
>>> 3=3.0
SyntaxError: cannot assign to literal
>>> a=7
>>> b=5
>>> a+b
12
>>> a>b
True
>>> a=b
>>> print(a)
5
>>> 