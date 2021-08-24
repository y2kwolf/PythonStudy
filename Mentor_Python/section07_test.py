# # 1번 문제풀이
# x = int(input('정수를 입력하시오.(입력값 이하 역순출력)>>> '))
# for n in range(1,x+1):
#     print(x+1-n)
# # 정답
# for n in range(5, 0, -1):
#     print(n)

# # 2번 문제풀이
# n = int(input('임의의 양수를 입력하세요.>>> '))
# sum = 0
# for a in range(1, n+1):
#     sum += a
# print('1부터 {}사이 모든 정수의 합계는 {}입니다.'.format(n, sum))
# 정답
# total = 0
# end = int(input('임의의 양수를 입력하세요 >>> '))
# for n in range(0, end + 1):
#     total += n
# print('1부터 {}사이 모든 정수의 합계는 {}입니다.'.format(n, total))

# 3번 문제풀이
# n = int(input('몇 개의 과일을 보관할까요?>>> '))
# basket = []
# for a in range(1,n+1):
#     fruit = input('{}번째 과일을 입력하세요>>> '.format(a))
#     basket.append(fruit)
# print('입력받은 과일들은 {}입니다.'.format(basket))
# 정답
# count = int(input('몇 개의 과일을 보관할까요? >>> '))
# basket = []
# for n in range(count):
#     fruit = input('{}번째 과일을 입력하세요 >>> '.format(n + 1))
#     basket.append(fruit)
# print('입력 받은 과일들은 {}입니다.'.format(basket))

# try: # 예외처리
#     n = int(input('몇 개의 과일을 보관할까요?>>> '))
#     basket = []
#     for a in range(1,n+1):
#         fruit = input('{}번째 과일을 입력하세요>>> '.format(a))
#         basket.append(fruit)
#     print('입력받은 과일들은 {}입니다.'.format(basket))
# except:
#     print('정수를 입력하세요!')


# # 4번 문제풀이
# exam = [99, 78, 100, 91, 81, 85, 54, 100, 71, 50]
# score = []
# for point in exam:
#     if point > 95:
#         score.append(100)
#     elif point <= 95:
#         point += 5
#         score.append(point)
#     else:
#         score.append(point)
# print(score)
# # 정답
# exam = [99, 78, 100, 91, 81, 85, 54, 100, 71, 50]
# score = [min(n + 5, 100) for n in exam]
# print(score)

# 5번 문제풀이
# 모름

# for n in range(1, 100):
#     units = n % 10
#     tens = n // 10
#     condition1 = units % 3 == 0 and units != 0
#     condition2 = tens % 3 == 0 and tens != 0
#     if condition1 and condition2:
#         print('짝짝', end='\t')
#     elif condition1 or condition2:
#         print('짝', end='\t')
#     else:
#         print(n, end='\t')
#     if n % 10 == 0:
#         print()