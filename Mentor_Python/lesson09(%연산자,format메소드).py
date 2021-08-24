'''
개요: %연산자, format() 메소드
작성자: 진상영
작성일: 2021.03.08
1. %연산자: 형식을 갖춘 문자열
- %d 정수(10진수)
- %o 정수(8진수)
- %x 정수(16진수)
- %f 실수 -> 기본 소수점이하 6자리 표시
- %s 문자열
2. format() 메소드
- 인수로 변수나 값을 표시, 해당값 표시 위치에 중괄호({}) 표시방식
'''

# # % 연산자
# name = "진상영"
# print('내 이름은 %s입니다' % name)
#
# height = 174.5
# print('내 키는 %fcm입니다' % height)
#
# weight = 73.38
# print('내 몸무게는 %.1fkg입니다.' % weight) # 소수 1자리 반올림 표현
# # print('내 몸무게는 %.3f' % weight) # 소수 3자리 반올림 표현
#
# year,month,day = 1973, 8, 24
# print('내 생일은 %d년 %d월 %d일 입니다.' %(year, month, day)) # 형식 연산자가 여러개일 경우 괄호사용
#
# # format() 메소드
# zipcode = '06236'
# print('우편번호: {}'.format(zipcode))
#
# address = '''부산광역시 해운대구
# 해운대로 469번길 110'''
# print('주소: {addr}'.format(addr=address))
# # print('주소: {}'.format(address)) 위실행결과와 동일한 표현
#
# tel1, tel2, tel3 = '010', '2746', '8762'
# print('연락처: {0}-{1}-{2}'.format(tel1, tel2, tel3))
#
# # f-strings : format()메소드와 유사. 단, 가독성이 뛰어나다는 장점
# who = 'you'
# how = 'happy'
# print(f'{who} make me {how}')
#
# age = 49
# print(f'내년엔 {age+1}살이 됩니다.')


# # format 사용법 추가
# print('%10s' % ('happy'))  # 10자리 확보 (오른쪽기준)
# print('{:>10}'.format('y'))
# print('{:>10}'.format('py'))
# print('{:>10}'.format('ppy'))
# print('{:>10}'.format('appy'))
# print('{:>10}'.format('happy'))

#
# print('%10s' % ('happyland'))
# print('{:>10}'.format('happy'))
#
# print('%-10s' % ('happy'))  # 10자리 확보 (왼쪽기준)
# print('{:10}'.format('happy'))
#
# print('{:_>10}'.format('happy')) # 공백대신 다른 문자 채우기
# print('{:$>10}'.format('happy'))
#
# print('{:^10}'.format('happy')) # ^로 중앙정렬
#
# print('%.8s' % ('happyland')) # .붙여 절삭
# print('%.5s' % ('happyland'))
# print('%.2s' % ('happyland'))
#
# print('{:10}'.format('koreaedugroup'))
# print('{:10.5}'.format('koreaedugroup'))
# print('{:10.8}'.format('koreaedugroup'))

# print('%d %d' % (1,2))
# print('{} {}'.format(1,2))
#
# print('%4d' % (42))
# print('{:4d}'.format(42))

import math
# print('%f' % (math.pi))
# print('{:f}'.format(math.pi))
#
# print('%1.8f' % (math.pi))
# print('{:f}'.format(math.pi))

# print('%6.2f' % (math.pi))
# print('%06.2f' % (math.pi))
# print('{:06.2f}'.format(math.pi))