"""
object of the program based on
value you put its will suggest menu
1 - idli 40 rs
2 - wada 40 rs
3 - dosa 60 rs
4 - Misal 80 rs
6 - sandwhich 100 rs
7 - Thali 120 rs

"""
ask_first = print("Kya chahiye?")
ans1 = input("Ask Menu kya hai?")
menu = ("idli ","wada ","dosa ","Misal ","sandwhich ","Thali ")
print(menu)
ans2 = input("Price kya hai?")
ask_2 = print("Paisa kitna hai?")
money_have=int(input("Put how much money you have?"))

if money_have == 0:
	print("Jaga Khali kr mere bhai.. focut ka nhi milta")

elif money_have < 40:
	print("isme kuch nhi ata mere bhai")

elif money_have >=40 and money_have<60:
	print("Bas ye ayega bhai",menu[0])
        
elif money_have >=60 and money_have<80:
	print("Bas ye ayega bhai",menu[0:2])

elif money_have >=80 and money_have<100:
	print("Bas ye ayega bhai",menu[0:3])

elif money_have >=100 and money_have<120:
	print("Bas ye ayega bhai",menu[0:4])

elif money_have >=120:
	print("Sabkuch Aap ka hai malik",menu)
else:
	print("bata jaldi")

"""
Kya chahiye?
Ask Menu kya hai? bhai menu?
('idli ', 'wada ', 'dosa ', 'Misal ', 'sandwhich ', 'Thali ')
Price kya hai?price?
Paisa kitna hai?
Put how much money you have?100
Bas ye ayega bhai ('idli ', 'wada ', 'dosa ', 'Misal ')

C:\Users\SHREE\Desktop\Python_Daniel>py "Python 11 - Hotel menu Program.py"
Kya chahiye?
Ask Menu kya hai?menu?
('idli ', 'wada ', 'dosa ', 'Misal ', 'sandwhich ', 'Thali ')
Price kya hai?price?
Paisa kitna hai?
Put how much money you have?0
Jaga Khali kr mere bhai.. focut ka nhi milta

C:\Users\SHREE\Desktop\Python_Daniel>py "Python 11 - Hotel menu Program.py"
Kya chahiye?
Ask Menu kya hai?
('idli ', 'wada ', 'dosa ', 'Misal ', 'sandwhich ', 'Thali ')
Price kya hai?
Paisa kitna hai?
Put how much money you have?150
Sabkuch Aap ka hai malik ('idli ', 'wada ', 'dosa ', 'Misal ', 'sandwhich ', 'Thali ')
"""