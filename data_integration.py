import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'config.settings')
django.setup()

from index.models import *

reviewDate = [0] * 12
category = 0
year = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def save_FashionScore(product):
    if product == "트렌치코트":
        product_id = 1
        for i in range(len(year)):
            reviewDate[i] = FashionScore_musinsa_trench_coat[product_id - 1]["\'" + year[i] + "\'"] + \
                            FashionScore_seoulstore_trench_coat[product_id - 1]["\'" + year[i] + "\'"] + \
                            FashionScore_ssf_trench_coat[product_id - 1]["\'" + year[i] + "\'"]

        copied_list = sorted(reviewDate, reverse=True)
        month_1 = reviewDate.index(copied_list[0]) + 1
        month_2 = reviewDate.index(copied_list[1]) + 1
        month_3 = reviewDate.index(copied_list[2]) + 1
        FashionScore_trench_coat(
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

def save_Ranking(product):
    if product == "트렌치코트":
        product_id = 1
        Ranking(
            ranking_name=product,
            ranking_img=product + ".jpg",
            ranking_score=FashionScore_musinsa_trench_coat[product_id - 1]['ranking_score`'] +
                          FashionScore_seoulstore_trench_coat[product_id - 1][
                              'ranking_score'] + FashionScore_ssf_trench_coat[product_id - 1]['ranking_score']
        ).save()

    elif product == "":
        pass

# product = input()
# save_FashionScore(product)
# save_Ranking(product)
