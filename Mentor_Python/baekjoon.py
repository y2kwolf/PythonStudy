# a, b = input().split('-')
# a1 = int(a)
# b1 = int(b)
# print(type(a), type(b))
# print(a1+b1)

# C언어
# print("오늘의 날짜를 입력하시오(YYYY.DD.YY 형식으로).");
# scanf("%d.%d.%d", &year, &month, &day);


# print("\    /\\")
# print(" )  ( \')")
# print("(  /  )")
# print(" \(__)|")
# print()
# print("|\\_/|")
# print("|q p|   /}")
# print('( 0 )\"\"\"\\')
# print('|\"^\"`    |')
# print("||_/=\\\\__|")

# A, B, C = input().split()
# num1 = int(A)
# num2 = int(B)
# num3 = int(C)
# print((num1+num2)%num3)
# print(((num1%num3)+(num2%num3))%num3)
# print((num1*num2)%num3)
# print(((num1%num3)*(num2%num3))%num3)

# x = input()   # 입력 472 385
# y = input()   # 출력 2360, 3776, 1416, 181720
# num1 = int(x)
# num2 = int(y)
# n = 2
# while n >= 0:
#     print(num1*int(y[n]))
#     n -= 1
# print(num1*num2)
# print(num1*int(y[2]))
# print(num1*int(y[1]))
# print(num1*int(y[0]))
# print(num1*num2)

# x, y = int(input()), input()
# [print(x * int(y[2 - i])) for i in range(3)]
# print(x*int(y))

# x, y = input().split()
# num1 = int(x)
# num2 = int(y)
# if num1 > num2:
#     print('>')
# elif num1 < num2:
#     print('<')
# elif num1 == num2:
#     print('==')

# score = int(input())
# if score >= 90:
#     print('A')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print('C')
# elif score >= 60:
#     print('D')
# else:
#     print('F')

# # 윤년 계산하기
# year = int(input())
# if (year%4 == 0 and year%100 != 0) or year%400 == 0:
#     print('1')
# else:
#     print('0')

# x, y = int(input()), int(input())
# if x > 0 and y > 0:
#     print('1')
# elif x < 0 and y > 0:
#     print('2')
# elif x < 0 and y < 0:
#     print('3')
# elif x > 0 and y < 0:
#     print('4')

# h, m = input().split()
# h1 = int(h)
# m1 = int(m)
# if m1 < 45:
#     if h1 == 0:
#         print('{} {}'.format(23, 60-(45-m1)))
#     else:
#         print('{} {}'.format(h1 - 1, 60 - (45 - m1)))
# elif m1 >= 45:
#     print('{} {}'.format(h1, m1-45))

# n = int(input())
# for i in range(9):
#     i += 1
#     print('{} * {} = {}'.format(n, i, n*i))

# t = int(input())
# for i in range(t):
#     A, B = input().split()
#     x = int(A)
#     y = int(B)
#     print('Case #{}: {} + {} = {}'.format(i+1, x, y, x+y))

# n = int(input())
# a = 0
# for i in range(n):
#     a += i+1
# print(a)

# n = int(input())
# for i in range(n):
#     star = '*' * (i + 1)
#     print(star.rjust(n))

# 입력
# 10 5 -> 첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
# 1 10 4 9 2 3 8 5 7 6 -> 둘째 줄에 수열 A를 이루는 정수 N개
# 출력
# X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.
# a, b = input().split()
# N = int(a)
# X = int(b)
# A = list(input().split())
# for i in A:
#     if int(i) < X:
#         print(i)

# import random
# a, b = input().split()
# N = int(a)
# X = int(b)
# A = random.sample(range(1,N+1), N)
# print(A)
# for i in A:
#     if int(i) < X:
#         print(i)

# import sys
# a = sys.stdin.readline()
# for i in range(int(a)):
#     x, y = sys.stdin.readline().split()
#     print(int(x)+int(y))

# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a + b)
#     except:
#         break

n = input()
if int(n) < 10:
    n = '0'+n
    # print(n, type(n))
# print(n, type(n))
n1 = int(n[0])
n2 = int(n[1])
sum = n1 + n2                   # 8=2+6
while int(n) != sum:            # 26 != 14
    cycle += 1                  # 2
    sum = n1 + n2               # 8=2+6 /
    a = str(sum)                # '8'
    new_sum = str(n2) + a[-1]   # '68' = '6' + '8'
    n1 = int(new_sum[0])        # n1 = 6 /
    n2 = int(new_sum[1])        # n2 = 8 /
print(cycle)