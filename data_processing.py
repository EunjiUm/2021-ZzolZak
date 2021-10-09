import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'config.settings')
django.setup()
from datetime import datetime
from index.models import *

origin_list = [0] * 12

print("리뷰를 선택하세요. 예) musinsa trench_coat")
company, product=map(str, input().split())
print("좋아요 개수를 입력하세요.")
like=int(input())
with open("data/" + company + "_" + product + ".txt", 'r', encoding='utf-8') as f:
    list_file = []
    for line in f:
        list_file.append(line.replace('\n', ''))

# 중복된 리뷰 제거
list_file = list(set(list_file))

for txt in list_file:
    if txt[-3].isdigit() and txt[-4].isdigit():
        origin_list[int(txt[-4]+txt[-3])-1]+=1
    elif txt[-3].isdigit() and not txt[-4].isdigit():
        origin_list[int(txt[-3])-1]+=1

copied_list = sorted(origin_list, reverse=True)
month_1 = origin_list.index(copied_list[0]) + 1

# 계절지수 계산
month_list = [0] * 12
if month_1 <= 5:
    month_list[0] = month_1 + 7
else:
    month_list[0] = month_1 - 5

for i in range(1, len(month_list)):
    if month_list[i - 1] == 12:
        month_list[i] = month_list[i - 1] - 11
    else:
        month_list[i] = month_list[i - 1] + 1

# 계절 지수 값의 범위 : -6 <= season_score <= 0
season_score = -(abs(month_list.index(month_1) - month_list.index(datetime.today().month)))

# 각종 데이터 DB에 저장
if company == "musinsa":
    if product == "trench_coat":
        FashionScore_musinsa_trench_coat(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_trench_coat(
                review=list_file[i]
            ).save()
    elif product == "coat":
        FashionScore_musinsa_coat(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_coat(
                review=list_file[i]
            ).save()
    elif product == "padded_jacket":
        FashionScore_musinsa_padded_jacket(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_padded_jacket(
                review=list_file[i]
            ).save()
    elif product == "military":
        FashionScore_musinsa_military(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_military(
                review=list_file[i]
            ).save()
    elif product == "blazer":
        FashionScore_musinsa_blazer(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_blazer(
                review=list_file[i]
            ).save()
    elif product == "leather_jacket":
        FashionScore_musinsa_leather_jacket(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_leather_jacket(
                review=list_file[i]
            ).save()
    elif product == "fur_jacket":
        FashionScore_musinsa_fur_jacket(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_fur_jacket(
                review=list_file[i]
            ).save()
    elif product == "short_sleeve_jacket":
        FashionScore_musinsa_short_sleeve_jacket(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_short_sleeve_jacket(
                review=list_file[i]
            ).save()
    elif product == "long_sleeve_jacket":
        FashionScore_musinsa_long_sleeve_jacket(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_long_sleeve_jacket(
                review=list_file[i]
            ).save()
    elif product == "shirt":
        FashionScore_musinsa_shirt(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_shirt(
                review=list_file[i]
            ).save()
    elif product == "blouse":
        FashionScore_musinsa_blouse(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_blouse(
                review=list_file[i]
            ).save()
    elif product == "neat":
        FashionScore_musinsa_neat(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_neat(
                review=list_file[i]
            ).save()
    elif product == "hoodie":
        FashionScore_musinsa_hoodie(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_hoodie(
                review=list_file[i]
            ).save()
    elif product == "sweat_shirt":
        FashionScore_musinsa_sweat_shirt(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_sweat_shirt(
                review=list_file[i]
            ).save()
    elif product == "denim_pants":
        FashionScore_musinsa_denim_pants(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_denim_pants(
                review=list_file[i]
            ).save()
    elif product == "mini_skirt":
        FashionScore_musinsa_mini_skirt(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_mini_skirt(
                review=list_file[i]
            ).save()
    elif product == "skirt":
        FashionScore_musinsa_skirt(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_skirt(
                review=list_file[i]
            ).save()
    elif product == "slacks":
        FashionScore_musinsa_slacks(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_slacks(
                review=list_file[i]
            ).save()
    elif product == "short_pants":
        FashionScore_musinsa_short_pants(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_short_pants(
                review=list_file[i]
            ).save()
    elif product == "sports_wear":
        FashionScore_musinsa_sports_wear(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_sports_wear(
                review=list_file[i]
            ).save()
    elif product == "leggings":
        FashionScore_musinsa_leggings(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_leggings(
                review=list_file[i]
            ).save()
    elif product == "sports_shoes":
        FashionScore_musinsa_sports_shoes(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_sports_shoes(
                review=list_file[i]
            ).save()
    elif product == "sandal":
        FashionScore_musinsa_sandal(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_sandal(
                review=list_file[i]
            ).save()
    elif product == "heel":
        FashionScore_musinsa_heel(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_heel(
                review=list_file[i]
            ).save()
    elif product == "loafers":
        FashionScore_musinsa_loafers(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_loafers(
                review=list_file[i]
            ).save()
    elif product == "walker":
        FashionScore_musinsa_walker(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_walker(
                review=list_file[i]
            ).save()
    elif product == "dress":
        FashionScore_musinsa_dress(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_dress(
                review=list_file[i]
            ).save()
    elif product == "back_pack":
        FashionScore_musinsa_back_pack(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_back_pack(
                review=list_file[i]
            ).save()
    elif product == "tote_bag":
        FashionScore_musinsa_tote_bag(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_tote_bag(
                review=list_file[i]
            ).save()
    elif product == "clutch_bag":
        FashionScore_musinsa_clutch_bag(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_clutch_bag(
                review=list_file[i]
            ).save()
    elif product == "shoulder_bag":
        FashionScore_musinsa_shoulder_bag(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_shoulder_bag(
                review=list_file[i]
            ).save()
    elif product == "eco_bag":
        FashionScore_musinsa_eco_bag(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_musinsa_eco_bag(
                review=list_file[i]
            ).save()

elif company == "seoulstore":
    if product == "trench_coat":
        FashionScore_seoulstore_trench_coat(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_trench_coat(
                review=list_file[i]
            ).save()
    elif product == "coat":
        FashionScore_seoulstore_coat(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_coat(
                review=list_file[i]
            ).save()
    elif product == "padded_jacket":
        FashionScore_seoulstore_padded_jacket(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_padded_jacket(
                review=list_file[i]
            ).save()
    elif product == "military":
        FashionScore_seoulstore_military(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_military(
                review=list_file[i]
            ).save()
    elif product == "blazer":
        FashionScore_seoulstore_blazer(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_blazer(
                review=list_file[i]
            ).save()
    elif product == "leather_jacket":
        FashionScore_seoulstore_leather_jacket(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_leather_jacket(
                review=list_file[i]
            ).save()
    elif product == "fur_jacket":
        FashionScore_seoulstore_fur_jacket(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_fur_jacket(
                review=list_file[i]
            ).save()
    elif product == "short_sleeve_jacket":
        FashionScore_seoulstore_short_sleeve_jacket(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_short_sleeve_jacket(
                review=list_file[i]
            ).save()
    elif product == "long_sleeve_jacket":
        FashionScore_seoulstore_long_sleeve_jacket(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_long_sleeve_jacket(
                review=list_file[i]
            ).save()
    elif product == "shirt":
        FashionScore_seoulstore_shirt(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_shirt(
                review=list_file[i]
            ).save()
    elif product == "blouse":
        FashionScore_seoulstore_blouse(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_blouse(
                review=list_file[i]
            ).save()
    elif product == "neat":
        FashionScore_seoulstore_neat(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_neat(
                review=list_file[i]
            ).save()
    elif product == "hoodie":
        FashionScore_seoulstore_hoodie(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_hoodie(
                review=list_file[i]
            ).save()
    elif product == "sweat_shirt":
        FashionScore_seoulstore_sweat_shirt(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_sweat_shirt(
                review=list_file[i]
            ).save()
    elif product == "denim_pants":
        FashionScore_seoulstore_denim_pants(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_denim_pants(
                review=list_file[i]
            ).save()
    elif product == "mini_skirt":
        FashionScore_seoulstore_mini_skirt(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_mini_skirt(
                review=list_file[i]
            ).save()
    elif product == "skirt":
        FashionScore_seoulstore_skirt(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_skirt(
                review=list_file[i]
            ).save()
    elif product == "slacks":
        FashionScore_seoulstore_slacks(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_slacks(
                review=list_file[i]
            ).save()
    elif product == "short_pants":
        FashionScore_seoulstore_short_pants(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_short_pants(
                review=list_file[i]
            ).save()
    elif product == "sports_wear":
        FashionScore_seoulstore_sports_wear(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_sports_wear(
                review=list_file[i]
            ).save()
    elif product == "leggings":
        FashionScore_seoulstore_leggings(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_leggings(
                review=list_file[i]
            ).save()
    elif product == "sports_shoes":
        FashionScore_seoulstore_sports_shoes(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_sports_shoes(
                review=list_file[i]
            ).save()
    elif product == "sandal":
        FashionScore_seoulstore_sandal(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_sandal(
                review=list_file[i]
            ).save()
    elif product == "heel":
        FashionScore_seoulstore_heel(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_heel(
                review=list_file[i]
            ).save()
    elif product == "loafers":
        FashionScore_seoulstore_loafers(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_loafers(
                review=list_file[i]
            ).save()
    elif product == "walker":
        FashionScore_seoulstore_walker(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_walker(
                review=list_file[i]
            ).save()
    elif product == "dress":
        FashionScore_seoulstore_dress(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_dress(
                review=list_file[i]
            ).save()
    elif product == "back_pack":
        FashionScore_seoulstore_back_pack(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_back_pack(
                review=list_file[i]
            ).save()
    elif product == "tote_bag":
        FashionScore_seoulstore_tote_bag(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_tote_bag(
                review=list_file[i]
            ).save()
    elif product == "clutch_bag":
        FashionScore_seoulstore_clutch_bag(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_clutch_bag(
                review=list_file[i]
            ).save()
    elif product == "shoulder_bag":
        FashionScore_seoulstore_shoulder_bag(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_shoulder_bag(
                review=list_file[i]
            ).save()
    elif product == "eco_bag":
        FashionScore_seoulstore_eco_bag(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_seoulstore_eco_bag(
                review=list_file[i]
            ).save()

elif company == "ssf":
    if product == "trench_coat":
        FashionScore_ssf_trench_coat(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_trench_coat(
                review=list_file[i]
            ).save()
    elif product == "coat":
        FashionScore_ssf_coat(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_coat(
                review=list_file[i]
            ).save()
    elif product == "padded_jacket":
        FashionScore_ssf_padded_jacket(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_padded_jacket(
                review=list_file[i]
            ).save()
    elif product == "military":
        FashionScore_ssf_military(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_military(
                review=list_file[i]
            ).save()
    elif product == "blazer":
        FashionScore_ssf_blazer(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_blazer(
                review=list_file[i]
            ).save()
    elif product == "leather_jacket":
        FashionScore_ssf_leather_jacket(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_leather_jacket(
                review=list_file[i]
            ).save()
    elif product == "fur_jacket":
        FashionScore_ssf_fur_jacket(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_fur_jacket(
                review=list_file[i]
            ).save()
    elif product == "short_sleeve_jacket":
        FashionScore_ssf_short_sleeve_jacket(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_short_sleeve_jacket(
                review=list_file[i]
            ).save()
    elif product == "long_sleeve_jacket":
        FashionScore_ssf_long_sleeve_jacket(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_long_sleeve_jacket(
                review=list_file[i]
            ).save()
    elif product == "shirt":
        FashionScore_ssf_shirt(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_shirt(
                review=list_file[i]
            ).save()
    elif product == "blouse":
        FashionScore_ssf_blouse(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_blouse(
                review=list_file[i]
            ).save()
    elif product == "neat":
        FashionScore_ssf_neat(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_neat(
                review=list_file[i]
            ).save()
    elif product == "hoodie":
        FashionScore_ssf_hoodie(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_hoodie(
                review=list_file[i]
            ).save()
    elif product == "sweat_shirt":
        FashionScore_ssf_sweat_shirt(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_sweat_shirt(
                review=list_file[i]
            ).save()
    elif product == "denim_pants":
        FashionScore_ssf_denim_pants(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_denim_pants(
                review=list_file[i]
            ).save()
    elif product == "mini_skirt":
        FashionScore_ssf_mini_skirt(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_mini_skirt(
                review=list_file[i]
            ).save()
    elif product == "skirt":
        FashionScore_ssf_skirt(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_skirt(
                review=list_file[i]
            ).save()
    elif product == "slacks":
        FashionScore_ssf_slacks(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_slacks(
                review=list_file[i]
            ).save()
    elif product == "short_pants":
        FashionScore_ssf_short_pants(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_short_pants(
                review=list_file[i]
            ).save()
    elif product == "sports_wear":
        FashionScore_ssf_sports_wear(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_sports_wear(
                review=list_file[i]
            ).save()
    elif product == "leggings":
        FashionScore_ssf_leggings(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_leggings(
                review=list_file[i]
            ).save()
    elif product == "sports_shoes":
        FashionScore_ssf_sports_shoes(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_sports_shoes(
                review=list_file[i]
            ).save()
    elif product == "sandal":
        FashionScore_ssf_sandal(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_sandal(
                review=list_file[i]
            ).save()
    elif product == "heel":
        FashionScore_ssf_heel(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_heel(
                review=list_file[i]
            ).save()
    elif product == "loafers":
        FashionScore_ssf_loafers(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_loafers(
                review=list_file[i]
            ).save()
    elif product == "walker":
        FashionScore_ssf_walker(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_walker(
                review=list_file[i]
            ).save()
    elif product == "dress":
        FashionScore_ssf_dress(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_dress(
                review=list_file[i]
            ).save()
    elif product == "back_pack":
        FashionScore_ssf_back_pack(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_back_pack(
                review=list_file[i]
            ).save()
    elif product == "tote_bag":
        FashionScore_ssf_tote_bag(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_tote_bag(
                review=list_file[i]
            ).save()
    elif product == "clutch_bag":
        FashionScore_ssf_clutch_bag(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_clutch_bag(
                review=list_file[i]
            ).save()
    elif product == "shoulder_bag":
        FashionScore_ssf_shoulder_bag(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_shoulder_bag(
                review=list_file[i]
            ).save()
    elif product == "eco_bag":
        FashionScore_ssf_eco_bag(
            Jan=origin_list[0],
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
            ranking_score=like // len(list_file) * season_score
        ).save()
        for i in range(len(list_file)):
            Review_ssf_eco_bag(
                review=list_file[i]
            ).save()

print("크롤링 데이터 저장 종료")
