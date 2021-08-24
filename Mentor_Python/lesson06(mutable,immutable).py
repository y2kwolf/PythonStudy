'''
개요: mutable, immutable
작성자: 진상영
작성일: 2021.02.27
내용:  
- mutable 리스트, 세트, 딕셔너리
- immutable 정수, 실수, 문자열, 튜플
'''
"""
id() 함수 전달된 변수나 자료형의 메모리 저장위치 주소(address) 반환
"""


""" 1) mutable """
me = [1,2,3]
id(me) # 메모리 저장위치 반환
me.append(4)
id(me)

""" 2) immutable """
me = 10
id(me)
me += 1
id(me)