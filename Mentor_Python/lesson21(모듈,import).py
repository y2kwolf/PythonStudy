'''
개요: 모듈과 import
작성자: 진상영
작성일: 2021.03.24
내용: 파이썬 파일로 언제든지 사용할 수 있도록 변수, 함수, 클래스를 모아 놓은 파일
1) 모듈의 사용
- import 모듈
- from 모듈 import 함수
- from 모듈 import 함수1, 함수2
- from 모듈 import *

2) import한 모듈 함수 호출
- 모듈.함수()

3) 별명사용
- import 모듈 as 별명 -> 별명.함수()
- from 모듈 import 함수 as 별명 -> 별명()
'''

# import converter
# km = 15000
# gram = 1000
# miles = converter.kilometer_to_miles(km)
# pounds = converter.gram_to_pounds(gram)
# print('{:,}km는 {:,.2f}miles입니다.'.format(km, miles))
# print('{:,}g은 {:.2f}pounds입니다.'.format(gram, pounds))

# from converter import kilometer_to_miles
# km = 15000
# miles = kilometer_to_miles(km)
# print('{:,}km는 {:,.2f}miles입니다.'.format(km, miles))

# from converter import * # 모든함수 활용가능, 모듈.함수() 형식 불필요
# km = 150
# gram = 1000
# miles = kilometer_to_miles(km)
# pounds = gram_to_pounds(gram)
# print('{:,}km = {:,.2f}miles'.format(km, miles))
# print('{:,}g = {:.2f}pounds'.format(gram, pounds))

# import converter as cvt
# km = 15000
# gram = 1000
# miles = cvt.kilometer_to_miles(km)
# pounds = cvt.gram_to_pounds(gram)
# print('{:,}km는 {:,.2f}miles입니다.'.format(km, miles))
# print('{:,}g은 {:.2f}pounds입니다.'.format(gram, pounds))

# from converter import kilometer_to_miles as ktom
# km = 15000
# miles = ktom(km)
# print('{:,}km는 {:,.2f}miles입니다.'.format(km, miles))

# from my_secure import *
#
# print(secure_name('진상영'))
# print(secure_no('730920-1109515'))
# print(secure_phone('010-2746-8762'))