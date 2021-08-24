'''
개요: 변수(Variable)
작성자: 진상영
작성일: 2021.02.27
내용: 
- 파이썬은 변수 선언 불필요, 선언시 자동 메모리공간 할당 및 저장
  -> 동적타이핑(dynamic typing)
- 변수명 규칙(식별자 명명규칙)
: 대소문자 구분
: 영문대소문자, 숫자, 밑중(_) 사용가능
: 숫자시작 불가
: 공백문자 불가
: 예약어 사용 불가
ex) 2021year, user name, $wiss, for
- 저장값의 의미를 짐작할 수 있는 변수명 사용
'''

# 변수 만들기와 값 저장
name = "진상영"            # 문자열
age = 49                  # 정수형
address = '''부산광역시 해운대구 해운대로469번길 110, 해운대자이 2차
105동 2701호'''            # multiple line 문자열
pet = None                # 자료형 미지정
height = 174.5            # 실수형

print(name, age, address, height)
print("이름: ", name)
print("나이: ", age)
print("주소: ", address)
print("체중: ", height)

# 문장(statement) 표현
num1 = 10
num2 = 20
num3 = 30
print(num1 + num2 + num3)

num4 = 10; num5 = 20; num6 = 30
print(num4 + num5 + num6)

num7, num8, num9 = 10, 20, 30
print(num7 + num8 + num9)

sum = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
sum = 1 + 2 + 3 + \
      4 + 5 + 6 + \
      7 + 8 + 9
print(sum)

tup = (1 + 2 + 3 +
      4 + 5 + 6 +
      7 + 8 + 9)
print(tup)

