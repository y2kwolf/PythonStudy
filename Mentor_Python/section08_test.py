# # 1번 문제풀이
# money = 10000
# print('현재 {}원이 있습니다.'.format(money))
# while True:
#     n = int(input('사용할 금액 입력>>> '))
#     if n > money:
#         print('{}이 부족합니다.'.format(n-money))
#         print('현재 {}원이 있습니다.'.format(money))
#         continue
#     elif n <= 0:
#         print('0이하의 금액은 사용할 수 없습니다.')
#         print('현재 {}원이 있습니다.'.format(money))
#         continue
#     money -= n
#     print('현재 {}원이 있습니다.'.format(money))
#     if money == 0:
#         break
# # 정답
# money = 10000
# while True:
#     print('현재 {}원이 있습니다.'.format(money))
#     if money == 0:
#         break
#     spend = int(input('사용할 금액 입력 >>> '))
#     if spend <= 0:
#         print('0 이하의 금액은 사용할 수 없습니다.')
#     elif spend > money:
#         print('{}원이 부족합니다.'.format(spend - money))
#     else:
#         money -= spend

# # 2번 문제풀이
# while True:
#     n = int(input('이번 영화의 평점을 입력하세요.>>> '))
#     if 0 < n <6:
#         print('평점: {}'.format('★'*n))
#         break
#     else:
#         print('평점은 1~5사이만 입력할 수 있습니다.')
# # 정답
# while True:
#     grade = int(input('이번 영화의 평점을 입력하세요 >>> '))
#     if grade >= 1 and grade <= 5:
#         print('평점: {}'.format('★' * grade))
#         break
#     else:
#         print('평점은 1~5 사이만 입력할 수 있습니다.')

# # 3번 문제풀이
# pwd = 'qwerty'
# try_no = 0
# while True:
#     n = input('비밀번호를 입력하세요>>> ')
#     if n == pwd:
#         print('비밀번호를 맞혔습니다.')
#         break
#     else:
#         try_no += 1
#         if try_no > 4:
#             print('비밀번호 입력 횟수를 초과했습니다.')
#             break
# # 정답
# answer = 'qwerty'
# count = 0
# while True:
#     if count == 5:
#         print('비밀번호 입력 횟수를 초과했습니다.')
#         break
#     pw = input('비밀번호를 입력하세요 >>> ')
#     if pw == answer:
#         print('비밀번호를 맞혔습니다.')
#         break
#     count += 1

# # 4번 문제풀이
# for dan in range(2, 10):
#     if dan % 2 == 0:
#         print()
#         continue
#     else:
#         for n in range(1, dan+1):
#             print('{}*{}={}'.format(dan, n, dan*n))
#     dan += 1
# 정답
for dan in range(2, 10):
    if dan % 2 == 0:
        print()
        continue
    for n in range(1, 10):
        if dan < n:
            break
        print('{}x{}={}'.format(dan, n, dan * n))