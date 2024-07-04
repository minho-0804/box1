# pg.102
a = [38,21,53,62,19]
print(a)
# pg.103
person = ['james', 17, 175.3, True]
print(person)

a = []
print(a)
b=list()
print(b)

# range=(10)
#print(range(0, 10))
#pg.104

#b = list(range(5, 12))
print(b)

# c = list(range(-4, 10, 2))
# print(c)

# d = list(range(10, 0, -1))
# print(d)

# pg.105

a = (38, 21, 53, 62, 19)
print(a)

a = 38, 21, 53, 62, 19
print(a)

person = ('james', 17, 175.3, True)
person
# pg.106
# (38)
# print(38)
(38, )
38,

# a = tuple(range(10))
print(a)

# b = tuple(range(5, 12))
print(b)
# pg.107
# c = tuple(range(-4, 10, 2))
# print(c)

a = [1,2,3]
tuple(a)

b = (4,5,6)
list(b)

list('Hello')
tuple('Hello')
# pg.108
a,b,c = [1,2,3]
print(a,b,c)

d,e,f = [4,5,6]
print(d,e,f)

x = [1,2,3]
a,b,c = x
print(a,b,c)

y = [4,5,6]
d,e,f, = y
print(d,e,f)

input().split()
# 10 20
x = input().split()
# 10 20

# a, b = x
print(a,b)

a = [] #a
a = [10,20,30] #c
# a = list(range(10,31,10)) #d

# pg.109

a = 10, 20, 30, False, 'Hello' # b
a = (False, 'Python') # c
a = tuple([10,20,30]) # e

# a = list(range(-10, 10, 3)) #d
print(tuple)
# a = list(range(5, -10, 2))

# pg.110

# datas=tuple(range(-10,10,2))
# tuple(range(-10,10,3))

# pg.112
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(30 in a)
print(100 in a)

a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(100 not in a)
print(30 not in a)

print(43 in(38,76,43,62,19))
print(1 in range(10))
print('P' in 'Hello, Python')

a = [0, 10, 20, 30]
b = [9, 8, 7, 6]
print(a+b)

# pg.114
# print('Hello, '+10)
print([0,10,20,30] * 3)

# pg.115

print(list(range(0,5,2))*3)
print(tuple(range(0,5,2))*3)
print('Hello'*3)

# pg.116

a = 0, 10, 20, 30, 40, 50, 60, 70, 80, 90
print(len(a))

b = (38, 76, 43, 62, 19)
print(len(b))

print(len(range(0,10,2)))

# pg.118
a = [38, 21, 53, 62, 19]
print(a[0])
print(a[2])
print(a[4])

# pg.119
r = range(0,10,2)
print(r[2])

hello = 'Hello, world'
print(hello[7])

a =[38, 21, 53, 62, 19]
print(a)

# pg.120

a = [38, 21, 53, 62, 19]
print(a[-1])
print(a[-5])

b = (38, 21, 53, 62, 19)
print(b[-1])

r = range(0,10,2)
print(r[-3])

# pg.121

hello = 'Hello, world!'
print(hello[-4])

#a = [38, 21, 53, 62, 19]
#print(a[5])

# pg.122

a = [38, 21, 53, 62, 19]
print(len(a))
print(a[5])
print(a[4])
print(a[len(a)])
print(a[len(a)-1])

# pg.123

a = [0, 0, 0, 0, 0]
(a[0]) =38
(a[1]) =21
(a[2]) =53
(a[3]) =62
(a[4]) =19
print(a)
print(a[0])
print(a[4])
# print(a[5])
b = (0,0,0,0,0)
(b[0]) = 38

# pg.124

# r = range(0,10,2)
# (r[0]) = 3

hello = 'Hello, world!'
hello[0] = 'A'

a = [38,21,53,62,19]
del a [2]
print(a)

b = [38,21,53,62,19]
del [b] 2
print(b)

# pg.125

r = range(0,10,2)
del r[2]
print(r)

hello = "Hello, world!"
del hello[2]
print(hello)

a = [0,10,20,30,40,50,60,70,80,90]
a[0:4]
a[0:10]
# pg.126
a = [0,10,20,30,40,50,60,70,80,90]
a[1:1]
a[1:2]

# pg.127

a[4:1]

a = [0,10,20,30,40,50,60,70,80,90]
a[2:8:3]
# pg.128
a[2:9:3]

a = [0,10,20,30,40,50,60,70,80,90]
a[:7]
# pg.129

a[7:]
a[:]

a = [0,10,20,30,40,50,60,70,80,90]
a[7:2]
# pg.130
a[7::2]
a[::2]
a[::]
# pg.131
a = [0,10,20,30,40,50,60,70,80,90]
a[5:1:-1]
a[::-1]

a = [0,10,20,30,40,50,60,70,80,90]
a[0:len(a)]
a[:len(a)]
# pg.132

b = [0,10,20,30,40,50,60,70,80,90]
b[4:7]
b[4:]
b[:7:2]

r = range(10)
print(r)

# pg.133
r[4:7]
r[4:]
r[:7:2]

print(list(r[:7:2]))

hello = "Hello, world!"
hello[2:9]
hello[2:]
hello[:9:2]

# pg.134

range(10)[slice(4,7,2)]
range(10).__getitem__(slice(4,7,2))

a = [0,10,20,30,40,50,60,70,80,90]
s = slice(4,7)
print(a[s])
print(r=range(10))
print(r[s])
hello = 'Hello, world!'
print(hello[s])

# pg.135

a = [0,10,20,30,40,50,60,70,80,90]
a[2:5] = ['a', 'b', 'c']
print(a)

a = [0,10,20,30,40,50,60,70,80,90]
a[2:5] = ['a']
print(a)

# pg.136

a = [0,10,20,30,40,50,60,70,80,90]
a[2:5] = ['a', 'b', 'c', 'd', 'e']
print(a)

a = [0,10,20,30,40,50,60,70,80,90]
a[2:8:2] = ['a', 'b', 'c']
print(a)

# pg.137

a = [0,10,20,30,40,50,60,70,80,90]
a[2:8:2] = ['a', 'b']
print(a)

b = [0,10,20,30,40,50,60,70,80,90]
b[2:5] = ['a', 'b', 'c']
print(b)

r = range(10)
print(r[2:5] = range(0, 3))

hello = 'Hello, world!'
print(hello[7:13] = 'Python')

# pg.138

a = [0,10,20,30,40,50,60,70,80,90]
del a[2:5]
print(a)

a = [0,10,20,30,40,50,60,70,80,90]
del a[2:8:2]
print(a)

# pg.139

b = [0,10,20,30,40,50,60,70,80,90]
del b[2:5]
print(b)

r = range(10)
print(r[2:5] = range(0, 3))

hello = 'Hello, world!'
del hello[2:9]

# a,d

# pg.140

# b,d
# c,e
# a,c

year = [2011,2012,2013,2014,2015,2016,2017,2018]
population = [10249679,10195318,10143645,10103233,10022181,9930616,9857426,9838892]
print(year[25:])
print(population[-24:])

# pg.141

n = -32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2
print(n[1::2])

x = 1 2 3 4 5 6 7 8 9 10
print(x[0:8:2]end'')

# pg.142

x = list(x)
print(tuple(x[:len(x)-5]))

x = input().strip()
y = input().strip()
data1 = x[1::2]
data2 = y[::2]
print(data1 + data2)