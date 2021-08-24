# # 1번 문제
# n = int(input('정수를 입력하세요!>>> '))
#
# if n != 0:
#     x = 1
#     while x <= n:
#         print('{}번째 \tHello'.format(x))
#         x += 1
# else:
#     print('잘못된 입력입니다')

# # 정답
# count = int(input('정수를 입력하세요 >>> '))
# if count <= 0:
#     print('잘못된 입력입니다.')
# else:
#     n = 0
#     while n < count:
#         print('{}번째 Hello'.format(n + 1))
#         n += 1

# # 2번 문제풀이
# n = int(input('정수를 입력하세요(0부터 입력값까지 7의배수를 출력합니다)>>> '))
# x = 1
# while x <= n:
#     if x%7 == 0:
#         print('{}'.format(x))
#     x += 1

# # 정답
# n = 1
# while n <= 100:
#     if n % 7 == 0:
#         print(n)
#     n += 1
#
# # 또는
# n = 7
# while n <= 100:
#     print(n)
#     n += 7
    
# # 3번 문제풀이
# money = int(input('자판기에 얼마를 넣을까요?>>> '))
# coffee = 1
# if money >= 300:
#     while coffee <= (money//300):
#         change = money-coffee*300
#         print('커피 {}잔, 잔돈 {}원'.format(coffee, change))
#         coffee += 1
# else:
#     print('금액이 부족합니다.')

# # 정답
# coffee = 0
# money = int(input('자판기에 얼마를 넣을까요? >>> '))
# while money >= 300:
#     coffee += 1
#     money -= 300
#     print('커피 {}잔, 잔돈 {}원'.format(coffee, money))

# # 4번 문제풀이
# s = set()
# while len(s) <= 4:
#     x = int(input('0~9 사이 정수를 입력하세요>>> '))
#     if x > 0 and x < 10:
#         s.add(x)
#     else:
#         print('입력하신 값이 잘못되었습니다.')
# print('모두 입력되었습니다.')
# print('입력된 값은 {}입니다.'.format(s))

# # 정답
# numbers = set()
# while len(numbers) < 5:
#     n = int(input('0 ~ 9 사이 정수를 입력하세요 >>> '))
#     numbers.add(n)
# print('모두 입력되었습니다.')
# print('입력된 값은 {}입니다.'.format(numbers))

# # 5번 문제풀이
# n = 1
# line = 1
# while line <= 10:
#     # print('{}번째줄: \t'.format(line), end='')
#     while n <= line*10:
#         print(n,'\t\t', end='')
#         n += 1
#     print()
#     line += 1

# # 정답
# n = 1
# while n <= 100:
#     if n % 10 == 0:
#         print(n)
#     else:
#         print(n, end='\t')
#     n += 1

# # 6번 문제풀이
# dan = 2
# n = 1
# while dan <= 9:
#     while n <= 9:
#         print('{}x{}={}\t'.format(dan, n, dan*n), end='')
#         n += 1
#     print()
#     n = 1
#     dan += 1

# # 정답
# n = 1
# while n <= 9:
#     dan = 2
#     while dan <= 9:
#         print('{}×{}={}'.format(dan, n, dan * n), end='\t')
#         dan += 1
#     print()
#     n += 1
