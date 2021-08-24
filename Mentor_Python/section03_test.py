
# 1번 문제풀이
f1 = float(input('첫번째 실수를 입력하세요>>>'))
f2 = float(input('두번째 실수를 입력하세요>>>'))

print('{}와 {}의 합은 {}입니다.'.format(f1, f2, f1+f2))

# 정답
a = float(input('첫 번째 실수를 입력하세요 >>> '))
b = float(input('두 번째 실수를 입력하세요 >>> '))
total = a + b
print('{}와 {}의 합은 {}입니다.'.format(a, b, total))

# 2번 문제풀이
month = int(input('1~12 사이의 월을 입력하세요>>>'))
mday = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print('{}월은 {}일까지 있습니다.'.format(month,mday[month-1]))

# 정답
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = int(input('1~12 사이의 월을 입력하세요 >>> '))
day = days[month - 1]
print('{}월은 {}일까지 있습니다.'.format(month, day))

# 3번 문제풀이
english_dict = {  # 딕셔너리 자료구조 저장
    'flower':'꽃',
    'fly':'날다',
    'floor':'바닥',
    'wolf':'늑대'
}

word = input('영어 단어를 입력하세요>>>')
rword = word.strip()  # 공백제거함수 string.strip()

print('{}: {}'.format(word, english_dict[rword]))

# 정답
english_dict = {
    'flower': '꽃',
    'fly': '날다',
    'floor': '바닥'
}
word = input('영어 단어를 입력하세요 >>> ')
print('{}: {}'.format(word, english_dict[word]))

# 4번 문제풀이
travel1 = input('희망하는 수학여행지를 입력하세요>>>')
travel2 = input('희망하는 수학여행지를 입력하세요>>>')
travel3 = input('희망하는 수학여행지를 입력하세요>>>')

ftravel = {travel1,travel2,travel3} # set 자료구조 저장으로 중복값 저장 방지

print('조사된 수학여행지는 {}입니다.'.format(ftravel))

# 정답
s = set()
s.add(input('희망하는 수학여행지를 입력하세요 >>> '))
s.add(input('희망하는 수학여행지를 입력하세요 >>> '))
s.add(input('희망하는 수학여행지를 입력하세요 >>> '))
print('조사된 수학여행지는 {}입니다.'.format(s))