'''
개요: input() 함수
작성자: 진상영
작성일: 2021.03.15
내용: 표준입력장치(키보드)로부터 값 입력받을 때 사용
- 입력된 모든값은 문자열
'''

# name = input('이름을 입력하세요>>>')
# age = input('나이를 입력하세요>>>')
#
# print('입력된 이름은 {}입니다.'.format(name)) # format()메소드 이용 출력
# print('입력된 나이는 {}살입니다.'.format(age))
#
# print('입력된 이름은 %s입니다.' % name) # %연산자 이용 출력
# print('입력된 나이는 %s살입니다.' % age)
#
# price = 5000
# n = int(input('할부 개월 입력>>>')) # 문자열을 정수형으로 형변환
# print('매달 내는 돈은 {}원입니다'.format(price//n))
# print(type(n))

# 두개 이상의 입력값을 받고자 하는 경우
# a, b = input().split() # split()메소드: 공백을 기준으로 문자열 분리 저장 리스트 반환
# a1 = int(a)
# b1 = int(b)
# print(type(a), type(b))
# print(a1+b1)

x, y = input(), input()
num1 = int(x)
num2 = int(y)
print(num1+num2)
print(num1-num2)