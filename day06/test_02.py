# ------------------------------------------------------
# [실습] 10번 숫자 데이터를 입력을 받습니다.
#        - 숫자 데이터를 모두 더해서 합계가 30이상이되면
#          10번 입력 받았더라도 종료해주세요.
# ------------------------------------------------------
# num=input()

# for n in num:
#     print()
#     for d in range(1,30,):
#         if 30>=d:
#             print(f'{n} + {d} = {n+d}')


total=0
for cnt in range(10):
    data=int(input('숫자 입력 : '))
    total=total+data
    if total>=30: break

