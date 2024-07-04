#1
print('Hello world')
#2
print("Mary's cosmetics")
#3
print('신씨가 소리를 질렀다. "도둑이야"')
#4
print('c:\windows')
#5
print("안녕하세요.\n만나서\t\t반갑습니다.")
#6
print("오늘은","일요일")
#7
print('naver','kakao','sk','samsung',sep=";")
#8
print('naver','kakao','sk','samsung',sep="/")
#9
print("first", end=""); print("second")
#10
print(5/3)
#11
삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)
#12
시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print(시가총액,type(시가총액))
print(현재가,type(현재가))
print(PER,type(PER))
#13
s = 'Hello'
t = 'Python'
print(s+'!', t)
#14
print(2+2*3)
#15
a = 132
print(type(a))
#16
num_str = '720' ##이해가 어렵다.
num_int = int(num_str)
print(num_int, type(num_int))
#17
num = 100
result = str(num)
print(result, type(result))
#18
data = 15.79
data = float(data)
print(data, type(data))
#19
year = "2020"
print(int(year)-3)  # 2017
print(int(year)-2)  # 2018
print(int(year)-1)  # 2019
#20
월 = 48584
총금액 = 월 * 36
print(총금액)
#21
letters = 'python'
print(letters[0],letters[2])
#22
license_plate = '24가 2210'
print(license_plate[-4:])
#23
string = "홀짝홀짝홀짝"
print(string[0::2])
#24
string = "PYTHON"
print(string[::-1])
#25
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-"," ")
print(phone_number1)
#26
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-","")
print(phone_number1)
#27
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])
#28
#lang[0] = 'p'
#print(lang) #ERROR
#29
#메서드
#30
#메서드
#31
a = '3'
b = '4'
print(a+b)
#32
print("Hi" * 3)
#33
print('-' * 80)
#34
t1 = 'python'
t2 = 'java'
print(t1,t2,t1,t2,t1,t2,t1,t2)
#35
name1 = '김민수'
age1 = 10
name2 = '이철회'
age2 = 13
print("이름: %s 나이: %d" % (name1,age1))
print("이름: %s 나이: %d" % (name2,age2))
#36
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))
#37
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")
#38
상장주식수 = '5,969,782,550'
컴마제거 = 상장주식수.replace(',','')
타입변환 = int(컴마제거)
print(타입변환, type(컴마제거))
#39
분기 = '2020/03(E) (IFRS연결)'
print(분기[:7])
#40
#메서드
#41
#메서드
#42
#메서드
#43
#메서드
#44
#메서드
#45
#메서드
#46
#메서드
#47
#메서드
#48
#메서드
#49
#메서드
#50
#메서드
#51
movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
#52
movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
movie_rank.append("배트맨")
print(movie_rank)
#53
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)
#54
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del movie_rank[3]
print(movie_rank)
#55
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[2]
del movie_rank[2]
print(movie_rank)
#56
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)
#57
nums = [1, 2, 3, 4, 5, 6, 7]
print("max: ", max(nums))
print("min: ", min(nums))
#58
nums = [1, 2, 3, 4, 5]
average = sum(nums) / len(nums)
print(average)
#59
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))
#60
nums = [1, 2, 3, 4, 5]
average = sum(nums) / len(nums)
print(average)
#61
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])
#62
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[0::2])
#63
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[1::2])
#64
nums = [1,2,3,4,5]
print(nums[::-1])
#65
interest = ['삼성전자', 'LG전자', 'naver']
print(interest[0::2])
#66
#메서드
#67
#메서드
#68
#메서드
#69
#메서드
#70
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)
#71
my_variable =()
print(type(my_variable))
#72
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
#73
my_tuple = (1)
print(type (my_tuple))
#74
# tuple은 데이터를 변경 없다.
#75
# t = 1, 2, 3, 4
# 타입은 튜플(tuple)
#76
#t = ('a', 'b', 'c')
#t[0] = 'A' # 튜플은 값 변경이 안됨 
t = ('A', 'b', 'c')
print(t)
#77
interest = ('삼성전자', 'LG전자', 'SK Hynix')
data = list(interest)
print(type(data))
#78
interest = ['삼성전자', 'LG전자', 'SK Hynix']
data = tuple(interest)
print(type(data))
#79
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
# apple banana cake
#80
data = range(2,100,2)
data = tuple(data)
print(data)