# # 1번 문제풀이
# a = '31025'
# print(a[0:1] + "학년 " + a[1:3] + "반 " + a[3:5] + "번")
# # 정답
# student = '31025'
# grade_no = student[0]
# class_no = student[1:3]
# stu_no = student[3:]  # stu_no = student[-2:] 도 가능합니다.
# print(grade_no, '학년', class_no, '반', stu_no, '번')
#
# # 2번 문제풀이
# car_no = ['서울2가1234', '10가4567', '19누8362']
# car1 = car_no[0]
# car2 = car_no[1]
# car3 = car_no[2]
# print(car1 + "의 차량번호 4자리는 " + car1[-4:] + '입니다.')
# print(car2 + "의 차량번호 4자리는 " + car2[-4:] + '입니다.')
# print(car3 + "의 차량번호 4자리는 " + car3[-4:] + '입니다.')
# # 정답
# car1 = '서울2가1234'
# car2 = '10가1234'
# car3 = '288가1234'
# car_no1 = car1[-4:]
# car_no2 = car2[-4:]
# car_no3 = car3[-4:]
# print(car1, '의 차량번호 4자리는', car_no1, '입니다.')
# print(car2, '의 차량번호 4자리는', car_no2, '입니다.')
# print(car3, '의 차량번호 4자리는', car_no3, '입니다.')
#
# 3번 문제풀이
s = 'maple'
cent_char = int(len(s)/2) # or cent_char = len(s)//2
print(s + "의 가운데 글자는 \'" + s[cent_char] + "\'" + "입니다.")
# 정답
s = 'maple'
middle = s[len(s) // 2]
print(s, '의 가운데 글자는', middle, '입니다.')
#
# # 4번 문제풀이
# li = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print('3번째 요소부터 7번째 요소 = ', li[2:7])
# print('3번째 요소부터 7번째 요소 중 2번째 요소 = ', li[3])
# # 정답
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print('3번째 요소부터 7번째 요소 =', my_list[2:7])
# print('3번째 요소부터 7번째 요소 중 2번째 요소 =', my_list[2:7][1])
#
# # 5번 문제풀이
# china_food = {'금요일':'탕수육', '토요일':'유산슬', '일요일':'팔보채'}
# print('금요일 : ', china_food['금요일'])
# print('토요일 : ', china_food['토요일'])
# print('일요일 : ', china_food['일요일'])
# # 정답
# menu = {
#     '금': '탕수육',
#     '토': '유산슬',
#     '일': '팔보채'
#     }
# print('금요일 :', menu['금'])
# print('토요일 :', menu['토'])
# print('일요일 :', menu['일'])