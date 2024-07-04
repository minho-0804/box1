## --------------------------------------------------
## ==> 1줄로 조건식을 축약 : 조건부표현식
## --------------------------------------------------
## [실습] 임의의 숫자가 5의 배수 여부 결과를 출력하세요.

# num=7

# if num%5 == 0:
#     print('5의 배수')
# else:
#     print('5의 배수 아님')

# if num%5 == 0: print('5의 배수') else print('5의 배수 아님')

## [실습] 문자열을 입력 받아서 문자열의 원소 개수를 저장
## - 단 원소 개수가 0이면 None 저장
## - (1) 입력받기 input()
## - (2) 원소/요소 개수 파악 len()
## - (3) 원소/요소 개수 저장 단, 0인 경우 None 저장하기

# x=input()
# # result=len(x)
# if len(data):
#     result=len(data)
# else:
#     result=None

# result =len(data) if len(data) else None
# print(f'{data}의 원소.요소 개수 : {result}개')

## [실습] 연산자(4칙연산자 : +,-,*,/) 와 숫자 2개 입력 받기
## - 입력된 연산자에 따라 계산 결과 저장
## - 예) 입력 : + 10 3  출력 13
x=input('숫자와 4칙연산을 입력하시오').split()

x[1]=int(x[1])
x[2]=int(x[2])

if x[0]== '+':
    result = x[1]+ x[2]
elif x[0]== '-':
    result = x[1]- x[2]
elif x[0]== '*':
    result = x[1]* x[2]
elif x[0]== '/':
    result = x[1]/ x[2]
else:
    print('답을 찾을수 없습니다.')

print(result)



