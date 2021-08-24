'''
개요: 특수문자(escape character)
작성자: 진상영
작성일: 2021.03.08
내용:
1) 이스케이프 문자(확장문자)
\'  작은따옴표
\"  큰따옴표
\n  줄바꿈
\r  캐리지 리턴
\t  탭
\v  수직 탭
\\  역슬래시
\a  벨
\b  백스페이스

2) 여러 줄 문자열
3) 문자열 연산
4) 문자열 인덱싱과 슬라이싱
5) 문자열 메소드

* 문자열을 구성하는 문자들은 다른 것으로 변경 불가능
* 문자열 관련 메소드 이용은 결과만 생성, 원본 문자열이 바뀌지 않음
'''

# print('Hello \'World\'')
# print("Hello 'World'")
# print('Hello \"World\"')
# print('*\n**\n***')
# print('이름\t연락처')
# print('진상영\t010-2746-8762')
# print('서승미\t010-7400-8762')

# text = '나는 문자열이다. \n줄바꿈하려면 특수문자열을 써야하고, \
# \n특수문자열을 사용하면 \t탭도 가능하다.'
# print(text)
# multiText = '''
# 여러 줄 문자열을 사용하면
# 여기 보이는 그대로 출력된다.
# 줄바꿈이나 탭이나 공백도 그대로이다.
#     큰 따옴표 세 개(""")를 사용해도
#     같은 결과를 얻을 수 있다.
#     물론 다양한 특수문자도 (*(!&#)(*@&$)도
#     그대로 출력된다.
# '''
# print(multiText)

# print("=" * 40)
# print('Python은 ' + '훌륭한 프로그래밍 언어이다')
# head = 'Python은'
# tail = '훌륭한 프로그래밍 언어이다'
# string = head + tail
# print(string)
# str1 = '꿈'
# str2 = '과'
# str3 = '도'
# str4 = '전'
# print(str1 + str2 + " " + str3 + str4)
# print("=" * 40)

str = "PYTHON"
print(str[0], str[2], str[4])
print(str[-1], str[-3], str[-5])
print(str[0:5])
print(str[2:5])
print(str[2:])
print(str[:2])
print(str[-6:-4])
print(str[-4:])
print(str[:-4])