
# flow controll in pyton 

code 1]
a = int(input("inter your value"))
if a >9:
	print("jai ho")
else:
	print("jai ho bhi ho")


# Good morning Program

# wish with name according to time 

#name = input("please enter your name :-")

#time = input("what is time ? :- ")

time = range(0,25)
timenew = list(time)

for values in time:
	print(values)


time = int(input("enter your age"))

if time > 60:
	print("old man")
elif time<= 60 and time >= 45:
	print("middle age man")
elif time<45 and time>=25:
	print("you are men")
elif time<25 and time>=16:
	print("you are young boy")
elif time<16:
	print("you are child")
else:
	print("mar ja bhai")


D:\Python_Daniel>py "Python 12 - flow control.py"
enter your age32
you are men

D:\Python_Daniel>py "Python 12 - flow control.py"
enter your age10
you are child

D:\Python_Daniel>py "Python 12 - flow control.py"
enter your age70
old man

D:\Python_Daniel>py "Python 12 - flow control.py"
enter your agehh
Traceback (most recent call last):
  File "D:\Python_Daniel\Python 12 - flow control.py", line 31, in <module>
    time = int(input("enter your age"))
ValueError: invalid literal for int() with base 10: 'hh'

D:\Python_Daniel>py "Python 12 - flow control.py"
enter your age55
middle age man



































































