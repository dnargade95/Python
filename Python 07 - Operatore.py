
# Operatores in python - Arithmatic 

a = 10
b = 20
print(a+b)
print(a-b)
print(a*b)
print(a/b)

30
-10
200
0.5

a = 10
b = 20
print(a**b)
100000000000000000000

a = 10
b = 20
print(a%b)
10


# Relational Operator 

a = 10
b = 20
print(a>b)
False

a = 10
b = 20
print(a<b)

True

a = 10
b = 20
print(a<=b)

True

a = 10
b = 20
print(a>=b)
False

a = 20
b = 20
print(a == b)

a = 20
b = 20
print(a != b)
False


a = 10
b = 20
c = 30

print(a>b and b>c)

False

a = 10
b = 20
c = 30

print(a<b and b>c)
False

a = 10
b = 20
c = 30

print(a<b or b>c)
True


a =[10,20,30,40]
print( 10 in a)

True

a =[10,20,30,40]
print( 100 in a)
False

a =[10,20,30,40]
print( 100 not in a)
True



a =[10,20,30,40]
print( 100 not in a)
True

>>> 10 + 20
30
>>> 20/2
10.0
>>> 20**2
400
>>> 20*2
40
>>>

>>> 20>30 and 30>40
False
>>> 10<20 and 20<30
True
>>> 10<20 or 20>40
True
>>> 10 == 10
True
>>> 10!= 10
False
>>>

>>> 10 not != 10
  File "<python-input-11>", line 1
    10 not != 10
           ^^
SyntaxError: invalid syntax
>>> 10 not 10
  File "<python-input-12>", line 1
    10 not 10
           ^^
SyntaxError: invalid syntax
>>> 10 not = 10
  File "<python-input-13>", line 1
    10 not = 10
           ^
SyntaxError: invalid syntax
>>>

>>> a=[10,20,30,40,50,60]
>>> 20 in a
True
>>> print(20 in a)
True
>>> 100 un a
  File "<python-input-17>", line 1
    100 un a
        ^^
SyntaxError: invalid syntax
>>> 100 in a
False
>>> 100 not inn a
  File "<python-input-19>", line 1
    100 not inn a
            ^^^
SyntaxError: invalid syntax
>>> 100 not in a
True
>>>

>>> a=range(100)
>>> for c in a
  File "<python-input-22>", line 1
    for c in a
              ^
SyntaxError: expected ':'
>>> for c in a:
...     print(c)
...
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
>>>

>>> values = range(10,20)
>>> fro c in value:
  File "<python-input-26>", line 1
    fro c in value:
        ^
SyntaxError: invalid syntax
>>> for c in values:
...     print(c)
...
10
11
12
13
14
15
16
17
18
19
>>> print(values[4])
14
>>>

