'''
개요: 내장함수
작성자: 진상영
작성일: 2021.03.22
내용: 내장함수(built-in function) 인터프리터에서 항상 사용할 수 있는 함수
      https://docs.python.org/ko/3/library/functions.html

1) 문자열 내장 함수
- print(): 입력값 화면 출력
- input(): 입력값 받기
- chr(): 유니코드값 -> 문자 반환
- ord(): 문자 -> 유니코드값 반환
- eval(): 문자열 표현식 -> 표현식 결과값 반환
- format(): 인수 -> 문자열 반환
- str(): 인수 -> 문자열 반환

2) 숫자 내장 함수
- abs(): 절대값 반환
- divmod(): 두 인수를 나누어 몫과 나머지를 한쌍으로 결과 튜플로 반환
- float(): 숫자,문자열 -> 실수 반환
- int(): 숫자,문자열 -> 정수 반환
- max(): 인수 중 최대값 반환
- min(): 인수 중 최소값 반환
- sum(): 리스트나 튜플등 반복가능객체 합계 반환
- pow(): 두 인수의 거듭제곱 반환 (연산자 **)
- round(): 인수의 반올림값 반환 (인수1개 반올림 정수반환, 인수2개 두번째인수만큼 소숫점반환)

3) 시퀀스 내장 함수
- enumerate(): 리스트의 인덱스와 요소 출력
- range(start,stop,step): 인수값 사이의 시퀀스 자료형 생성, 범위생성자
- len(): 함수에 전달된 객체의 길이(항목수)를 반환
- sorted(): 함수에 전달된 반복가능객체 오름차순 정렬 결과 리스트 반환 (리스트, 튜플 동일)
- zip(): 여러개의 반복가능객체 -> 튜플로 묶어서 반환
- list(): 괄호안 시퀀스형 객체 인수를 리스트 변환
- tuple(): 괄호안 시퀀스형 객체 인수를 튜플 변환
'''

# 1) 문자열 내장 함수
# print(chr(65))
# print(ord('A'))
# print(eval('4+5'))
# a = format(10000, ',')
# print(a, type(a))

# expr = input('계산식을 입력하세요>>> ')
# result = eval(expr)
# print(type(result))
# # print('{}={}'.format(expr, eval(expr)))

# 2) 숫자 내장 함수
# money = int(input('당신이 가진돈을 입력하시요>>> '))
# price = int(input('빵값을 입력하시요>>> '))
# result = divmod(money, price)
# print('빵을 {}개 사고, {}원이 남았습니다.'.format(result[0], result[1])) # 튜플 요소 인덱싱
# bread, change = result
# print('빵을 {}개 사고, {}원이 남았습니다.'.format(bread, change)) # 튜플 언팩킹

# 3) 시퀀스 내장 함수
# for idx, item in enumerate(['가위', '바위', '보']): # 언팩킹
#     print(idx, item)

# a = list(range(10, 0, -1)) # 범위생성자를 리스트 자료형으로 변환, 튜플도 가능
# print(a)

# li = ['a', 'b', 'c', 'd']
# print(len(li))

# my_list = [6, 3, 1, 2, 5, 4]
# print(sorted(my_list)) # 정렬된 결과만 반환할뿐 실제 객체 정렬X
# print(my_list)
# my_list = sorted(my_list) # 정렬된 결과값을 객체 자신 전달해야 실제 정렬
# print(sorted(my_list))

# names = ['james', 'emily', 'amanda']
# scores = [60, 70, 80]
# for name, score in zip(names, scores): # 튜플 언팩킹
#     print('{}의 점수는 {}입니다.'.format(name, score))

# months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# for month, day in enumerate(months):
#     if month == 0:
#         continue
#     print('{}월 = {}일'.format(month, day))
