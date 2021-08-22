import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'config.settings')
django.setup()

from index.models import FashionScore, FashionScore_musinsa, FashionScore_seoulstore, FashionScore_ssf

reviewDate = [0] * 12
category = 0


def save_FashionScore():
    for i in range(category):
        reviewDate[0] = FashionScore_musinsa[i]['Jan'] + FashionScore_seoulstore[i]['Jan'] + FashionScore_ssf[i]['Jan']
        reviewDate[1] = FashionScore_musinsa[i]['Feb'] + FashionScore_seoulstore[i]['Feb'] + FashionScore_ssf[i]['Feb']
        reviewDate[2] = FashionScore_musinsa[i]['Mar'] + FashionScore_seoulstore[i]['Mar'] + FashionScore_ssf[i]['Mar']
        reviewDate[3] = FashionScore_musinsa[i]['Apr'] + FashionScore_seoulstore[i]['Apr'] + FashionScore_ssf[i]['Apr']
        reviewDate[4] = FashionScore_musinsa[i]['May'] + FashionScore_seoulstore[i]['May'] + FashionScore_ssf[i]['May']
        reviewDate[5] = FashionScore_musinsa[i]['June'] + FashionScore_seoulstore[i]['June'] + FashionScore_ssf[i]['June']
        reviewDate[6] = FashionScore_musinsa[i]['July'] + FashionScore_seoulstore[i]['July'] + FashionScore_ssf[i]['July']
        reviewDate[7] = FashionScore_musinsa[i]['Aug'] + FashionScore_seoulstore[i]['Aug'] + FashionScore_ssf[i]['Aug']
        reviewDate[8] = FashionScore_musinsa[i]['Sep'] + FashionScore_seoulstore[i]['Sep'] + FashionScore_ssf[i]['Sep']
        reviewDate[9] = FashionScore_musinsa[i]['Oct'] + FashionScore_seoulstore[i]['Oct'] + FashionScore_ssf[i]['Oct']
        reviewDate[10] = FashionScore_musinsa[i]['Nov'] + FashionScore_seoulstore[i]['Nov'] + FashionScore_ssf[i]['Nov']
        reviewDate[11] = FashionScore_musinsa[i]['Dec'] + FashionScore_seoulstore[i]['Dec'] + FashionScore_ssf[i]['Dec']

        copied_list = sorted(reviewDate, reverse=True)

        month_1 = reviewDate.index(copied_list[0]) + 1
        month_2 = reviewDate.index(copied_list[1]) + 1
        month_3 = reviewDate.index(copied_list[2]) + 1

        FashionScore(
            Jan=reviewDate[0],
            Feb=reviewDate[1],
            Mar=reviewDate[2],
            Apr=reviewDate[3],
            May=reviewDate[4],
            June=reviewDate[5],
            July=reviewDate[6],
            Aug=reviewDate[7],
            Sep=reviewDate[8],
            Oct=reviewDate[9],
            Nov=reviewDate[10],
            Dec=reviewDate[11],
            month_1=month_1,
            month_2=month_2,
            month_3=month_3,
        ).save()


save_FashionScore()
