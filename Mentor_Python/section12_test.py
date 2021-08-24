# 1번 문제풀이
import random
import time

pot = []
for n in range(1, 46):
    pot.append(n)
print(pot)

n = 1
jackpot = []
while n < 7:
    random.shuffle(pot)
    print('{}번째 당첨번호는 {}입니다.'.format(n, pot[-1]))
    jackpot.append(pot[-1])
    n += 1
    time.sleep(2)

print('이번 당첨번호는 {}입니다.'.format(jackpot))

# #정답
# import random
# import time
#
# pot = [n for n in range(1, 46)]
# jackpot = []
#
# for n in range(1, 7):
#     random.shuffle(pot)
#     pick = pot.pop()
#     print('{}번째 당첨번호는 {}입니다.'.format(n, pick))
#     jackpot.append(pick)
#     time.sleep(2)
#
# jackpot.sort()
# print('이번 당첨번호는 {} 입니다.'.format(jackpot))

# 2번 문제풀이
import random
from datetime import *
import math

num = random.randint(1, 100)  # 1부터 100이하의 정수 랜덤 반환
# print('랜덤수:', num, type(num))
print('업다운 게임을 시작합니다.')
start = datetime.now()

while True:
    answer = int(input('어떤값일까요?>>> '))
    if answer == num:
        end = datetime.now()
        elapse = end - start
        elapse = math.floor(elapse.total_seconds())
        break
    elif answer < num:
        print('Up')
        continue
    elif answer > num:
        print('Down')
        continue

print('정답입니다.\n{}초만에 성공했습니다.'.format(elapse))

# #정답
# import random
# import time
# import math
#
# answer = random.randint(1, 100)
#
# print('UpDown게임을 시작합니다.')
# start = time.time()
# while True:
#     n = int(input('어떤 값일까요? >>> '))
#     if answer == n:
#         print('정답입니다.')
#         break
#     elif answer < n:
#         print('Down')
#     else:
#         print('Up')
# end = time.time()
#
# elapse = end - start
# print('{}초 만에 성공했습니다.'.format(math.floor(elapse)))
