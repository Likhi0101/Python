Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 21:52:07) [MSC v.1937 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 10
b = 10
print ( a is b)
True
a = 10
b = 5
print ( a is b)
False
if 3<7:
    print("hi")

    
hi
if 3:
    print("hi")

    
hi
if -45:
    print("hi")

    
hi
if 0:
    print("hi")

    
a = int(input())
if a:
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a = int(input())
ValueError: invalid literal for int() with base 10: 'if a:'
a = int(input())
if a: 
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a = int(input())
ValueError: invalid literal for int() with base 10: 'if a: '
if a:
    print("hi")

    
hi
a=int(input("enter a number"))
enter a number 5
if a:
    print("hi")
... 
...     
hi
>>> a=int(input("enter a number"))
enter a number 6
>>> if a:
...     print("hi")
... else:
...     print("bye")
... 
...     
hi
>>> a=int(input("enter a number"))
enter a number 0
>>> if a:
...     print("hi")
... else:
...     print("bye")
... 
...     
bye
>>> a = int(input("enter a number"))
enter a number 2
>>> b = int(input("enter the length"))
enter the length 3
>>> c = int(input("enter the breadth"))
enter the breadth 4
>>> result = b*c
>>> print(result)
12
>>> result = pi*a*a
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    result = pi*a*a
NameError: name 'pi' is not defined
>>> result = 3.14*a*a
>>> 
>>> print(result)
12.56
