# ----------------------------------------------------------------------
# 입력 & 출력 실습
# ----------------------------------------------------------------------
# [실숩1] 데이터 저장 및 변수 생성 그리고 출력
# - 생년월일
# - 띠 (용,범...)
# - 혈액형
# - 출력형태
#   나는0000년 0월 00일 000띠입니다.
#   혈액형은 ____ 0형 입니다
# ----------------------------------------------------------------------
year='2005'
month='8'
day='4'
c_zodiac="닭띠"
blood='O'

print('나는',year,'년',month,'월',day,'일',c_zodiac,'입니다')
print('혈액형은',blood,'입니다')

# [실숩2] 입력 받은 데이터 저장 단, 파일로 저장
# - 좋아하는 계절
# - 좋아하는 나라
# - 여행가고 싶은 나라
# ----------------------------------------------------------------------

season=input('좋아하는 계절')
country=input('좋아하는 나라')
country2=input('여행가고 싶은 나라')

FILENAME='info.txt'
f=open(FILENAME,mode='w',encoding='utf-8')

# f.write(season)
# f.write('\n')  # 줄바꿈 문자
# f.write(nara)
# f.write('\n')   #줄바꿈 문자
# f write(nara2)
print(f'좋아하는 계절   :{season}',file=f)
print(f'좋아하는 나라   :{country}',file=f)
print(f'여행가고 싶은 나라   :{country2}',file=f,end='')

f.close()