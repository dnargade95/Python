"""

------------  string ---------------------------------

a="dnyaneshwar"
b='dnyaneshwar'
c='''dnyaneshwar'''
print("my name is :- ",a,b,c)

indexing and slicing in string 

print(a[7])

print(a[0:7])

String is imutable

a="dnyaneshwar"
a[0]="m"
print(a)
  File "D:\Python_Daniel\Python 14 -String.py", line 19, in <module>
    a[0]="m"
  
TypeError: 'str' object does not support item assignment



we can access string using index, slicing and for loop


a="dnyaneshwar"
print(a[0])





a="dnyaneshwar"
print(a[0:5])

for values in a:
	print(values)

  File "D:\Python_Daniel\Python 14 -String.py", line 19, in <module>
dnyan

D:\Python_Daniel>py "Python 14 -String.py"
D:\Python_Daniel\Python 14 -String.py:21: SyntaxWarning: invalid escape sequence '\P'
  File "D:\Python_Daniel\Python 14 -String.py", line 19, in <module>
dnyan
d
n
y
a
n
e
s
h
w
a
r


a = "Dnyaneshwar"
b = "argade"
print(len((a+"  "+b)*3))
print(len(a))

in and not in  operator in string works

a="dnyaneshwar argade"
print("dnyaneshwar" in a)

a= "dnyaneshwar"
print(a.upper())

b ="DNYANESHWAR"
print(b.lower())

c = "              DNYANESHWAR             "
print(c.strip())

d="ram" * 100
print(d)
print(d.count("r"))
e = d.replace("r","sh")
print(e)
f = d.split(",")
print(f)

STRING PREDEFINED CLASS HAVE BEWLOW METHODS
- UPPER
- LOWER
- COUNT
- SPLITE
- STRIP
- REPLACE

"""