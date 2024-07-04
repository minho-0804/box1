#16.1
for i in range(100):
    print('hello, world')

for i in range(100):
    print('Hello, world!', i)

for i in range(5,12):
    print('Hello, world!', i)

for i in range(0, 10, 2):
    print('Hello, world!', i)

for i in range(10,0,-1):
    print('Hello, world!', i)

for i in reversed(range(10)):     
    print('Hello, world!', i)

#16.2
# count= int(input('반복할 횟수를 입력하세요'))
# for a in range(count):
#     print('Hello, world!', a)

#16.3
a=[10,20,30,40,50]
for i in a:     
    print(i)

fruits=('apple', 'orange', 'grape')
for fruit in fruits:
    print(fruit)

for letter in 'python':
    print(letter, end='')


for letter in reversed('python'):
    print(letter, end='')
# 연습문제
x = [49, -17, 25, 102, 8, 62, 21]
for i in x:
    print(i*10,end=' ')

print()

# 심사문제
num = int(input())
for r in range(1,10):
    print(f'{num} * {r} = {num*r}')