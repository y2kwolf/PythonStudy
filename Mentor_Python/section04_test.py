# # 1번 문제풀이
# number = int(input('10~99 사이의 정수를 입력하세요>>>'))
# ten = number//10
# one = number%10
#
# print('십의 자리:{}'.format(ten))
# print('일의 자리:{}'.format(one))
#
# # 정답
# number = int(input('10 ~ 99 사이의 정수를 입력하세요 >>> '))
# tens = number // 10
# units = number % 10
# print('십의 자리: {}'.format(tens))
# print('일의 자리: {}'.format(units))
#
# # 2번 문제풀이
# seconds = int(input('초를 입력하세요>>>'))
#
# second = seconds%60
# minute = (seconds//60)%60
# hour = seconds//3600
#
# print('변환결과는 {}시간 {}분 {}초입니다'.format(hour, minute, second))
#
# # 정답
# times = int(input('초를 입력하세요 >>> '))
# hour = times // 3600
# minute = times % 3600 // 60
# second = times % 60
# print('변환 결과는 {}시간 {}분 {}초입니다.'.format(hour, minute, second))
#
# # 3번 문제풀이
# id = int(input('4자리 사원번호를 입력하세요>>>'))
# work = id%10
# if work >= 5:
#     print('근무 시간은 오전입니다.')
# else:
#     print('근무 시간은 오후입니다.')
#
# # 정답
# emp_no = int(input('4자리 사원번호를 입력하세요 >>> '))
# emp_last_no = emp_no % 10
# is_am = emp_last_no >= 5
# print('근무 시간은 {}입니다.'.format('오전' if is_am else '오후'))

# # 4번 문제풀이
# print('한 박스에 20개의 라면을 담을 수 있습니다.')
# print('라면의 개수를 입력하시면 필요한 박스 수를 알려드립니다.')
#
# ea = int(input('라면의 개수를 입력하세요>>>'))
# box = ea//20
#
# print('{}개 라면을 담으려면 {}박스가 필요합니다.'.format(ea, box if ea%20 == 0 else box+1))
#
# # 정답
# print('한 박스에 20개의 라면을 담을 수 있습니다.')
# print('라면의 개수를 입력하시면 필요한 박스 수를 알려드립니다.')
# ramen = int(input('라면의 개수를 입력하세요 >>> '))
# box = ramen // 20 if ramen % 20 == 0 else ramen // 20 + 1
# print('{}개 라면을 담으려면 {}박스가 필요합니다.'.format(ramen, box))

# 5번 문제풀이

lang = int(input('국어 점수를 입력하세요>>> '))
eng = int(input('영어 점수를 입력하세요>>> '))
math = int(input('수학 점수를 입력하세요>>> '))

avg = (lang + eng + math)/3
result = '합격' if avg >= 80 else '불합격'
# print(type(avg))
print('평균은 {:.1f}점이고, 결과는 {}입니다.'.format(avg, result))
print('평균은 %.1f점이고, 결과는 %s입니다.' % (avg, result))
