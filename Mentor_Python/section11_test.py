# # 1번 문제풀이
# def vending_machine(money):
#     for ea in range(0, money//700+1):
#         print('음료수 = {}개, 잔돈 = {}원'.format(ea, money))
#         money -= 700
#
# vending_machine(1500)

# # 2번 문제풀이
# def get_average(marks):
#     score = []
#     for key in marks:
#         score.append(marks[key])
#     return sum(score)/len(marks)
#
# marks = {'국어':90, '영어':80, '수학':85, '과학':100}
# average = get_average(marks)
# print('평균은 {}점입니다.'.format(average))

# # 3번 문제풀이
# total = 0
# def gift(dic, who, money):
#     # dic.setdefault(who,money) # 딕셔너리에 키와 값 추가
#     dic[who] = money
#     global total # 전역변수 사용을 위해 global 키워드 사용
#     total += money
#     return dic
#
# wedding = {}
# gift(wedding, '영희', 5)
# gift(wedding, '철수', 3)
# gift(wedding, '이모', 10)
# print('축의금 명단: {}'.format(wedding))
# print('전체 축의금: {}'.format(total))

