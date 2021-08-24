'''
개요: 표준모듈
작성자: 진상영
작성일: 2021.03.24
내용: 파이썬에 기본적으로 설치된 모듈(buil-in module)
1) math 모듈
- pi: 원주율
- ceil(): 정수로 올림처리
- floor(): 정수로 내림처리
- trunc(): 정수로 절사처리
- sqrt(): 제곱근
- pow(): 제곱

2) random 모듈
- randint(): 두 인수 사이의 임의 정수 생성
- randrange(): 두 인수 사이의  임의 정수 생성
- random(): 0이상 1미만 범위 임의의 실수 생성
- choice(): 전달된 시퀀스 자료형 요소 중 하나 임의 반환
- sample(): 전달된 시퀀스 자료형 요소 중 지정된 개수 요소 리스트형으로 임의 반환
- shuffle(): 전달된 시퀀스 자료형(리스트) 요소 순서를 재배치, 실제순서 변경, / 문자열, 튜플 불가(오류)

3) time 모듈
- time(): 1970년 1월 1일 0시 0분 0초부터 현재까지 경과된 시간(timestamp) 반환
- ctime(): 시간형식 반환
- strftime(): 지시자 이용 형식을 갖춘 날짜문자열 반환
  년 %y(2자리),%Y(4자리)
  월 %m(2자리),%b(3자리영문),%B(전체영문) / 일 %d(2자리) / 요일 %a(3자리영문),%A(전체영문)
  시 %l,%H / 분 %M / 초 %S / 오전,오후 %p
- sleep(): 인수초만큼 시스템 정지

4) datetime 모듈
- now(): 시스템의 현재 날짜와 시간 반환
- date(): 특정 날짜 반환
- time(): 특정 시간 반환
- timedelta(): +,-연산사용 날짜, 시간 데이터 연산
- totalseconds(): 특정 기간 총 시간을 초로 반환
'''

import math
# print(math.pi)
# print(math.ceil(2.4), math.ceil(2.5))
# print(math.floor(2.4), math.floor(2.5))
# print(math.trunc(-1.9), math.floor(-1.9))
# print(math.sqrt(25), math.pow(5,2))


import random
# print(random.randint(1,10)) # 1부터 10이하의 정수 중 랜덤
# print(random.randrange(1,10,2)) # 1부터 10미만의 정수 중 홀수
# print(random.random())
# if random.random() < 0.5: # 50%확률로 안녕하세요 출력
#     print('안녕하세요.')
#
# season = ['봄', '여름', '가을', '겨울']
# print(random.choice(season))

sam = random.sample(range(1,46), 6)
print(sam, type(sam))

# n = list(range(1,10))
# random.shuffle(n)
# print(n)

# dice = random.randint(1,6)
# print('컴퓨터가 주사위를 굴렸습니다.\n데구르르르~ 데굴~ 데굴~')
# # print(dice)
# while True:
#     choice = int(input('\n주사위 값은 얼마일까요?>>> '))
#     if dice == choice:
#         print('{}! 오 맞췄습니다. 대단하군요~'.format(choice))
#         break
#     else:
#         print('틀렸습니다. 다시 맞춰보세요!')


import time
# print(time.time())
# print(time.ctime())
# # 년 %y(2자리),%Y(4자리)
# # 월 %m(2자리),%b(3자리영문),%B(전체영문) / 일 %d(2자리) / 요일 %a(3자리영문),%A(전체영문)
# # 시 %l(12시간제),%H(24시간제) / 분 %M(2자리) / 초 %S(2자리) / 오전,오후 %p(AM/PM)
# print(time.strftime('%Y-%m-%d %a %H:%M:%S'))
#
# time.sleep(10)


import datetime
# today = datetime.datetime.now() # 모듈.클래스.메소드()
# yesterday = today - datetime.timedelta(days=1)
# tomorrow = today + datetime.timedelta(days=1)
# print('오늘: ', today)
# print('어제: ', yesterday)
# print('내일: ', tomorrow)
# print(datetime.datetime.now())
# print(today.year, today.month, today.day, today.hour, today.minute, today.second)
# print(datetime.date(1973, 9, 20))
# print(datetime.time(23, 59, 59))

# date1 = datetime.date(2020, 8 , 25)
# date2 = datetime.date(2020, 8 , 26)
# print(date2 - date1)
# print(datetime.timedelta(days=1))
# print((date2-date1).total_seconds())

# from datetime import *
#
# start = datetime.now()  # from절을 이용해 import하면 모듈명 생략
# total = 0
# for num in range(1, 10000001):
#     total += num
# end = datetime.now()
#
# elapse = end - start
# elapse = elapse.total_seconds()
#
# print('총 합은 {}입니다.'.format(total))
# print('총 {}초가 소요됩니다.'.format(elapse))


