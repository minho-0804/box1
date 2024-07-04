# -------------------------------------------------------------
# Dict 전용 함수 즉, 메서드
# -> keys(),values(),items()
# --------------------------------------------------------------
person={'name':'홍길동','age':'10'}

#[메서드 - 값 읽어오는 메서드 get(key, default)]-------------
# - key에 해당하는 value가 없다면 default값을 반환
print(person['name'])
# print(person['gender']) #keyerror

print(person.get('name','몰라'))
print(person.get('gender','없음'))
print(person.get('gender'))

# [메서드 - 키와 값 추가 메서드] ---------------------------
person['gender']='남'

# [메서드 - 수정 및 추가 업데이트 메서드 update(k==v)]-----------------
person['gender']='여'

person.update(gender='어린이')
print(person)

person.update(gender='어린이',job='학생')
print(person)

person.update({'phone':'010','birth':'240101'})
print(person)

## (**{'weight':'100','height':'170'})
person.update(**{'weight':'100','height':'170'})
print(person)



msg='Hello Good Luck'
# alpha=set(msg)
# save={}
# print(alpha)
# for m in alpha:
#     print(m,msg.count(m))
#     save[m]=msg.count(m)

# print(save)