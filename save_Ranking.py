import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'config.settings')
django.setup()

from index.models import Ranking_outer, FashionScore_musinsa, FashionScore_seoulstore, FashionScore_ssf


def save_Ranking(product):
    if product == "shirt":
        product_code = 0
        Ranking_outer(
            ranking_name="셔츠",
            ranking_img="shirt.jpg",
            ranking_score=FashionScore_musinsa[product_code]['ranking_score`'] + FashionScore_seoulstore[product_code][
                'ranking_score'] +
                          FashionScore_ssf[product_code]['ranking_score']
        ).save()
    elif product == "coat":
        product_code = 1
        Ranking_outer(
            ranking_name="코트",
            ranking_img="coat.jpg",
            ranking_score=FashionScore_musinsa[product_code]['ranking_score`'] + FashionScore_seoulstore[product_code][
                'ranking_score'] +
                          FashionScore_ssf[product_code]['ranking_score']
        ).save()


print("랭킹을 저장하고자 하는 품목을 영어로 입력해주세요")
product = input()
save_Ranking(product)
