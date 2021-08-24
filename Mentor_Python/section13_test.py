# 1번 문제풀이
nation = ['그리스', '아테네', '독일', '베를린', '러시아', '모스크바', \
          '미국', '워싱턴', '대한민국', '서울', '중국', '베이징', \
          '일본', '동경', '북한', '평양', '캐나다', '오타와']
file = open('nation.txt', 'wt')
n = 0
while n < len(nation):
    file.write(nation[n] + '-')
    file.write(nation[n+1] + '\n')
    n += 2
file.close()

print('생성된 nation.txt 파일의 내용은 다음과 같습니다.')
file = open('nation.txt', 'rt')
str = file.read()
print(str, end='')
file.close()

# # 첫 번째 풀이
# nation = ['그리스', '아테네', '독일', '베를린', '러시아', '모스크바', '미국', '워싱턴']
# file = open('nation.txt', 'wt')
# for i in range(0, len(nation), 2):
#     file.write('{}-{}\n'.format(nation[i], nation[i + 1]))
# file.close()
#
# print('생성된 nation.txt 파일의 내용은 다음과 같습니다.')
# file = open('nation.txt', 'rt')
# line_list = file.readlines()
# for line in line_list:
#     print(line, end='')
# file.close()

# # 두 번째 풀이
# nation = ['그리스', '아테네', '독일', '베를린', '러시아', '모스크바', '미국', '워싱턴']
# file = open('nation.txt', 'wt')
# for i, country in enumerate(nation):
#     if i % 2 == 0:
#         file.write('{}-{}\n'.format(nation[i], nation[i + 1]))
# file.close()
#
# print('생성된 nation.txt 파일의 내용은 다음과 같습니다.')
# file = open('nation.txt', 'rt')
# line_list = file.readlines()
# for line in line_list:
#     print(line, end='')
# file.close()



# 2번 문제풀이
file = open('연락처.txt', 'rt')
contact = file.read()
num = contact.count('011')
print('총 {}건의 011 데이터를 찾았습니다.'.format(num))

file = open('연락처.txt', 'wt')
file.write(contact.replace('011', '010'))
print('모든 데이터를 수정했습니다.')

file.close()

# #정답
# prev_file = open('연락처.txt', 'rt')
# buffer = prev_file.read()
# n = buffer.count('"011-')
# buffer = buffer.replace('"011-', '"010-')
# print('총 {}건의 011 데이터를 찾았습니다.'.format(n))
# prev_file.close()
#
# new_file = open('연락처.txt', 'wt')
# new_file.write(buffer)
# new_file.close()
# print('모든 데이터를 수정했습니다.')

## 연락처.txt
##"김나라", "목포시", "011-1111-1111"
##"이나라", "서울시", "011-2222-2222"
##"오나라", "전주시", "010-3333-3333"
##"정나라", "속초시", "011-4444-4444"
##"유나라", "제주시", "010-5555-5555"