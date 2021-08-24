'''
개요: 반복문2
작성자: 진상영
작성일: 2021.03.17
내용:
1) for문
for 변수 in 반복가능객체:
    반복실행문

2) 반복가능객체
: 시퀀스자료형 (문자열'', 리스트[], 튜플())
: 비시퀀스자료형 (세트{}, 딕셔너리{})
'''

# pwd = input('비밀번호를 입력하세요(단, 숫자와 영문 반드시 포함 8자리 이상)>>> ')
#
# ch_count = 0
# num_count = 0
#
# for ch in pwd:
#     if ch.isalpha(): # a.isalpha() a가 문자인 경우 True
#         ch_count += 1
#     elif ch.isnumeric(): # a.isnumeric() a가 숫자인 경우 True
#         num_count += 1
#
# print('문자 {}개'.format(ch_count))
# print('숫자 {}개'.format(num_count))
#
# if ch_count > 0 and num_count > 0 and (ch_count + num_count) >= 8:
#     print('가능한 비밀번호입니다.')
# else:
#     print('불가능한 비밀번호입니다.')

## 시퀀스 자료형과 for문
# # 1)for문과 리스트
# for item in ['가위', '바위', '보']: # for 변수 in [리스트]
#     print(item)
#
# a = [n*2 for n in [1,2,3,4,5] if n%2 ==1] # 표현식 for 변수 in 반복가능객체 if 조건식
# print(a)

# # 2) for문과 튜플
# four_season = ('Spring', 'Summer', 'Autumn', 'Winter')
# for season in four_season:
#     print(season)

# # 3) for문과 range()함수, range(초기값,종료값,증감값)
# for n in range(1,11):
#     print(n)

# for n in range(10): # 10번의 반복 생성 코드
#     print('Hello')

# dan = int(input('출력할 구구단을 입력하세요>>> '))
# for n in range(1,10):
#     print('{}x{}={}'.format(dan, n, dan*n))

## 비시퀀스 자료형과 for문
# # 1) for문과 세트
# for item in {'가위', '바위', '보'}: # 실행때마다 다른 결과
#     print(item)

# # 2) for문과 딕셔너리
# person = {
#     'name' : '진상영',
#     'age' : 49
#     }
# for item in person:
#     print(item)
#
# for key in person:
#     print(person[key]) # 인덱스 대신 키 사용하면 값 반환
#
# for key in person:
#     print(person.get(key))
# eng_dict = {
#     'sun' : '태양',
#     'moon' : '달',
#     'star' : '별',
#     'space' : '우주'
# }
# for word in eng_dict:
#     print('{}의 뜻: {}'.format(word, eng_dict[word]))

# for문 한줄표현
v = list(range(10))
print(v)
for i in v: # 기본표현식
    print(i)
# [print(i,type(i)) for i in v] # 한줄표현식