python: 

Data Types: 1. int 
            2. float
            3. complex
            4. bool
            5. str
            6. byte
            7. bytearray
            8. range
            9. list
            10. tuple
            11. set
            12. frozenset
            13. dict
            14. None
in pyhton everthing is an object 
Python provide some in build fucations 
  1. print()     
  2. type() ---> to fin the type of the object 
  3. id() ---> to find the address of object 
        
Identifiers in the python: 
variable name , method name , class name by default considerd as identifiers.
Rules: 
1. a to z , A to Z . 0-9, _ ,
2. it should not start with digit
3. Case senstive
4. We cannot use Reserved word as identifiers
5. No length

1. If Any identifiers start with _ symbol it is private
2. if any identifiers start with __ symbol it is strogly private 
3. If any identifiers start with __tdered__ it is language specific 

these are the reserved words 
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 
'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 
'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 
'try', 'while', 'with', 'yield']


Data Types: 
1. int :
number with out decimal points 
10 20 30 1000033443
ex: 
>>> a=10
>>> type(a)
<class 'int'>

in python 3 long data type is not avaliable.

for the int data type we can represent values 4 Types
1. Decimal form   (Base 2)
   0 to 9
   a=345467474
2  Binary form (Base 2)
    0 to 1
    a=0b1111
    a=oB1111
    by default which number contains 0b,0B then only is considred as binary data type
3. Octal form (Base 7)
   0 to 7 
   a=0o777 
   Answer=511
4. Hexa Form (Base 16)
   0 to 9 , a to f 
   a=0XBeef ...> it is accpeted
   a=0XBeer ...> it is not accepted

By default we used to get only decimal form as a output

The speciality of python is no need to define the data type.

Float data type:
f=1334.57 allowed 
f=0X124 not allowed 
f=1.3e3 is allowed.
when we need decimal value. we use float value.

Complex data type: 

(a+bj)
a= Real part
b= Imaginary part 
j= Square root -1

>>> x=10+20j
>>> type(x)
<class 'complex'>
>>> x
(10+20j)

bool: 
   it is used to represent bullig value
   True and False
>>> a,b=10,20
>>> c=a>b
>>> c
False
b='true' in this type only it is stated as string

str:
    'ashok' then it is a string. we can use "" also.

slice:
>>> a='ashok'
>>> a[2]
'h'
>>> a[45]
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a[45]
IndexError: string index out of range
>>> a[1:3]
'sh'
>>> a*2
'ashkashk'
