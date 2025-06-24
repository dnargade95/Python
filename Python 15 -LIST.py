"""
----------LIST DATA STRUCTURE--------------

lIST IS PREDEFINED CLASS IN PYTHON 
PYTON CLASS CONTAINS METHODS


a = [10,20,30,40,50,60,70,80,90,100]

b = [10,20,"Dnyaneshwar",True,0.003]

print(b)
print(type(b))

print(a)

c = [12,12,12,13,13,13,14,14,16]
print(c,"- Duplicates allowed")


c[0]=1000
print(c)

c[0,1,2]=1000,2000,3000
print(c)

TypeError: list indices must be integers or slices, not tuple


c = [12,12,12,13,13,13,14,14,16] 
print(c[5])
print(c[0:8])


for values in c:
	print(values)

print(len(c))

d = [10,2,30,40,50,60,70,80,920]
print(c+d)
print(c*5)

print(dir(list()))

 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']



a=[10,20,30,40,50,60,70,80,90]
print(len(a))

print(a.count(10))


a.append("Rajababu")
print(a)

a.insert(5,"mera babu")
print(a)

a.remove(10)
print(a)

a.reverse()
print(a)

a.sort()
TypeError: '<' not supported between instances of 'int' and 'str'



a=[1,54,2165,1,6541,6516541,1654,1234,32156,16,156,13,6,1,651,321,31,31,3211,321,321,23,123,123,121,2,13,1,2,322,3]
print(a)
b=a.sort()
print(b)



numbers = [3, 1, 4, 2]
print(numbers.sort())

a=[1,20,30,40,50,60,70,80,90]
listcompr = [values + 100 for values in a]
print(listcompr)

"""














