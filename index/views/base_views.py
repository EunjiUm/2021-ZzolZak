from django.shortcuts import render

from index.models import *


def intro(request):
    keyword = request.GET.get('kw', '')  # 검색어
    product_list = ['트렌치코트', '코트', '패딩', '밀리터리', '블레이저', '레더재킷', '퍼', '반팔티셔츠', '긴팔티셔츠', '셔츠', '블라우스', '니트', '후드', '맨투맨', '데님팬츠',
                    '미니스커트', '스커트', '슬랙스', '숏팬츠', '트레이닝', '레깅스', '운동화,''샌들', '힐', '로퍼', '워커', '원피스', '백팩', '토트백', '클러치', '숄더백', '에코백']

    if keyword == "트렌치코트":
        musinsa_review_list = Review_musinsa_trench_coat.objects.all()
        seoulstore_review_list = Review_seoulstore_trench_coat.objects.all()
        ssf_review_list = Review_ssf_trench_coat.objects.all()

        month_value = FashionScore_trench_coat.objects.values()
        sent_value = SentValue_trench_coat.objects.values()
        sent_list = SentScore_trench_coat.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "코트":
        musinsa_review_list = Review_musinsa_coat.objects.all()
        seoulstore_review_list = Review_seoulstore_coat.objects.all()
        ssf_review_list = Review_ssf_coat.objects.all()
        month_value = FashionScore_coat.objects.values()
        sent_value = SentValue_coat.objects.values()
        sent_list = SentScore_coat.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "패딩":
        musinsa_review_list = Review_musinsa_padded_jacket.objects.all()
        seoulstore_review_list = Review_seoulstore_padded_jacket.objects.all()
        ssf_review_list = Review_ssf_padded_jacket.objects.all()
        month_value = FashionScore_padded_jacket.objects.values()
        sent_value = SentValue_padded_jacket.objects.values()
        sent_list = SentScore_padded_jacket.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "밀리터리":
        musinsa_review_list = Review_musinsa_military.objects.all()
        seoulstore_review_list = Review_seoulstore_military.objects.all()
        ssf_review_list = Review_ssf_military.objects.all()
        month_value = FashionScore_military.objects.values()
        sent_value = SentValue_military.objects.values()
        sent_list = SentScore_military.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "블레이저":
        musinsa_review_list = Review_musinsa_blazer.objects.all()
        seoulstore_review_list = Review_seoulstore_blazer.objects.all()
        ssf_review_list = Review_ssf_blazer.objects.all()
        month_value = FashionScore_blazer.objects.values()
        sent_value = SentValue_blazer.objects.values()
        sent_list = SentScore_blazer.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "레더재킷":
        musinsa_review_list = Review_musinsa_leather_jacket.objects.all()
        seoulstore_review_list = Review_seoulstore_leather_jacket.objects.all()
        ssf_review_list = Review_ssf_leather_jacket.objects.all()
        month_value = FashionScore_leather_jacket.objects.values()
        sent_value = SentValue_leather_jacket.objects.values()
        sent_list = SentScore_leather_jacket.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "퍼":
        musinsa_review_list = Review_musinsa_fur_jacket.objects.all()
        seoulstore_review_list = Review_seoulstore_fur_jacket.objects.all()
        ssf_review_list = Review_ssf_fur_jacket.objects.all()
        month_value = FashionScore_fur_jacket.objects.values()
        sent_value = SentValue_fur_jacket.objects.values()
        sent_list = SentScore_fur_jacket.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "반팔 티셔츠":
        musinsa_review_list = Review_musinsa_short_sleeve_jacket.objects.all()
        seoulstore_review_list = Review_seoulstore_short_sleeve_jacket.objects.all()
        ssf_review_list = Review_ssf_short_sleeve_jacket.objects.all()
        month_value = FashionScore_short_sleeve_jacket.objects.values()
        sent_value = SentValue_short_sleeve_jacket.objects.values()
        sent_list = SentScore_short_sleeve_jacket.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "긴팔 티셔츠":
        musinsa_review_list = Review_musinsa_long_sleeve_jacket.objects.all()
        seoulstore_review_list = Review_seoulstore_long_sleeve_jacket.objects.all()
        ssf_review_list = Review_ssf_long_sleeve_jacket.objects.all()
        month_value = FashionScore_long_sleeve_jacket.objects.values()
        sent_value = SentValue_long_sleeve_jacket.objects.values()
        sent_list = SentScore_long_sleeve_jacket.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "셔츠":
        musinsa_review_list = Review_musinsa_shirt.objects.all()
        seoulstore_review_list = Review_seoulstore_shirt.objects.all()
        ssf_review_list = Review_ssf_shirt.objects.all()
        month_value = FashionScore_shirt.objects.values()
        sent_value = SentValue_shirt.objects.values()
        sent_list = SentScore_shirt.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "블라우스":
        musinsa_review_list = Review_musinsa_blouse.objects.all()
        seoulstore_review_list = Review_seoulstore_blouse.objects.all()
        ssf_review_list = Review_ssf_blouse.objects.all()
        month_value = FashionScore_blouse.objects.values()
        sent_value = SentValue_blouse.objects.values()
        sent_list = SentScore_blouse.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "니트":
        musinsa_review_list = Review_musinsa_neat.objects.all()
        seoulstore_review_list = Review_seoulstore_neat.objects.all()
        ssf_review_list = Review_ssf_neat.objects.all()
        month_value = FashionScore_neat.objects.values()
        sent_value = SentValue_neat.objects.values()
        sent_list = SentScore_neat.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "후드":
        musinsa_review_list = Review_musinsa_hoodie.objects.all()
        seoulstore_review_list = Review_seoulstore_hoodie.objects.all()
        ssf_review_list = Review_ssf_hoodie.objects.all()
        month_value = FashionScore_hoodie.objects.values()
        sent_value = SentValue_hoodie.objects.values()
        sent_list = SentScore_hoodie.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "맨투맨":
        musinsa_review_list = Review_musinsa_sweat_shirt.objects.all()
        seoulstore_review_list = Review_seoulstore_sweat_shirt.objects.all()
        ssf_review_list = Review_ssf_sweat_shirt.objects.all()
        month_value = FashionScore_sweat_shirt.objects.values()
        sent_value = SentValue_sweat_shirt.objects.values()
        sent_list = SentScore_sweat_shirt.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "데님팬츠":
        musinsa_review_list = Review_musinsa_denim_pants.objects.all()
        seoulstore_review_list = Review_seoulstore_denim_pants.objects.all()
        ssf_review_list = Review_ssf_denim_pants.objects.all()
        month_value = FashionScore_denim_pants.objects.values()
        sent_value = SentValue_denim_pants.objects.values()
        sent_list = SentScore_denim_pants.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "미니스커트":
        musinsa_review_list = Review_musinsa_mini_skirt.objects.all()
        seoulstore_review_list = Review_seoulstore_mini_skirt.objects.all()
        ssf_review_list = Review_ssf_mini_skirt.objects.all()
        month_value = FashionScore_mini_skirt.objects.values()
        sent_value = SentValue_mini_skirt.objects.values()
        sent_list = SentScore_mini_skirt.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "스커트":
        musinsa_review_list = Review_musinsa_skirt.objects.all()
        seoulstore_review_list = Review_seoulstore_skirt.objects.all()
        ssf_review_list = Review_ssf_skirt.objects.all()
        month_value = FashionScore_skirt.objects.values()
        sent_value = SentValue_skirt.objects.values()
        sent_list = SentScore_skirt.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "슬랙스":
        musinsa_review_list = Review_musinsa_slacks.objects.all()
        seoulstore_review_list = Review_seoulstore_slacks.objects.all()
        ssf_review_list = Review_ssf_slacks.objects.all()
        month_value = FashionScore_slacks.objects.values()
        sent_value = SentValue_slacks.objects.values()
        sent_list = SentScore_slacks.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "숏팬츠":
        musinsa_review_list = Review_musinsa_short_pants.objects.all()
        seoulstore_review_list = Review_seoulstore_short_pants.objects.all()
        ssf_review_list = Review_ssf_short_pants.objects.all()
        month_value = FashionScore_short_pants.objects.values()
        sent_value = SentValue_short_pants.objects.values()
        sent_list = SentScore_short_pants.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "트레이닝":
        musinsa_review_list = Review_musinsa_sports_wear.objects.all()
        seoulstore_review_list = Review_seoulstore_sports_wear.objects.all()
        ssf_review_list = Review_ssf_sports_wear.objects.all()
        month_value = FashionScore_sports_wear.objects.values()
        sent_value = SentValue_sports_wear.objects.values()
        sent_list = SentScore_sports_wear.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "레깅스":
        musinsa_review_list = Review_musinsa_leggings.objects.all()
        seoulstore_review_list = Review_seoulstore_leggings.objects.all()
        ssf_review_list = Review_ssf_leggings.objects.all()
        month_value = FashionScore_leggings.objects.values()
        sent_value = SentValue_leggings.objects.values()
        sent_list = SentScore_leggings.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "운동화":
        musinsa_review_list = Review_musinsa_sports_shoes.objects.all()
        seoulstore_review_list = Review_seoulstore_sports_shoes.objects.all()
        ssf_review_list = Review_ssf_sports_shoes.objects.all()
        month_value = FashionScore_sports_shoes.objects.values()
        sent_value = SentValue_sports_shoes.objects.values()
        sent_list = SentScore_sports_shoes.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "샌들":
        musinsa_review_list = Review_musinsa_sandal.objects.all()
        seoulstore_review_list = Review_seoulstore_sandal.objects.all()
        ssf_review_list = Review_ssf_sandal.objects.all()
        month_value = FashionScore_sandal.objects.values()
        sent_value = SentValue_sandal.objects.values()
        sent_list = SentScore_sandal.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "힐":
        musinsa_review_list = Review_musinsa_heel.objects.all()
        seoulstore_review_list = Review_seoulstore_heel.objects.all()
        ssf_review_list = Review_ssf_heel.objects.all()
        month_value = FashionScore_heel.objects.values()
        sent_value = SentValue_heel.objects.values()
        sent_list = SentScore_heel.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "로퍼":
        musinsa_review_list = Review_musinsa_loafers.objects.all()
        seoulstore_review_list = Review_seoulstore_loafers.objects.all()
        ssf_review_list = Review_ssf_loafers.objects.all()
        month_value = FashionScore_loafers.objects.values()
        sent_value = SentValue_loafers.objects.values()
        sent_list = SentScore_loafers.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "워커":
        musinsa_review_list = Review_musinsa_walker.objects.all()
        seoulstore_review_list = Review_seoulstore_walker.objects.all()
        ssf_review_list = Review_ssf_walker.objects.all()
        month_value = FashionScore_walker.objects.values()
        sent_value = SentValue_walker.objects.values()
        sent_list = SentScore_walker.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "원피스":
        musinsa_review_list = Review_musinsa_dress.objects.all()
        seoulstore_review_list = Review_seoulstore_dress.objects.all()
        ssf_review_list = Review_ssf_dress.objects.all()
        month_value = FashionScore_dress.objects.values()
        sent_value = SentValue_dress.objects.values()
        sent_list = SentScore_dress.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "백팩":
        musinsa_review_list = Review_musinsa_back_pack.objects.all()
        seoulstore_review_list = Review_seoulstore_back_pack.objects.all()
        ssf_review_list = Review_ssf_back_pack.objects.all()
        month_value = FashionScore_back_pack.objects.values()
        sent_value = SentValue_back_pack.objects.values()
        sent_list = SentScore_back_pack.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "토트백":
        musinsa_review_list = Review_musinsa_tote_bag.objects.all()
        seoulstore_review_list = Review_seoulstore_tote_bag.objects.all()
        ssf_review_list = Review_ssf_tote_bag.objects.all()
        month_value = FashionScore_tote_bag.objects.values()
        sent_value = SentValue_tote_bag.objects.values()
        sent_list = SentScore_tote_bag.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "클러치":
        musinsa_review_list = Review_musinsa_clutch_bag.objects.all()
        seoulstore_review_list = Review_seoulstore_clutch_bag.objects.all()
        ssf_review_list = Review_ssf_clutch_bag.objects.all()
        month_value = FashionScore_clutch_bag.objects.values()
        sent_value = SentValue_clutch_bag.objects.values()
        sent_list = SentScore_clutch_bag.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "숄더백":
        musinsa_review_list = Review_musinsa_shoulder_bag.objects.all()
        seoulstore_review_list = Review_seoulstore_shoulder_bag.objects.all()
        ssf_review_list = Review_ssf_shoulder_bag.objects.all()
        month_value = FashionScore_shoulder_bag.objects.values()
        sent_value = SentValue_shoulder_bag.objects.values()
        sent_list = SentScore_shoulder_bag.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    elif keyword == "에코백":
        musinsa_review_list = Review_musinsa_eco_bag.objects.all()
        seoulstore_review_list = Review_seoulstore_eco_bag.objects.all()
        ssf_review_list = Review_ssf_eco_bag.objects.all()
        month_value = FashionScore_eco_bag.objects.values()
        sent_value = SentValue_eco_bag.objects.values()
        sent_list = SentScore_eco_bag.objects.all()
        month_1 = month_value[0]['month_1']
        month_2 = month_value[0]['month_2']
        month_3 = month_value[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'keyword': keyword,
            'musinsa_review_list': musinsa_review_list,
            'seoulstore_review_list': seoulstore_review_list,
            'ssf_review_list': ssf_review_list,
            'month_1': month_1,
            'month_2': month_2,
            'month_3': month_3,
            'positive_value': positive_value,
            'negative_value': negative_value,
            'neutral_value': neutral_value,
            'sent_list': sent_list
        }
        return render(request, 'index/data.html', context)
    else: # 품목 리스트에 없는 단어를 입력했을때
        return render(request, 'index/search.html')


def ranking(request):
    ranking_list = Ranking.objects.all().order_by('-ranking_score')
    context = {'ranking_list': ranking_list}

    return render(request, 'index/ranking.html', context)


def search(request):
    return render(request, 'index/search.html')
