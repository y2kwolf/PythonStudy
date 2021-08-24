'''
개요: 반복문1
작성자: 진상영
작성일: 2021.03.17
내용:
1) while문
while 조건식:
    반복실행문
'''

# my_list = []
#
# n = int(input('정수를 입력하세요(종료는 0입니다.)>>> '))
#
# while n != 0:
#     my_list.append(n)
#     n = int(input('정수를 입력하세요(종료는 0입니다.)>>> '))
#
# print('입력한 정수는 {}이고, \n총합은 {}입니다.'.format(my_list, sum(my_list)))

# my_list = []
#
# n = 1
# while n != 0:
#     n = int(input('정수를 입력하세요(종료는 0입니다.)>>> '))
#     my_list.append(n) # append() 메소드는 마지막 요소 추가
#
# my_list.pop()  # pop() 메소드는 인덱스 미지정시 마지막 요소 제거
#
# print('입력한 정수는 {}이고, \n총합은 {}입니다.'.format(my_list, sum(my_list)))

# day = 1
# while day <= 5:
#     hour = 1
#     while hour <= 3:
#         print('{}일차 {}교시입니다.'.format(day, hour))
#         hour += 1
#     day += 1

# dan = 2
# while dan <= 9:
#     n = 1
#     print('\n<{}단>'.format(dan))
#     while n <= 9:
#         print('{} x {} = {}'.format(dan, n, dan*n) )
#         n += 1
#     dan += 1