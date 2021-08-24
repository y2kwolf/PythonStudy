# # 1번 문제풀이
# rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
#
# for no, color in enumerate(rainbow):
#     print('무지개의 {}번째 색은 {}입니다'.format(no+1, color))
# # 정답
# # 첫 번째 풀이입니다.
# rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
# for no, color in enumerate(rainbow):
#     print('무지개의 {}번째 색은 {}입니다.'.format(no + 1, color))
# print()
# # 두 번째 풀이입니다.
# for idx in range(len(rainbow)):
#     print('무지개의 {}번째 색은 {}입니다.'.format(idx + 1, rainbow[idx]))

# 2번 문제풀이
print('점수를 입력하세요. 더 이상 입력할 점수가 없으면 음수를 아무거나 입력하세요.')
scores = []
while True:
    score = int(input('점수 입력>>> '))
    if score < 0:
        break
    else:
        scores.append(score)

print('평균 = {}, 최대 = {}, 최소 = {}'.format(sum(scores)/len(scores), max(scores), min(scores)))
# # 정답
# exam = []
# print('점수를 입력하세요.')
# print('더 이상 입력할 점수가 없으면 음수를 아무거나 입력하세요.')
# while True:
#     score = int(input('점수 입력 >>> '))
#     if score < 0:
#         break
#     else:
#         exam.append(score)
# average = sum(exam) / len(exam)
# maximum = max(exam)
# minimum = min(exam)
# print('평균 = {}, 최대 = {}, 최소 = {}'.format(average, maximum, minimum))
