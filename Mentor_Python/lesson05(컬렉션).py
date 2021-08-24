'''
개요: 컬렉션(collection) - 자료구조
작성자: 진상영
작성일: 2021.02.27
내용: 리스트, 튜플, 세트, 딕셔너리
1) 리스트(list)         list()     a = [1,2,3]      인덱싱, 슬라이싱 가능(시퀀스자료형)   가변객체,   인덱스반환(index), 추가(append,insert,extend), 수정, 반환삭제(pop)가능
2) 튜플(tuple)         tuple()     a = (1,2,3)     인덱싱, 슬라이싱 가능(시퀀스자료형)    불변객체(읽기전용)
3) 세트,집합(set)            set()      a = {1,2,3}     인덱싱, 슬라이싱 불가(비시퀀스자료형)  중복값 저장 불가능, 추가(add), 삭제(remove,discard)
4) 딕셔너리(dictionary) dict()     a = {'age':25}   인덱싱, 슬라이싱 불가(비시퀀스자료형)  추가(setdefault), 수정(update), 삭제(pop) 키(key):값(value) 로 관리, 동일한 키값을 가질수 없음

* 시퀀스형(순서) 객체 - 문자열, 리스트, 튜플, range
* 비시퀀스형(비순서) 객체 - 세트, 딕셔너리
* 언팩킹 - 리스트나 튜플 같은 컬렉션의 요소를 여러개의 변수에 나누어 담는 것
'''

# 1) 리스트(list)
# member = ["진상영", 49, "부산시 해운대구", "010-2746-8762", 174.5] # C, Java의 배열은 하나의 자료형만 저장 가능
# print(member)
# print(member[2])
# print(member[3:5])

# a = int(member[2])
# print(type(a))
# # ※ 언팩킹
# member = ['진상영', '010-2746-8762', 'B형']
# name, tel, blood = member
# print(name, tel, blood)

# print('이름의 위치:', member.index('진상영'))
# member.append("B형")              # append() 메소드는 마지막 요소 추가
# print(member)
# member.insert(0, 1)               # insert() 메소드는 인덱스 지정 추가
# print(member)
# member.extend(['69Kg', '자녀2명']) # extend() 메소드는 리스트에 리스트 추가
# print(member)
# member.pop()                      # 인덱스 미지정 시 마지막 요소 제거
# print(member)
# member.pop(1)                     # 인덱스 지정 시 선택 요소 제거
# print(member)

# """ type() 함수 자료형 확인 """
# a = [1,2,3]
# b = (1,2,3)
# c = {1,2,3}
# d = {'age':25}
# e = 2
# f = 3.14
# g = 'python'
# h = True
# print(type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h))


# 2) 튜플(tuple)
# myTuple1 = ()
# myTuple2 = (1, 'python', 3.14)
# myTuple3 = ('software',)
# myTuple4 = ('software') # 하나의 항목은 튜플로 미인정
# myTuple5 = 1, 2, 'python'
# myTuple6 = ('문자열', (1, 2, 3), [4, 5, 6])
# print(myTuple6)
# a, b, c = myTuple6
# print(a, b, c)
#
# print(myTuple6[0])
# print(myTuple6[0][1])
# print(myTuple6[2][2])
# print(myTuple6[0:2])
# print(myTuple6[1:])
# print(myTuple6[:-1])
# myTuple6[2][0] = 7 # 튜플 객체는 불변, 가변 시퀀스객체 내 항목 수정 가능
# print(myTuple6)

# myTuple = (1, 2, 3)
# yourTuple = (4, 5, 6)
# ourTuple = myTuple + yourTuple
# print(ourTuple)
# print(myTuple * 3)
# print(1 in myTuple)
# print(4 in myTuple)
# print(1 not in myTuple)
# print(myTuple.count(1))
# print(myTuple.index(3))

# 3) 집합(set) - 중복X, 순서X, 가변객체X
# li = list(set([1, 1, 2, 2, 3, 3]))
# print(li, type(li))

# s = {} # 빈집합이 아닌 딕셔너리형
# print(s, type(s))
# s = set() # 빈집합
# print(s, type(s))

s = {1, 2, 3}
s.add(4)
print(s)
# s.remove(5) # 5값 제거, 값이 없을 경우 KeyError 오류발생
# s.discard(5) # 5값 제거, 값이 없어도 오류 미발생
# s.remove(4)
# print(s)


# 4) 딕셔너리(dictionary)
# dic = {'a':'apple', 'b':'banana'}

# print(dic)
# print(type(dic))

# print(dic['a']) # 인덱스 대신 키 사용하면 값 반환
# print(dic['b'])

# dic['c'] = 'melon' # 새로운 데이터 추가
# print(dic)
# dic.setdefault('d','strawberry') # 새로운 데이터 추가
# print(dic)
# dic.update(d='orange') # 키값 수정
# print(dic)
# dic.update(e='peach') # 존재하지 않는 키값 수정시 새로운 데이터 추가
# print(dic)
# dic.pop('e') # e키값 삭제
# print(dic)