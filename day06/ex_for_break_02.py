# --------------------------------------------------------------
# 제어문 -반복문과 break
# - 중첩 반복문일 경우의 break는가장 가까이 있는 부분만 종료
# --------------------------------------------------------------
## [실습] 단의 숫자만큼만 구구단을 출력하세여.
## 2 * 1 = 2 2 * 2 = 4
## 3 * 1 = 3 3 * 2 = 6 3 * 3 = 9
## 4 * 1 = 4 4 * 2 = 8 4 * 3 = 12 4 * 4 = 16
# ----------------------------------------------------------------
dan=int(input('출력 원하는 단 입력 : '))
isbreak=False
    
for d in range(2,10):
    print(f'\n[{d}단]', end=' ')
    for n in range(1,10):
        print(f'{d} * {n} = {d*n:<2}', end=' ')
        if n==d:
            isbreak=True
            break
    if isbreak: break


for d in range(2,dan+1):
    print(f'\n[{d}단]', end=' ')
    for n in range(1,d+1):
        print(f'{d} * {n} = {d*n:<2}', end=' ')