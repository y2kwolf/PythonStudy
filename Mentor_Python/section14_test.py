# 1번 문제풀이
# copy_file = input('복사할 파일명을 입력하세요>>> ')
# if copy_file == '1.txt':
#     with open('1.txt', 'rt') as file:
#         with open('1-복사본.txt', 'wt') as copy:
#             copy.write(file.read())
#             print('1-복사본.txt 파일이 생성되었습니다.')
# else:
#     print('복사할 수 없는 파일입니다.')

# 정답
# while True:
#     filename = input('복사할 파일명을 입력하세요 >>> ')
#     extname = filename[filename.rfind('.') + 1:]
#     if extname != 'txt':
#         print('복사할 수 없는 파일입니다.')
#     else:
#         break
#
# with open(filename, 'rt') as source:
#     with open('복사본-' + filename, 'wt') as copy:
#         while True:
#             buffer = source.read(1)
#             if not buffer:
#                 break
#             copy.write(buffer)
#
# print('복사본-' + filename + '파일이 생성되었습니다.')

# 2번 문제풀이
# import csv
# with open('cctv.csv', 'r', newline='') as file:
#     csv_reader = csv.reader(file, delimiter=',')
#     totalcctv = 0
#     for i, line in enumerate(csv_reader):
#         if i != 0:
#             totalcctv += int(line[4])
# print('서울특별시 마포구에 설치된 CCTV는 총 {}대입니다.'.format(totalcctv))

# 정답
# import csv
# with open('cctv.csv', 'r') as csvfile:
#     buffer = csv.reader(csvfile, delimiter=',', quotechar='"')
#     totalcctv = 0
#     for i, line in enumerate(buffer):
#         if i != 0:
#             totalcctv += int(line[4])
# print('서울특별시 마포구에 설치된 CCTV는 총 {}대입니다.'.format(totalcctv))

# 3번 문제풀이
# import json
# with open('cctv.json', 'r', encoding='utf-8') as file:
#     json_reader = file.read()
#     cctv_list = json.loads(json_reader)
#     cctv_purpose = set()
#     for place in cctv_list:
#         cctv_purpose.add(place['설치목적구분'])
# print(cctv_purpose)

# 정답
# import json
#
# with open('cctv.json', 'r', encoding='utf-8') as jsonfile:
#     buffer = jsonfile.read()
#     cctv_list = json.loads(buffer)
#     cctv_purpose = set()
#     for place in cctv_list:
#         cctv_purpose.add(place['설치목적구분'])
# print(cctv_purpose)