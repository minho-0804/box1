# ---------------------------------------------------
# 구구단 전제 출력 => 중첩 For ==> For 1개로
# % 계산하고 남은 나머지
# // 계산한 숫자
# ----------------------------------------------------
for d in range(2,10):
    print()
    for n in range(1,10):
        print(f'단{d} * {n} = {d*n:>2}', end='')

for d in range(20, 100):
    if d % 10 == 0:
        print(f'----{d//10}단----')
    else:
        print(f'{(d//10):>0} * {(d%10)} = {(d//10)*(d%10)}')

# ---------------------------------------------------
## 구구단 옆으로 출력 => 
## 2 * 1 = 2   3 * 1 = 3   4 * 1 = 4 
## 2 * 2 = 4   3 * 2 = 6   4 * 2 = 8
##
## 6 * 1 = 6
## 6 * 2 = 12
# ----------------------------------------------------
# i=0

# for i in range(2, 10):
#     print(i)
#     for j in range(1, 10):
#         print(f'{i} * {j} = {i*j},')


# for i in range(2,10):
#     for j in range(1, 10):
#         print(f'{i} * {j} = {i*j}', end='    ')

# for i in range(1,10):
#     for j in range(2,10):
#         print(f'{j} * {i} = {j*i:2}', end='    ')
#     print()

# for i in range(1,10):
#     for j in range(2,6):
#         print(f'{j} * {i} = {j*i:2}', end='    ')
#     print()

for i in range(1,10):                                 # i라는 원소에 (1~9까지 대입)
    for j in range(2,6):                              # j라는 원소에 (2~6까지 대입)
        print(f'{j} * {i} = {j*i:2}', end='    ')     # jXi= 예): 2X1=2 ~ 5X9=45
    print()                                           # 출력
print()                                           # 이때까지 한 작업을 위아래로 나누기 위한 줄바꿈
for i in range(1,10):                                 # 위에 작업을 똑같이 반복(2x)
    for j in range(6,10):                             
        print(f'{j} * {i} = {j*i:2}', end='    ')
    print() 