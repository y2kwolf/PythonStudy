'''
개요: 자료형(type)
작성자: 진상영
작성일: 2021.02.27
내용:
1) int:     정수형    int(n)      정수변환
2) float:   실수형    float(n)    실수변환
3) bool:    논리형    bool(n)     논리변환
- 숫자 0은 False, 그 외 숫자 True
4) str:     문자열형   str(n)      문자열변환
- 문자열 인덱싱(indexing)
- 문자열 슬라이싱(slicing)
- 문자열 연산 : 문자열*숫자, 문자열+문자열
- 관련메소드 : upper(), lower(), title(), count(), starswith(), endswith(), split(), zfill()
   https://docs.python.org/ko/3/library/stdtypes.html
5) complex: 복소수형   complex(n1,n2) -> n1실수, n2허수
- 변수명.real 복소수중 실수
- 변수명.imag 복소수중 허수
- 변수명.conjugate() 켤레 복소수


* 자료형 확인 함수 type()
* 파이썬은 변수에 값을 저장하기 전 변수의 자료형을 미리 지정할 필요 없음
'''

# a = 1
# b = 3.14
# c = True
# d = "python"
# e = '100'
# f = "010-2746-8762"
# g = 2 + 5j
# print(type(a), type(b), type(c), type(d), type(e), type(f), type(g))

# print(int(b))
# print(a+float(e))
# print(str(b)+e)

# boot = True
# print(boot, type(boot))
# boof = False
# print(boof, type(boof))
# print(2 > 5)
# print(0 < 0)
# print('안녕' == '안녕')
# print(bool(0))
# print(bool(3))

# print(d[0], d[1], d[2], d[3], d[4], d[5]) # 문자열 인덱싱 (정방향인덱스)
# print(d[-1], d[-2], d[-3], d[-4], d[-5], d[-6]) # 문자열 인덱싱 (역방향인덱스)
# print(d[3]==d[-3])
# print(d[0:5:2]) # s[start:stop:step] 문자열 슬라이싱
# print(f[4:8]) # 전화번호 중 2746만 추출

# comp1 = 2 + 5j
# print('변수 comp1의 자료형은', type(comp1))
# comp2 = complex(3, -6)
# print('복소수 comp2의 값은', comp2)
# print('실수 부분은', comp2.real)
# print('허수 부순은', comp2.imag)
# print('켤레 복소수는', comp2.conjugate())