'''
개요: continue문
작성자: 진상영
작성일: 2021.03.22
내용: continue문은 반복문의 시작 지점으로 제어의 흐름 변경
- while문 : 조건식 이동 실행
- for문 : 반복가능객체 이동 나머지 실행
'''

# fruits = ['사과', '감귤']
# count = 3
#
# while count > 0:
#     fruit = input('어떤 과일을 저장할까요?>>> ')
#     if fruit in fruits:
#         print('동일한 과일이 있습니다.')
#         continue
#     fruits.append(fruit)
#     count -= 1
#     print('입력이 {}번 남았습니다.'.format(count))
# print('5개 과일은 {}입니다.'.format(fruits))

count = 0 # 입력받을 양의 정수 갯수
total = 0 # 입력받은 정수의 갯수
while count < 5:
    n = int(input('{}번째 정수를 입력하세요.>>> '.format(count+1)))
    if n <= 0:
        print('0이하의 정수는 처리할 수 없습니다.')
        continue
    total += n
    count += 1
print('입력한 정수의 총합계는 {}입니다.'.format(total))