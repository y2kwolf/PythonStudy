'''
개요: print() 함수
작성자: 진상영
작성일: 2021.03.08
내용: print() 함수 기본속성
- sep: 출력할 value 구분자 (디폴트는 공백)
- end: value 출력 후 출력할 문자
- file: 출력방향지정
- flush: flush 유무지정
'''
print('재미있는', '파이썬') # 콤마(,)로 여러값 출력
print('Python', 'Java', 'C', sep='.')

print()

print('영화 타이타닉')
print('평점', end=':')
print('5점')

print("파이썬","welcome to my world",sep="-",end="!")

# sample.py 파일 생성
fos = open('sample.py', mode='wt')
print('print("Hello World")', file=fos)
fos.close()
