# loop in python

       2 types of loop 
                   1 ->> for loop
                   2 ->> while loop 



a = [10,20,30,40,50,60,70,80,90,100]

for values in a:
	print(values)

D:\Python_Daniel>py "Python 13 - flow control - loop.py"
10
20
30
40
50
60
70
80
90
100

D:\Python_Daniel>


b =range(0,1000)
for values in b:
	print(values)




# passward is passward code

a = int(input("inter your passward here"))
while a != 123456789:
	print("please inter correct password")
	a = int(input("inter your passward here"))
	a == 123456789
print("welcome to program ")

  D:\Python_Daniel>py "Python 13 - flow control - loop.py"
inter your passward here100
please inter correct password
inter your passward here123456789
welcome to program

D:\Python_Daniel>





b=[1,2,3,4,5,6,7,8,9]
for values in b:
	if values==4:
		continue
	print(values)


1
2
3
5
6
7
8
9

D:\Python_Daniel>


b=[1,2,3,4,5,6,7,8,9]

for values in b:
	if values in b[0:3]:
		continue
	print(values)

  D:\Python_Daniel>py "Python 13 - flow control - loop.py"
4
5
6
7
8
9
