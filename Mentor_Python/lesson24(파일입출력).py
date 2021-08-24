'''
개요: 파일 입출력(input/output)
작성자: 진상영
작성일: 2021.03.27~04.12
내용: 파일 입력(읽기), 출력(추가 및 생성), 저장
1. 파일입출력개요
1) 파일열기: 파일객체 = open(파일명, 모드)
- 모드: 입력(r-읽기) / 출력(w-쓰기, a-추가, x-배타적추가)
- 종류: t-text, b-binary
2) 파일닫기: 파일객체.close()
3) with문 - close()메소드 생략
with open(파이명, 모드) as 파일객체
    파일처리코드
2. 파일입력
- file.read(size) 메소드
'''

# file = open('myFile.txt', 'wt')
# print('myFile.txt 파일이 생성되었습니다.')
# file.close()
#
# with open('myFile2.txt', 'wt') as file:
#     print('myFile2.txt 파일이 생성되었습니다.')

# file = open('hello.txt', 'wt')
# file.write('안녕하세요.')
# file.write('\n')
# file.write('반갑습니다.')
# file.write('\n')
# print('hello.txt 파일이 생성되었습니다.')
# file.close()

# file = open('hello.txt', 'at')
# file.write('hello.\n')
# file.write('Nice to meet you.\n')
# file.close()

# import time
# file = open(time.strftime('%Y-%m-%d') + '.txt', 'at') # a모드는 파일이 없는 경우 생성, 있을경우 추가
# while True:
#     schedule = input('오늘의 스케쥴을 입력하세요.>>> ')
#     if not schedule:
#         break
#     file.write(schedule + '\n')
# file.close()

# file = open('hello.txt', 'rt')
# str = file.read()
# print(str, end='')
# file.close()

# file = open('hello.txt', 'rt')
# while True:
#     str = file.read(5)  # 파일로부터 5글자 읽기
#     if not str:
#         break
#     print(str, end='*')
# file.close()

# file = open('hello.txt', 'rt')
# while True:
#     str = file.readline() # 파일로부터 한줄 읽기
#     if str == '':
#         break
#     print(str, end='*')
# file.close()

# file = open('hello.txt', 'rt')
# line_list = file.readlines() # 파일로부터 한줄씩 리스트 저장
# for line in line_list:
#     print(line, end='*')
# file.close()

file = open('hello.txt', 'rt')
line_list = file.readlines()
for no, line in enumerate(line_list): # 내장함수 enumerate(): 리스트의 인덱스와 요소 출력
    print('{} {}'.format(no+1, line), end='')
file.close()

# import sys
# file = open('hello.txt', 'rt')
# line_list = file.readlines()
# sys.stdout.writelines(line_list) #sys모듈의 표준입출력 위한 stdout객체 사용
# file.close()

# file = open('엄마돼지아기돼지.txt', 'rt')
# line_list = file.readlines()
# count = 0
# for list in line_list:
#     str_count = list.count('꿀') # 문자열 메소드 count(): 문자열 내부에 포함된 특정 문자열의 개수 반환
#     count += str_count
# print('꿀은 전체 {}번 나타납니다.'.format(count))