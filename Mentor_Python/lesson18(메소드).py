'''
개요: 메소드
작성자: 진상영
작성일: 2021.03.22
내용: 특정 객체(object)가 가지고 있는 함수(function)
      https://docs.python.org/ko/3/library/stdtypes.html
1) 문자열 메소드
- format(): 인수로 변수나 값을 표시, 해당값 표시 위치에 중괄호({}) 표시방식
- count(): 문자열 내부에 포함된 특정 문자열의 개수 반환
- find() / rfind(): 문자열내 포함된 첫 특정문자 인덱스 반환 (찾는 문자열이 없는 경우 -1 반환)
- index(): 문자열내 포함된 첫 특정문자 인덱스 반환 (찾는 문자열이 없을경우 오류발생)
- upper(): 모두 대문자 반환
- lower(): 모두 소문자 반환
- capitalize(): 첫글자 대문자, 나머지 소문자 반환
- title(): 단어의 첫글자 대문자 변환
- join(): 반복가능객체 요소사이 문자열 포함 반환
- split(): 문자열 분리 저장 리스트 반환
- replace(): 문자열의 일부를 다른 문자열로 변경 반환
- lstrip(): 왼쪽 끝 불필요한 문자열 제거 반환
- rstrip(): 오른쪽 끝 불필요한 문자열 제거 반환
- strip(): 양쪽 끝 불필요한 문자열 제거 반환
- is메소드: 문자열,숫자,소문자,제목 등 다양한 값 True, False 반환
- ljust(길이) / rjust() / center(): 길이만큼 만든뒤 왼쪽/오른쪽/중앙 정렬

2) 리스트 메소드
- index(): 객체 인덱스 반환, 리턴값이 없을경우 오류
- append(): 리스트 마지막에 요소 추가
- insert(): 리스트의 지정된 특정 인덱스에 요소 추가
- extend(): 리스트에 다른 리스트나 튜플 같은 반복가능객체 추가
- sort(): 리스트 구성항목 정렬
- reverse(): 리스트 구성항목 역순정렬
- pop(): 리스트의 마지막 요소 or 지정인덱스 반환 후 삭제
- remove(): 리스트 객체 삭제
- count(): 리스트 객체 갯수 리턴
- clear(): 리스트 저장 요소 전체 삭제

3) 집합(셋트) 메소드
- add(): 집합에 객체 추가
- update(): 집합에 여러 객체 추가
- pop(): 집합의 임의의 항목 반환 후 삭제
- discard(): 집합 객체 삭제 (없어도 오류없음)
- remove(): 집합 객체 삭제 (오류발생)
- clear(): 모든 객체 삭제 빈집합 갱신
* 집합 연산
- 합집합: union() -> |
- 교집합: intersection() -> &
- 차집합: difference() -> -
- 대칭차집합: symmetric_difference() -> ^
- 부분집합: issubset() -> <=
- 포함함합: issuperset() -> >=
'''

# 1) 리스트 메소드
# print("10자리 폭 외엔쪽 정렬 '{:<10d}'".format(123))
# print("10자리 폭 오른쪽 정렬 '{:>10d}'".format(123))
# print("10자리 폭 가운데 정렬 '{:^10d}'".format(123))
#
# print("10자리 폭 외엔쪽 정렬 '{:*<10d}'".format(123))
# print("10자리 폭 오른쪽 정렬 '{:*>10d}'".format(123))
# print("10자리 폭 가운데 정렬 '{:*^10d}'".format(123))

# print("숫자 천단위 구분기호 콤마(,) 출력하기 '{:,}'".format(123456789))

# s = '내가 그린 기린 그림은 목 긴 기린 그림이고, 네가 그린 기린 그림은 목 짧은 기린 그림이다'
# print(s.count('기린'))
# print(s.count('기린', 12)) # 2번째 인수는 시작위치 인덱스(마이너스 인덱스 가능) 지정

# s = 'best of best'
# print(s.find('b'))
# print(s.rfind('b'))
# print(s.rfind('z')) # 찾는 문자열이 없는 경우 -1 반환

# print(s.index('b'))
# print(s.index('z')) # 찾는 문자열이 없는 경우 오류 발생

# s = 'welcome To the jungle'
# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.title())

# print('*'.join('python'))
# print('+'.join(['a', 'b', 'c', 'd', 'e']))
# print('-'.join({'a':'apple', 'b':'banana'}))

# s = 'Life is too short'
# print(s.split())

# s = '010-2746-8762'
# print(s.split('-'))

# s = '진상영, 49, B형, 부산광역시 해운대구'
# print(s.split(','))

# s = '010-2746-8762'
# print(s.replace('-', ''))

# s = '   wolfjin   '
# print(s.lstrip().replace(' ','*'))
# print(s.rstrip().replace(' ','*'))
# print(s.strip().replace(' ','*'))
# print(s.strip(' ').replace(' ','*'))

# while True:
#     p = input('하이픈을 포함하여 전체 주민등록번호를 입력하세요.>>> ')
#     if p.find('-') != 6:
#         print('하이픈의 위치가 잘못되었습니다.')
#         continue
#     birthday = p.split('-')[0]
#     print('생년월일은 {}년 {}월 {}일 입니다.'.format(birthday[0:2], birthday[2:4], birthday[4:6]))
#     break

# s = 'wolfjin'
# print(s.isalnum()) # 문자,숫자 판별
# print(s.isalpha()) # 문자만 판별
# print(s.isdecimal()) # 숫자만(10진수만) 판별
# print(s.isdigit()) # 숫자만 판별 ex) ⁸
# print(s.isnumeric()) # 숫자만(유니코드포함) 판별  ex) ½


# 2) 리스트 메소드
# fruit = ['apple', 'banana']
# fruit.append('cherry')
# print(fruit)
# fruit.extend(['peach', 'orange'])
# print(fruit)
# fruit.insert(0,'strawberry')
# print(fruit)
# print(fruit.pop(0), '삭제', fruit) # 인덱스 지정 반환 삭제
# print(fruit.remove('apple'), fruit)
# print(fruit.clear(), fruit)

# colors = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 1 ]
# colors.sort()
# print(colors)
# colors.reverse()
# print(colors)
# print(colors.pop())
# print(colors)
# print(colors.count(1))

# # 리스트 중 a 문자가 없는 단어 제거 프로그램
# a_list = ['above', 'cookie', 'app', 'about', 'admin', 'bisket', 'apple', 'april']
# for i, item in enumerate(a_list):
#     if item.find('a') == -1: # 찾는 문자열이 없는 경우 -1
#         print('{}를 제거합니다'.format(a_list.pop(i)))
# print(a_list)

# 3) 집합(셋트) 메소드
# s_nature = {'sky', 'sea'}
# print(s_nature)
# s_nature.add('earth')
# print(s_nature)
# s_nature.update({1, 2}, [2, 3])
# print(s_nature)
# print(s_nature.pop())
# print(s_nature)

# s_planet = {'수성', '금성', '지구', '화성', '목성', '토성', '천왕성',\
#             '해왕성'}
# print(s_planet)
# s_planet.discard('명왕성')
# # s_planet.remove('명왕성') # 값이 없을 경우 오류발생
# s_planet.discard('지구')
# print(s_planet)
# s_planet.clear()
# print(s_planet)

# s1 = {'apple', 'banana', 'cherry'}
# s2 = {'apple', 'banana', 'orange'}
# s3 = s1 & s2 # 교집합
# s4 = s1 | s2 # 합집합
# s5 = s1 - s2 # 차집합
# s6 = s1 ^ s2 # 대칭차집합
# print(s3, s4, s5, s6, sep='\n')
# print(s1.intersection(s2))
# print(s1.union(s2))
# print(s1.difference(s2))
# print(s1.symmetric_difference(s2))

x = {1, 2, 3, 4, 5, 6}
y = {1, 2, 3, 7, 8, 9}
print({4, 5, 6, 7} <= x) # 부분집합
print({4, 5, 6}.issubset(x)) # 부분집합