'''
개요: break문
작성자: 진상영
작성일: 2021.03.22
내용: break문 반복문 강제종료
'''

# while True:
#     city = input('대한민국의 수도는 어디인가요?>>> ')
#     if city == '서울' or city == 'seoul' or city == 'SEOUL':
#         print('정답입니다.')
#         break
#     else:
#         print('오답입니다. 다시 시도하세요.')

hobbies = []
while True:
    hobby = input('취미를 입력하세요(종료는 그냥 엔터)>>> ')
    if hobby == '':
        print('입력된 취미가 모두 저장되었습니다.')
        break
    else:
        hobbies.append(hobby)
print(hobbies)