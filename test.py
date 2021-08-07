import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'config.settings')
import django
django.setup()
from index.models import FashionScore
import random

origin_list = [0]*12
copied_list = [0]*12

for i in range(12):
    rnum = random.randint(0, 100)  # 0부터100까지 추출
    origin_list[i] = rnum

for i in range(len(origin_list)):
    copied_list[i] = origin_list[i]

copied_list.sort(reverse=True)  # 월별로 1씩 증가시킨 리스트를 내림차순으로 정렬

month_1 = origin_list.index(copied_list[0]) + 1
month_2 = origin_list.index(copied_list[1]) + 1
month_3 = origin_list.index(copied_list[2]) + 1

FashionScore(Jan=origin_list[0],
             Feb=origin_list[1],
             Mar=origin_list[2],
             Apr=origin_list[3],
             May=origin_list[4],
             June=origin_list[5],
             July=origin_list[6],
             Aug=origin_list[7],
             Sep=origin_list[8],
             Oct=origin_list[9],
             Nov=origin_list[10],
             Dec=origin_list[11],

             month_1=month_1,
             month_2=month_2,
             month_3=month_3,
             ).save()