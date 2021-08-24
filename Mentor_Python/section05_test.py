# # 1번 문제풀이
# point = int(input('점수를 입력하세요!>>> '))
#
# if point >= 90:
#     print('점수는 {}점이고, 학점은 A학점입니다.'.format(point))
# elif point >= 80:
#     print('점수는 {}점이고, 학점은 B학점입니다.'.format(point))
# elif point >= 70:
#     print('점수는 {}점이고, 학점은 C학점입니다.'.format(point))
# elif point >= 60:
#     print('점수는 {}점이고, 학점은 D학점입니다.'.format(point))
# else:
#     print('점수는 {}점이고, 학점은 F학점입니다.'.format(point))

# # 정답
# score = int(input('점수를 입력하세요 >>> '))
# if score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'
# elif score >= 70:
#     grade = 'C'
# elif score >= 60:
#     grade = 'D'
# else:
#     grade = 'F'
# print('점수는 {}점이고, 학점은 {}학점입니다.'.format(score, grade))

# # 2번 문제풀이
# integer = int(input('정수를 입력하세요>>> '))
# triple = integer%3
#
# if triple == 0 and integer != 0:
#     print('{}는 3의 배수입니다.'.format(integer))
# else:
#     print('{}는 3의 배수가 아닙니다.'.format(integer))

# # 정답
# n = int(input('정수를 입력하세요 >>> '))
# if n % 3 == 0 and n != 0:
#     print('{}는 3의 배수입니다.'.format(n))
# else:
#     print('{}는 3의 배수가 아닙니다.'.format(n))


# # 3번 문제풀이
# int1 = int(input('첫번째 정수를 입력하시오>>> '))
# int2 = int(input('두번째 정수를 입력하시오>>> '))
# int3 = int(input('세번째 정수를 입력하시오>>> '))
#
# if int1 >= int2 and int1 >= int3:
#     print('가장 큰 수는 {}입니다.'.format(int1))
# elif int2 >= int1 and int2 >= int3:
#     print('가장 큰 수는 {}입니다.'.format(int2))
# else:
#     print('가장 큰 수는 {}입니다.'.format(int3))

# # 정답
# n1 = int(input('정수1 입력 >>> '))
# n2 = int(input('정수2 입력 >>> '))
# n3 = int(input('정수3 입력 >>> '))
# if n1 >= n2 and n1 >= n3:
#     print('가장 큰 수는 {}입니다.'.format(n1))
# elif n2 >= n1 and n2 >= n3:
#     print('가장 큰 수는 {}입니다.'.format(n2))
# else:
#     print('가장 큰 수는 {}입니다.'.format(n3))

# # 4번 문제풀이
# car_no = input('차량번호를 입력하세요>>> ')
# end_no = int(car_no[-1])
# drive = end_no%2
# if drive == 0:
#     result = '운행가능'
# else:
#     result = '운행불가'
# print('차량번호 \'{}\'는 오늘 {}합니다.'.format(car_no, result))

# # 정답
# car_no = input('차량번호를 입력하세요 >>> ')
# if int(car_no[-1]) % 2 == 0:
#     result = '운행가능'
# else:
#     result = '운행불가'
# print('차량번호 {} 는 오늘 {}입니다.'.format(car_no, result))