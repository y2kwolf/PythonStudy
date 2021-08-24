# # 1번 문제풀이
# while True:
#     num = input('전화번호를 입력하세요>>> ')
#     if num == '':
#         break
#     print('입력하신 지역번호는 {}, 국번은 {}, 번호는 {}입니다.'.format(num.split('-')[0], num.split('-')[1], num.split('-')[2]))
# 정답
# # 첫 번째 풀이입니다. (index() 메소드와 슬라이싱 활용)
# phone = input('전화번호를 입력하세요 >>> ')
# start = phone.index('-') + 1
# end = phone.index('-', start)
# code = phone[start:end]
# print(code)
# # 두 번째 풀이입니다. (split() 메소드 활용)
# phone = input('전화번호를 입력하세요 >>> ')
# code = phone.split('-')[1]
# print(code)

# # 2번 문제풀이
# while True:
#     num = input('사업자등록번호를 입력하세요(예:123-45-67890)>>> ')
#     no = num.split('-')
#     if num.find('-') == 3 and num.rfind('-') == 6 and no[0].isdecimal() \
#        and no[1].isdecimal() and no[2].isdecimal():
#         print('올바른 형식입니다.\n당신의 사업자등록번호는 {}입니다.'.format(num))
#         break
#     else:
#         print('올바른 형식이 아닙니다.')
# # 정답
# no = input('사업자등록번호를 입력하세요(예: 123-45-67890) >>> ')
#
# condition1 = (no.find('-') == 3)
# condition2 = (no.find('-', 4) == 6)
# condition3 = (len(no) == 12)
# condition4 = (no.replace('-', '').isdecimal())
# if condition1 and condition2 and condition3 and condition4:
#     print('올바른 형식입니다.')
# else:
#     print('올바른 형식이 아닙니다.')

# # 3번 문제풀이
# member = '"김철수",85'
# student = member.split(',')
# name = student[0].strip('"')
# score = student[1]
# print('이름은 {}이고, 점수는 {}점입니다.'.format(name, score))
# 정답
student = '"김철수",85'
name = student.split(',')[0].strip('"')
age = student.split(',')[1]
print('이름은 {}이고, 점수는 {}점입니다.'.format(name, age))