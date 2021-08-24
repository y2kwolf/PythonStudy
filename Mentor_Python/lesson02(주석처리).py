'''
개요: 반지름을 전달하면 원의 넓이를 반환하는 get_area() 함수
작성자: 진상영
작성일: 2021.02.27
내용: 
1) 주석처리 
- 여러줄 주석: ''' ''', """ """
- 한줄 주석: #

2) 모듈(module)
- 내장모듈(built-in module) 기본제공 
- 서드파티모듈(third-party module) 외부개발자 제공 추가설치 후 import
'''

import math # math 모듈 포함
def get_area(radius): # get_area() 함수 정의
    area = math.pi * math.pow(radius, 2)
    return area
radius = 2
area = get_area(radius) # get_area() 함수 호출 결과를 area 변수에 저장
print(area)
print(get_area.__doc__) # Docstring 확인