'''
개요: 사용자함수
작성자: 진상영
작성일: 2021.03.23
내용: 사용자가 직접 만든 함수
함수용어: 함수정의, 인수, 매개변수, 반환값, 함수호출
1) 함수정의 및 호출
def 함수이름(매개변수):
    본문
    return 반환값
함수이름(인수)
'''

# def welcome(a):
#     print('Hello Python')
#     print('Nice to meet you')
# welcome('인수를 매개변수에 전달한 값')

# def introduce(name, age):
#     print('내 이름은 {}이고, 나이는 {}살입니다.'.format(name, age))
# introduce('진상영','49')

# def show(*args): # 가변매개변수: 매개변수 앞 애스터리크(*), 입력된 인수들을 튜플로 처리
#     for item in args:
#         print(item)
# show('Python', 'Happy', 'Birthday')

# def greet(message='안녕하세요'): # 기본(디폴트) 매개변수
#     print(message)
# greet('반갑습니다')
# greet()

# def greet(name, message='안녕하세요'):
#     print('{}님 {}'.format(name, message))
# greet('김철수')

# def adder(*args):
#     print('{}의 합은 {}입니다.'.format(args, sum(args)))
# adder(1,2)
# adder(1,2,3)
# adder(1,2,3,4)

# def address():
#     str = '우편번호 12345\n'
#     str += '부산시 해운대구 해운대로 469번길'
#     return str
# print(address())

# def calculator(*args): # 가변매개변수 -> 튜플로 처리
#     return sum(args), sum(args)/len(args), max(args), min(args)
# a, b, c, d = calculator(1,2,3,4,5)
# print('합계: {}'.format(a))
# print('평균: {}'.format(b))
# print('최대값: {}'.format(c))
# print('최소값: {}'.format(d))
# print()
# result = calculator(1,2,3,4,5)
# print('합계: ', result[0], sep='')
# print('합계: ', result[1], sep='')
# print('합계: ', result[2], sep='')
# print('합계: ', result[3], sep='')

# def charge(energy):
#     if energy < 0:
#         print('0보다 작은 에너지는 충전할 수 없습니다.')
#         return # 함수종료
#     print('에너지가 충전되었습니다.')
# charge(1)
# charge(-1)

# def coffee_machine(money, pick):
#     print('{}원에 {}를 선택하셨습니다.'.format(money, pick))
#     menu = {
#         '아메리카노':1000,
#         '카페라떼':1500,
#         '카푸치노':2000
#     }
#     if pick not in menu:
#         print('{}는 판매하지 않습니다.'.format(pick))
#         return money, '없는 메뉴'
#     elif menu[pick] > money:
#         print('{}는 {}원입니다.'.format(pick, menu[pick]))
#         return money, '금액 부족'
#     else:
#         return money-menu[pick], pick
#
# order = input('커피를 선택하세요.(아메리카노, 카페라떼, 카푸치노)>>> ')
# pay = int(input('얼마를 내시나요?>>> '))
#
# change, coffee = coffee_machine(pay, order)
# print('잔돈은 {}원, 선택하신 커피는 {}입니다.'.format(change, coffee))