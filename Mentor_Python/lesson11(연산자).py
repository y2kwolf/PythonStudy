'''
개요: 연산자와 우선순위
작성자: 진상영
작성일: 2021.03.15
내용:
1) 연산자
- 산술연산자 : +, -, *, **(지수승), /, //(몫), %(나머지)
- (복합)대입연산자 : =, +=, -=, *=, /=, //=, %=
- 관계연산자 : >, <=, <, <=, ==, !=
- 논리연산자 : and, or, not
- 비트연산자 : &, |, ^, ~, <<, >>
- 기타연산자 : 참 if 조건식 else 거짓, in, +, *

2) 연산우선순위
- () > ** > *,/,//,% > +,- > =, 복합대입연산자

'''

# 산술연산자
# a = 7
# b = 2
# print('{} + {} = {}'.format(a, b, a+b))
# print('{} - {} = {}'.format(a, b, a-b))
# print('{} * {} = {}'.format(a, b, a*b))
# print('{} ** {} = {}'.format(a, b, a**b))
# print('{} / {} = {}'.format(a, b, a/b))
# print('{} // {} = {}'.format(a, b, a//b))
# print('{} % {} = {}'.format(a, b, a%b))

# 대입연산자
# piggy_bank = 0
# money = int(input('저금통에 얼마를 저금하시겠습니까?'))
# piggy_bank += money
# print('저금통에 용돈 {}원을 넣었습니다.'.format(money))
# print('지금 저금통에는 {}원이 있습니다'.format(piggy_bank))

# snack = int(input('저금통에서 얼마를 빼 쓰시겠습니까?'))
# piggy_bank -= snack
# print('저금통에서 스낵 구입비 {}원을 뺐습니다.'.format(snack))
# print('지금 저금통에는 {}원이 있습니다.'.format(piggy_bank))

# 관계연산자
# a = 15
# print('{}>10:{}'.format(a, a>10))
# print('{}<10:{}'.format(a, a<10))
# print('{}>=10:{}'.format(a, a>=10))
# print('{}<=10:{}'.format(a, a<=10))
# print('{}==10:{}'.format(a, a==10))
# print('{}!=10:{}'.format(a, a!=10))

# 논리연산자
# a = 10
# b = 0
# print('{}>0 and {}>0:{}'.format(a, b, a>5 and b>5))
# print('{}>0 or {}>0:{}'.format(a, b, a>5 or b>5))
# print('not {}:{}'.format(a, not a))
# print('not {}:{}'.format(b, not b))

# 비트연산자
# a = 10 # 이진수변환 0000 1010
# b = 70 # 이진수변환 0100 0110
# print('a&b:{}'.format(a&b)) # 비트 AND 입력이 모두 1이면 1, 아니면 0
# print('a|b:{}'.format(a|b)) # 비트 OR 입력중 하나로도 1이면 1, 아니면 0
# print('a^b:{}'.format(a^b)) # 비트 XOR 입력이 서로 다르면 1, 아니면 0
# print('~a:{}'.format(~a)) # 비트 NOT 입력이 0이면 1, 1이면 0
# print('a<<1:{}'.format(a<<1)) # 비트 왼쪽 SHIFT 비트단위로 왼쪽으로 N비트 이동
# print('a>>1:{}'.format(a>>1)) # 비트 오른쪽 SHIFT 비트단위로 오른쪽으로 N비트 이동

# 시퀀스연산자
# tree = '#'
# space = ' '
# print(space*4 + tree*1)
# print(space*3 + tree*3)
# print(space*2 + tree*5)
# print(space*1 + tree*7)
# print(space*0 + tree*9)

# 기타연산자 : 맴버십연산자(in, not in) / 조건연산자(삼항연산자: x if C else y)
# a = 49
# b = 46
# result = (a-b) if (a>=b) else (b-a)
# print('{}과 {}의 차이는 {}입니다.'.format(a, b, result))