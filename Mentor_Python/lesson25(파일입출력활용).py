'''
개요: 파일 입출력의 활용
작성자: 진상영
작성일: 2021.04.13
내용:
1) 파일복사
2) CSV(Comma Separated Values) 파일 입출력
3) JSON(JavaScript Object Notation) 파일 입출력
'''

# buffer_size = 1024
# with open('code.mp4', 'rb') as source:
#     with open('code2.mp4', 'wb') as copy:
#         while True:
#             buffer = source.read(buffer_size)
#             if not buffer:
#                 break
#             copy.write(buffer)
# print('code2.mp4 파일이 복사되었습니다')

# student_list = []
# with open('학생명단.csv', 'rt') as file:
#     file.readline()
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         student = line.split(',')
#         student_list.append(student)
# print(student_list)

# member_list = []
# with open('회원명단.csv', 'rt') as file:
#     file.readline()
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         member = line.split(',')
#         member[0] = member[0].strip('"')
#         member_list.append(member)
# print(member_list)

# import csv
# with open('차량관리.csv', 'w', newline='') as file:
#     csv_maker = csv.writer(file, delimiter=',', quotechar='"')
#     csv_maker.writerow([1, '08러1234', '2020-10-20,14:00'])
#     csv_maker.writerow([2, '25다1234', '2020-10-20,14:10'])
#     csv_maker.writerow([3, '28하1234', '2020-10-20,14:20'])
# print('차량관리.csv 파일이 생성되었습니다.')

# import csv
# with open('차량관리.csv', 'r', newline='') as file:
#     csv_reader = csv.reader(file, delimiter=',', quotechar='"')
#     for line in csv_reader:
#         print(line)

# import json
# dict_list = [
#     {
#         'name': 'james',
#         'age': 20,
#         'spec': [
#             175.5,
#             70.5
#         ]
#     },
#     {
#         'name': 'alice',
#         'age': 21,
#         'spec': [
#             168.5,
#             60.5
#         ]
#     }
# ]
# json_string = json.dumps(dict_list, indent=4) # indent옵션 추가 그대로 출력, 불필요한 공백 생성, 가능한 사용X
# with open('dictList.json', 'w') as file:
#     file.write(json_string)
# print('dictList.json 파일이 생성되었습니다.')

# import json
# with open('dictList.json', 'r') as file:
#     json_reader = file.read()
#     dict_list = json.loads(json_reader)
# for dic in dict_list:
#     print('이름: {}'.format(dic['name']))
#     print('나이: {}'.format(dic['age']))
#     print('키: {}'.format(dic['spec'][0]))
#     print('몸무게: {}'.format(dic['spec'][1]))
#     print()