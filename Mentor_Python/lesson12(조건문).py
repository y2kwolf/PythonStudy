'''
개요: 조건문
작성자: 진상영
작성일: 2021.03.16
내용:
1) if문
if 조건식1:
    조건식1의 결과가 True일 때 실행문
elif 조건식2:
    조건식1 False, 조건식2 결과가 True일 때 실행문
else:
    조건식1,2의 결과가 False일 때 실행문

- 조건식은 True 또는 False 반환
- 실행문은 반드시 들여쓰기: C나 자바처럼 중괄호({}) 미사용
'''

# age = int(input('몇 살입니까?>>> '))
# if age >= 20:
#     print('당신은 성인입니다.')
# else:
#     print('당신은 미성년자입니다.')

# important = int(input('중요도를 입력하세요.>>> '))
# if important >= 100:
#     print('상')
# else:
#     if important >= 50:
#         print('중')
#     else:
#         print('하')

# important = int(input('중요도를 입력하세요.>>> '))
# if important >= 100:
#     print('상')
# elif important >= 50:
#     print('중')
# else:
#     print('하')

age = int(input('당신의 나이는 몇살입니까?>>> '))
if age >= 20:
    print('당신은 성인입니다.')
elif age >= 17:
    print('당신은 고등학생입니다.')
elif age >= 14:
    print('당신은 중학생입니다.')
elif age >= 8:
    print('당신은 초등학생입니다.')
else:
    print('당신은 미취학아동입니다.')
