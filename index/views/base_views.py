from django.shortcuts import render

from index.models import *

FashionScore_trench_coat = FashionScore_trench_coat.objects.values()
FashionScore_coat = FashionScore_coat.objects.values()
FashionScore_padded_jacket = FashionScore_padded_jacket.objects.values()
FashionScore_military = FashionScore_military.objects.values()
FashionScore_blazer = FashionScore_blazer.objects.values()
FashionScore_leather_jacket = FashionScore_leather_jacket.objects.values()
FashionScore_fur_jacket = FashionScore_fur_jacket.objects.values()
FashionScore_short_sleeve_jacket = FashionScore_short_sleeve_jacket.objects.values()
FashionScore_long_sleeve_jacket = FashionScore_long_sleeve_jacket.objects.values()
FashionScore_shirt = FashionScore_shirt.objects.values()
FashionScore_blouse = FashionScore_blouse.objects.values()
FashionScore_neat = FashionScore_neat.objects.values()
FashionScore_hoodie = FashionScore_hoodie.objects.values()
FashionScore_sweat_shirt = FashionScore_sweat_shirt.objects.values()
FashionScore_denim_pants = FashionScore_denim_pants.objects.values()
FashionScore_mini_skirt = FashionScore_mini_skirt.objects.values()
FashionScore_skirt = FashionScore_skirt.objects.values()
FashionScore_slacks = FashionScore_slacks.objects.values()
FashionScore_short_pants = FashionScore_short_pants.objects.values()
FashionScore_sports_wear = FashionScore_sports_wear.objects.values()
FashionScore_leggings = FashionScore_leggings.objects.values()
FashionScore_sports_shoes = FashionScore_sports_shoes.objects.values()
FashionScore_sandal = FashionScore_sandal.objects.values()
FashionScore_heel = FashionScore_heel.objects.values()
FashionScore_loafers = FashionScore_loafers.objects.values()
FashionScore_walker = FashionScore_walker.objects.values()
FashionScore_dress = FashionScore_dress.objects.values()
FashionScore_back_pack = FashionScore_back_pack.objects.values()
FashionScore_tote_bag = FashionScore_tote_bag.objects.values()
FashionScore_clutch_bag = FashionScore_clutch_bag.objects.values()
FashionScore_shoulder_bag = FashionScore_shoulder_bag.objects.values()
FashionScore_eco_bag = FashionScore_eco_bag.objects.values()


def intro(request):
    keyword = request.GET.get('kw', '')  # 검색어
    product_list = ['트렌치코트', '코트', '패딩', '밀리터리', '블레이저', '레더재킷', '퍼', '반팔티셔츠', '긴팔티셔츠', '셔츠', '블라우스', '니트', '후드', '맨투맨', '데님팬츠',
                    '미니스커트', '스커트', '슬랙스', '숏팬츠', '트레이닝', '레깅스', '운동화','샌들', '힐', '로퍼', '워커', '원피스', '백팩', '토트백', '클러치백', '숄더백',
                    '에코백']

    if keyword == "트렌치코트":
        musinsa_review_list = Review_musinsa_trench_coat.objects.all()
        seoulstore_review_list = Review_seoulstore_trench_coat.objects.all()
        ssf_review_list = Review_ssf_trench_coat.objects.all()
        sent_value = SentValue_trench_coat.objects.values()
        sent_list = SentScore_trench_coat.objects.all()
        Jan = FashionScore_trench_coat[0]['Jan']
        Feb = FashionScore_trench_coat[0]['Feb']
        Mar = FashionScore_trench_coat[0]['Mar']
        Apr = FashionScore_trench_coat[0]['Apr']
        May = FashionScore_trench_coat[0]['May']
        June = FashionScore_trench_coat[0]['June']
        July = FashionScore_trench_coat[0]['July']
        Aug = FashionScore_trench_coat[0]['Aug']
        Sep = FashionScore_trench_coat[0]['Sep']
        Oct = FashionScore_trench_coat[0]['Oct']
        Nov = FashionScore_trench_coat[0]['Nov']
        Dec = FashionScore_trench_coat[0]['Dec']
        month_1 = FashionScore_trench_coat[0]['month_1']
        month_2 = FashionScore_trench_coat[0]['month_2']
        month_3 = FashionScore_trench_coat[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
    elif keyword == "슬랙스" or keyword == "정장바지" or keyword == "밴딩슬랙스" or keyword == "슬렉스":
        musinsa_review_list = Review_musinsa_slacks.objects.all()
        seoulstore_review_list = Review_seoulstore_slacks.objects.all()
        ssf_review_list = Review_ssf_slacks.objects.all()
        sent_value = SentValue_slacks.objects.values()
        sent_list = SentScore_slacks.objects.all()
        Jan = FashionScore_slacks[0]['Jan']
        Feb = FashionScore_slacks[0]['Feb']
        Mar = FashionScore_slacks[0]['Mar']
        Apr = FashionScore_slacks[0]['Apr']
        May = FashionScore_slacks[0]['May']
        June = FashionScore_slacks[0]['June']
        July = FashionScore_slacks[0]['July']
        Aug = FashionScore_slacks[0]['Aug']
        Sep = FashionScore_slacks[0]['Sep']
        Oct = FashionScore_slacks[0]['Oct']
        Nov = FashionScore_slacks[0]['Nov']
        Dec = FashionScore_slacks[0]['Dec']
        month_1 = FashionScore_slacks[0]['month_1']
        month_2 = FashionScore_slacks[0]['month_2']
        month_3 = FashionScore_slacks[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
        sent_value = SentValue_coat.objects.values()
        sent_list = SentScore_coat.objects.all()
        Jan = FashionScore_coat[0]['Jan']
        Feb = FashionScore_coat[0]['Feb']
        Mar = FashionScore_coat[0]['Mar']
        Apr = FashionScore_coat[0]['Apr']
        May = FashionScore_coat[0]['May']
        June = FashionScore_coat[0]['June']
        July = FashionScore_coat[0]['July']
        Aug = FashionScore_coat[0]['Aug']
        Sep = FashionScore_coat[0]['Sep']
        Oct = FashionScore_coat[0]['Oct']
        Nov = FashionScore_coat[0]['Nov']
        Dec = FashionScore_coat[0]['Dec']
        month_1 = FashionScore_coat[0]['month_1']
        month_2 = FashionScore_coat[0]['month_2']
        month_3 = FashionScore_coat[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
    elif keyword == "패딩" or keyword == "패딩점퍼" or keyword == "다운패딩":
        musinsa_review_list = Review_musinsa_padded_jacket.objects.all()
        seoulstore_review_list = Review_seoulstore_padded_jacket.objects.all()
        ssf_review_list = Review_ssf_padded_jacket.objects.all()
        sent_value = SentValue_padded_jacket.objects.values()
        sent_list = SentScore_padded_jacket.objects.all()
        Jan = FashionScore_padded_jacket[0]['Jan']
        Feb = FashionScore_padded_jacket[0]['Feb']
        Mar = FashionScore_padded_jacket[0]['Mar']
        Apr = FashionScore_padded_jacket[0]['Apr']
        May = FashionScore_padded_jacket[0]['May']
        June = FashionScore_padded_jacket[0]['June']
        July = FashionScore_padded_jacket[0]['July']
        Aug = FashionScore_padded_jacket[0]['Aug']
        Sep = FashionScore_padded_jacket[0]['Sep']
        Oct = FashionScore_padded_jacket[0]['Oct']
        Nov = FashionScore_padded_jacket[0]['Nov']
        Dec = FashionScore_padded_jacket[0]['Dec']
        month_1 = FashionScore_padded_jacket[0]['month_1']
        month_2 = FashionScore_padded_jacket[0]['month_2']
        month_3 = FashionScore_padded_jacket[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
    elif keyword == "밀리터리" or keyword == "사파리자켓" or keyword == "필드자켓":
        musinsa_review_list = Review_musinsa_military.objects.all()
        seoulstore_review_list = Review_seoulstore_military.objects.all()
        ssf_review_list = Review_ssf_military.objects.all()
        sent_value = SentValue_military.objects.values()
        sent_list = SentScore_military.objects.all()
        Jan = FashionScore_military[0]['Jan']
        Feb = FashionScore_military[0]['Feb']
        Mar = FashionScore_military[0]['Mar']
        Apr = FashionScore_military[0]['Apr']
        May = FashionScore_military[0]['May']
        June = FashionScore_military[0]['June']
        July = FashionScore_military[0]['July']
        Aug = FashionScore_military[0]['Aug']
        Sep = FashionScore_military[0]['Sep']
        Oct = FashionScore_military[0]['Oct']
        Nov = FashionScore_military[0]['Nov']
        Dec = FashionScore_military[0]['Dec']
        month_1 = FashionScore_military[0]['month_1']
        month_2 = FashionScore_military[0]['month_2']
        month_3 = FashionScore_military[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
        sent_value = SentValue_blazer.objects.values()
        sent_list = SentScore_blazer.objects.all()
        Jan = FashionScore_blazer[0]['Jan']
        Feb = FashionScore_blazer[0]['Feb']
        Mar = FashionScore_blazer[0]['Mar']
        Apr = FashionScore_blazer[0]['Apr']
        May = FashionScore_blazer[0]['May']
        June = FashionScore_blazer[0]['June']
        July = FashionScore_blazer[0]['July']
        Aug = FashionScore_blazer[0]['Aug']
        Sep = FashionScore_blazer[0]['Sep']
        Oct = FashionScore_blazer[0]['Oct']
        Nov = FashionScore_blazer[0]['Nov']
        Dec = FashionScore_blazer[0]['Dec']
        month_1 = FashionScore_blazer[0]['month_1']
        month_2 = FashionScore_blazer[0]['month_2']
        month_3 = FashionScore_blazer[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
    elif keyword == "레더재킷" or keyword == "가죽재킷":
        musinsa_review_list = Review_musinsa_leather_jacket.objects.all()
        seoulstore_review_list = Review_seoulstore_leather_jacket.objects.all()
        ssf_review_list = Review_ssf_leather_jacket.objects.all()
        sent_value = SentValue_leather_jacket.objects.values()
        sent_list = SentScore_leather_jacket.objects.all()
        Jan = FashionScore_leather_jacket[0]['Jan']
        Feb = FashionScore_leather_jacket[0]['Feb']
        Mar = FashionScore_leather_jacket[0]['Mar']
        Apr = FashionScore_leather_jacket[0]['Apr']
        May = FashionScore_leather_jacket[0]['May']
        June = FashionScore_leather_jacket[0]['June']
        July = FashionScore_leather_jacket[0]['July']
        Aug = FashionScore_leather_jacket[0]['Aug']
        Sep = FashionScore_leather_jacket[0]['Sep']
        Oct = FashionScore_leather_jacket[0]['Oct']
        Nov = FashionScore_leather_jacket[0]['Nov']
        Dec = FashionScore_leather_jacket[0]['Dec']
        month_1 = FashionScore_leather_jacket[0]['month_1']
        month_2 = FashionScore_leather_jacket[0]['month_2']
        month_3 = FashionScore_leather_jacket[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
    elif keyword == "퍼" or keyword == "털옷":
        musinsa_review_list = Review_musinsa_fur_jacket.objects.all()
        seoulstore_review_list = Review_seoulstore_fur_jacket.objects.all()
        ssf_review_list = Review_ssf_fur_jacket.objects.all()
        sent_value = SentValue_fur_jacket.objects.values()
        sent_list = SentScore_fur_jacket.objects.all()
        Jan = FashionScore_fur_jacket[0]['Jan']
        Feb = FashionScore_fur_jacket[0]['Feb']
        Mar = FashionScore_fur_jacket[0]['Mar']
        Apr = FashionScore_fur_jacket[0]['Apr']
        May = FashionScore_fur_jacket[0]['May']
        June = FashionScore_fur_jacket[0]['June']
        July = FashionScore_fur_jacket[0]['July']
        Aug = FashionScore_fur_jacket[0]['Aug']
        Sep = FashionScore_fur_jacket[0]['Sep']
        Oct = FashionScore_fur_jacket[0]['Oct']
        Nov = FashionScore_fur_jacket[0]['Nov']
        Dec = FashionScore_fur_jacket[0]['Dec']
        month_1 = FashionScore_fur_jacket[0]['month_1']
        month_2 = FashionScore_fur_jacket[0]['month_2']
        month_3 = FashionScore_fur_jacket[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
    elif keyword == "반팔티셔츠" or keyword == "반팔티" or keyword == "반팔":
        musinsa_review_list = Review_musinsa_short_sleeve_jacket.objects.all()
        seoulstore_review_list = Review_seoulstore_short_sleeve_jacket.objects.all()
        ssf_review_list = Review_ssf_short_sleeve_jacket.objects.all()
        sent_value = SentValue_short_sleeve_jacket.objects.values()
        sent_list = SentScore_short_sleeve_jacket.objects.all()
        Jan = FashionScore_short_sleeve_jacket[0]['Jan']
        Feb = FashionScore_short_sleeve_jacket[0]['Feb']
        Mar = FashionScore_short_sleeve_jacket[0]['Mar']
        Apr = FashionScore_short_sleeve_jacket[0]['Apr']
        May = FashionScore_short_sleeve_jacket[0]['May']
        June = FashionScore_short_sleeve_jacket[0]['June']
        July = FashionScore_short_sleeve_jacket[0]['July']
        Aug = FashionScore_short_sleeve_jacket[0]['Aug']
        Sep = FashionScore_short_sleeve_jacket[0]['Sep']
        Oct = FashionScore_short_sleeve_jacket[0]['Oct']
        Nov = FashionScore_short_sleeve_jacket[0]['Nov']
        Dec = FashionScore_short_sleeve_jacket[0]['Dec']
        month_1 = FashionScore_short_sleeve_jacket[0]['month_1']
        month_2 = FashionScore_short_sleeve_jacket[0]['month_2']
        month_3 = FashionScore_short_sleeve_jacket[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
    elif keyword == "긴팔티셔츠" or keyword == "긴팔티" or keyword == "긴팔":
        musinsa_review_list = Review_musinsa_long_sleeve_jacket.objects.all()
        seoulstore_review_list = Review_seoulstore_long_sleeve_jacket.objects.all()
        ssf_review_list = Review_ssf_long_sleeve_jacket.objects.all()
        sent_value = SentValue_long_sleeve_jacket.objects.values()
        sent_list = SentScore_long_sleeve_jacket.objects.all()
        Jan = FashionScore_long_sleeve_jacket[0]['Jan']
        Feb = FashionScore_long_sleeve_jacket[0]['Feb']
        Mar = FashionScore_long_sleeve_jacket[0]['Mar']
        Apr = FashionScore_long_sleeve_jacket[0]['Apr']
        May = FashionScore_long_sleeve_jacket[0]['May']
        June = FashionScore_long_sleeve_jacket[0]['June']
        July = FashionScore_long_sleeve_jacket[0]['July']
        Aug = FashionScore_long_sleeve_jacket[0]['Aug']
        Sep = FashionScore_long_sleeve_jacket[0]['Sep']
        Oct = FashionScore_long_sleeve_jacket[0]['Oct']
        Nov = FashionScore_long_sleeve_jacket[0]['Nov']
        Dec = FashionScore_long_sleeve_jacket[0]['Dec']
        month_1 = FashionScore_long_sleeve_jacket[0]['month_1']
        month_2 = FashionScore_long_sleeve_jacket[0]['month_2']
        month_3 = FashionScore_long_sleeve_jacket[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
        sent_value = SentValue_shirt.objects.values()
        sent_list = SentScore_shirt.objects.all()
        Jan = FashionScore_shirt[0]['Jan']
        Feb = FashionScore_shirt[0]['Feb']
        Mar = FashionScore_shirt[0]['Mar']
        Apr = FashionScore_shirt[0]['Apr']
        May = FashionScore_shirt[0]['May']
        June = FashionScore_shirt[0]['June']
        July = FashionScore_shirt[0]['July']
        Aug = FashionScore_shirt[0]['Aug']
        Sep = FashionScore_shirt[0]['Sep']
        Oct = FashionScore_shirt[0]['Oct']
        Nov = FashionScore_shirt[0]['Nov']
        Dec = FashionScore_shirt[0]['Dec']
        month_1 = FashionScore_shirt[0]['month_1']
        month_2 = FashionScore_shirt[0]['month_2']
        month_3 = FashionScore_shirt[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
    elif keyword == "블라우스" or keyword == "슬리브":
        musinsa_review_list = Review_musinsa_blouse.objects.all()
        seoulstore_review_list = Review_seoulstore_blouse.objects.all()
        ssf_review_list = Review_ssf_blouse.objects.all()
        sent_value = SentValue_blouse.objects.values()
        sent_list = SentScore_blouse.objects.all()
        Jan = FashionScore_blouse[0]['Jan']
        Feb = FashionScore_blouse[0]['Feb']
        Mar = FashionScore_blouse[0]['Mar']
        Apr = FashionScore_blouse[0]['Apr']
        May = FashionScore_blouse[0]['May']
        June = FashionScore_blouse[0]['June']
        July = FashionScore_blouse[0]['July']
        Aug = FashionScore_blouse[0]['Aug']
        Sep = FashionScore_blouse[0]['Sep']
        Oct = FashionScore_blouse[0]['Oct']
        Nov = FashionScore_blouse[0]['Nov']
        Dec = FashionScore_blouse[0]['Dec']
        month_1 = FashionScore_blouse[0]['month_1']
        month_2 = FashionScore_blouse[0]['month_2']
        month_3 = FashionScore_blouse[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
    elif keyword == "니트" or keyword == "스웨터" or keyword == "니트조끼" or keyword == "베스트":
        musinsa_review_list = Review_musinsa_neat.objects.all()
        seoulstore_review_list = Review_seoulstore_neat.objects.all()
        ssf_review_list = Review_ssf_neat.objects.all()
        sent_value = SentValue_neat.objects.values()
        sent_list = SentScore_neat.objects.all()
        Jan = FashionScore_neat[0]['Jan']
        Feb = FashionScore_neat[0]['Feb']
        Mar = FashionScore_neat[0]['Mar']
        Apr = FashionScore_neat[0]['Apr']
        May = FashionScore_neat[0]['May']
        June = FashionScore_neat[0]['June']
        July = FashionScore_neat[0]['July']
        Aug = FashionScore_neat[0]['Aug']
        Sep = FashionScore_neat[0]['Sep']
        Oct = FashionScore_neat[0]['Oct']
        Nov = FashionScore_neat[0]['Nov']
        Dec = FashionScore_neat[0]['Dec']
        month_1 = FashionScore_neat[0]['month_1']
        month_2 = FashionScore_neat[0]['month_2']
        month_3 = FashionScore_neat[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
    elif keyword == "후드" or keyword == "후드티" or keyword == "후드집업":
        musinsa_review_list = Review_musinsa_hoodie.objects.all()
        seoulstore_review_list = Review_seoulstore_hoodie.objects.all()
        ssf_review_list = Review_ssf_hoodie.objects.all()
        sent_value = SentValue_hoodie.objects.values()
        sent_list = SentScore_hoodie.objects.all()
        Jan = FashionScore_hoodie[0]['Jan']
        Feb = FashionScore_hoodie[0]['Feb']
        Mar = FashionScore_hoodie[0]['Mar']
        Apr = FashionScore_hoodie[0]['Apr']
        May = FashionScore_hoodie[0]['May']
        June = FashionScore_hoodie[0]['June']
        July = FashionScore_hoodie[0]['July']
        Aug = FashionScore_hoodie[0]['Aug']
        Sep = FashionScore_hoodie[0]['Sep']
        Oct = FashionScore_hoodie[0]['Oct']
        Nov = FashionScore_hoodie[0]['Nov']
        Dec = FashionScore_hoodie[0]['Dec']
        month_1 = FashionScore_hoodie[0]['month_1']
        month_2 = FashionScore_hoodie[0]['month_2']
        month_3 = FashionScore_hoodie[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
        sent_value = SentValue_sweat_shirt.objects.values()
        sent_list = SentScore_sweat_shirt.objects.all()
        Jan = FashionScore_sweat_shirt[0]['Jan']
        Feb = FashionScore_sweat_shirt[0]['Feb']
        Mar = FashionScore_sweat_shirt[0]['Mar']
        Apr = FashionScore_sweat_shirt[0]['Apr']
        May = FashionScore_sweat_shirt[0]['May']
        June = FashionScore_sweat_shirt[0]['June']
        July = FashionScore_sweat_shirt[0]['July']
        Aug = FashionScore_sweat_shirt[0]['Aug']
        Sep = FashionScore_sweat_shirt[0]['Sep']
        Oct = FashionScore_sweat_shirt[0]['Oct']
        Nov = FashionScore_sweat_shirt[0]['Nov']
        Dec = FashionScore_sweat_shirt[0]['Dec']
        month_1 = FashionScore_sweat_shirt[0]['month_1']
        month_2 = FashionScore_sweat_shirt[0]['month_2']
        month_3 = FashionScore_sweat_shirt[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
    elif keyword == "청바지" or keyword == "진청" or keyword == "연청" or keyword == "와이드팬츠" or keyword == "스키니진" or keyword == "데님":
        musinsa_review_list = Review_musinsa_denim_pants.objects.all()
        seoulstore_review_list = Review_seoulstore_denim_pants.objects.all()
        ssf_review_list = Review_ssf_denim_pants.objects.all()
        sent_value = SentValue_denim_pants.objects.values()
        sent_list = SentScore_denim_pants.objects.all()
        Jan = FashionScore_denim_pants[0]['Jan']
        Feb = FashionScore_denim_pants[0]['Feb']
        Mar = FashionScore_denim_pants[0]['Mar']
        Apr = FashionScore_denim_pants[0]['Apr']
        May = FashionScore_denim_pants[0]['May']
        June = FashionScore_denim_pants[0]['June']
        July = FashionScore_denim_pants[0]['July']
        Aug = FashionScore_denim_pants[0]['Aug']
        Sep = FashionScore_denim_pants[0]['Sep']
        Oct = FashionScore_denim_pants[0]['Oct']
        Nov = FashionScore_denim_pants[0]['Nov']
        Dec = FashionScore_denim_pants[0]['Dec']
        month_1 = FashionScore_denim_pants[0]['month_1']
        month_2 = FashionScore_denim_pants[0]['month_2']
        month_3 = FashionScore_denim_pants[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
    elif keyword == "미니스커트" or keyword == "짧은치마" or keyword == "숏스커트":
        musinsa_review_list = Review_musinsa_mini_skirt.objects.all()
        seoulstore_review_list = Review_seoulstore_mini_skirt.objects.all()
        ssf_review_list = Review_ssf_mini_skirt.objects.all()
        sent_value = SentValue_mini_skirt.objects.values()
        sent_list = SentScore_mini_skirt.objects.all()
        Jan = FashionScore_mini_skirt[0]['Jan']
        Feb = FashionScore_mini_skirt[0]['Feb']
        Mar = FashionScore_mini_skirt[0]['Mar']
        Apr = FashionScore_mini_skirt[0]['Apr']
        May = FashionScore_mini_skirt[0]['May']
        June = FashionScore_mini_skirt[0]['June']
        July = FashionScore_mini_skirt[0]['July']
        Aug = FashionScore_mini_skirt[0]['Aug']
        Sep = FashionScore_mini_skirt[0]['Sep']
        Oct = FashionScore_mini_skirt[0]['Oct']
        Nov = FashionScore_mini_skirt[0]['Nov']
        Dec = FashionScore_mini_skirt[0]['Dec']
        month_1 = FashionScore_mini_skirt[0]['month_1']
        month_2 = FashionScore_mini_skirt[0]['month_2']
        month_3 = FashionScore_mini_skirt[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
    elif keyword == "스커트" or keyword == "롱스커트" or keyword == "청치마":
        musinsa_review_list = Review_musinsa_skirt.objects.all()
        seoulstore_review_list = Review_seoulstore_skirt.objects.all()
        ssf_review_list = Review_ssf_skirt.objects.all()
        sent_value = SentValue_skirt.objects.values()
        sent_list = SentScore_skirt.objects.all()
        Jan = FashionScore_skirt[0]['Jan']
        Feb = FashionScore_skirt[0]['Feb']
        Mar = FashionScore_skirt[0]['Mar']
        Apr = FashionScore_skirt[0]['Apr']
        May = FashionScore_skirt[0]['May']
        June = FashionScore_skirt[0]['June']
        July = FashionScore_skirt[0]['July']
        Aug = FashionScore_skirt[0]['Aug']
        Sep = FashionScore_skirt[0]['Sep']
        Oct = FashionScore_skirt[0]['Oct']
        Nov = FashionScore_skirt[0]['Nov']
        Dec = FashionScore_skirt[0]['Dec']
        month_1 = FashionScore_skirt[0]['month_1']
        month_2 = FashionScore_skirt[0]['month_2']
        month_3 = FashionScore_skirt[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
    elif keyword == "숏팬츠" or keyword == "반바지" or keyword == "러닝팬츠" or keyword == "쇼츠":
        musinsa_review_list = Review_musinsa_short_pants.objects.all()
        seoulstore_review_list = Review_seoulstore_short_pants.objects.all()
        ssf_review_list = Review_ssf_short_pants.objects.all()
        sent_value = SentValue_short_pants.objects.values()
        sent_list = SentScore_short_pants.objects.all()
        Jan = FashionScore_short_pants[0]['Jan']
        Feb = FashionScore_short_pants[0]['Feb']
        Mar = FashionScore_short_pants[0]['Mar']
        Apr = FashionScore_short_pants[0]['Apr']
        May = FashionScore_short_pants[0]['May']
        June = FashionScore_short_pants[0]['June']
        July = FashionScore_short_pants[0]['July']
        Aug = FashionScore_short_pants[0]['Aug']
        Sep = FashionScore_short_pants[0]['Sep']
        Oct = FashionScore_short_pants[0]['Oct']
        Nov = FashionScore_short_pants[0]['Nov']
        Dec = FashionScore_short_pants[0]['Dec']
        month_1 = FashionScore_short_pants[0]['month_1']
        month_2 = FashionScore_short_pants[0]['month_2']
        month_3 = FashionScore_short_pants[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
    elif keyword == "트레이닝" or keyword == "운동복" or keyword == "트레이닝바지" or keyword == "조거팬츠":
        musinsa_review_list = Review_musinsa_sports_wear.objects.all()
        seoulstore_review_list = Review_seoulstore_sports_wear.objects.all()
        ssf_review_list = Review_ssf_sports_wear.objects.all()
        sent_value = SentValue_sports_wear.objects.values()
        sent_list = SentScore_sports_wear.objects.all()
        Jan = FashionScore_sports_wear[0]['Jan']
        Feb = FashionScore_sports_wear[0]['Feb']
        Mar = FashionScore_sports_wear[0]['Mar']
        Apr = FashionScore_sports_wear[0]['Apr']
        May = FashionScore_sports_wear[0]['May']
        June = FashionScore_sports_wear[0]['June']
        July = FashionScore_sports_wear[0]['July']
        Aug = FashionScore_sports_wear[0]['Aug']
        Sep = FashionScore_sports_wear[0]['Sep']
        Oct = FashionScore_sports_wear[0]['Oct']
        Nov = FashionScore_sports_wear[0]['Nov']
        Dec = FashionScore_sports_wear[0]['Dec']
        month_1 = FashionScore_sports_wear[0]['month_1']
        month_2 = FashionScore_sports_wear[0]['month_2']
        month_3 = FashionScore_sports_wear[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
    elif keyword == "레깅스" or keyword == "타이즈" or keyword == "기모레깅스" or keyword == "스타킹":
        musinsa_review_list = Review_musinsa_leggings.objects.all()
        seoulstore_review_list = Review_seoulstore_leggings.objects.all()
        ssf_review_list = Review_ssf_leggings.objects.all()
        sent_value = SentValue_leggings.objects.values()
        sent_list = SentScore_leggings.objects.all()
        Jan = FashionScore_leggings[0]['Jan']
        Feb = FashionScore_leggings[0]['Feb']
        Mar = FashionScore_leggings[0]['Mar']
        Apr = FashionScore_leggings[0]['Apr']
        May = FashionScore_leggings[0]['May']
        June = FashionScore_leggings[0]['June']
        July = FashionScore_leggings[0]['July']
        Aug = FashionScore_leggings[0]['Aug']
        Sep = FashionScore_leggings[0]['Sep']
        Oct = FashionScore_leggings[0]['Oct']
        Nov = FashionScore_leggings[0]['Nov']
        Dec = FashionScore_leggings[0]['Dec']
        month_1 = FashionScore_leggings[0]['month_1']
        month_2 = FashionScore_leggings[0]['month_2']
        month_3 = FashionScore_leggings[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
    elif keyword == "운동화" or keyword == "스니커즈" or keyword == "신발" or keyword == "트레이닝화":
        musinsa_review_list = Review_musinsa_sports_shoes.objects.all()
        seoulstore_review_list = Review_seoulstore_sports_shoes.objects.all()
        ssf_review_list = Review_ssf_sports_shoes.objects.all()
        sent_value = SentValue_sports_shoes.objects.values()
        sent_list = SentScore_sports_shoes.objects.all()
        Jan = FashionScore_sports_shoes[0]['Jan']
        Feb = FashionScore_sports_shoes[0]['Feb']
        Mar = FashionScore_sports_shoes[0]['Mar']
        Apr = FashionScore_sports_shoes[0]['Apr']
        May = FashionScore_sports_shoes[0]['May']
        June = FashionScore_sports_shoes[0]['June']
        July = FashionScore_sports_shoes[0]['July']
        Aug = FashionScore_sports_shoes[0]['Aug']
        Sep = FashionScore_sports_shoes[0]['Sep']
        Oct = FashionScore_sports_shoes[0]['Oct']
        Nov = FashionScore_sports_shoes[0]['Nov']
        Dec = FashionScore_sports_shoes[0]['Dec']
        month_1 = FashionScore_sports_shoes[0]['month_1']
        month_2 = FashionScore_sports_shoes[0]['month_2']
        month_3 = FashionScore_sports_shoes[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
    elif keyword == "샌들" or keyword == "슬리퍼" or keyword == "샌달":
        musinsa_review_list = Review_musinsa_sandal.objects.all()
        seoulstore_review_list = Review_seoulstore_sandal.objects.all()
        ssf_review_list = Review_ssf_sandal.objects.all()
        sent_value = SentValue_sandal.objects.values()
        sent_list = SentScore_sandal.objects.all()
        Jan = FashionScore_sandal[0]['Jan']
        Feb = FashionScore_sandal[0]['Feb']
        Mar = FashionScore_sandal[0]['Mar']
        Apr = FashionScore_sandal[0]['Apr']
        May = FashionScore_sandal[0]['May']
        June = FashionScore_sandal[0]['June']
        July = FashionScore_sandal[0]['July']
        Aug = FashionScore_sandal[0]['Aug']
        Sep = FashionScore_sandal[0]['Sep']
        Oct = FashionScore_sandal[0]['Oct']
        Nov = FashionScore_sandal[0]['Nov']
        Dec = FashionScore_sandal[0]['Dec']
        month_1 = FashionScore_sandal[0]['month_1']
        month_2 = FashionScore_sandal[0]['month_2']
        month_3 = FashionScore_sandal[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
    elif keyword == "힐" or keyword == "하이힐" or keyword == "펌프스":
        musinsa_review_list = Review_musinsa_heel.objects.all()
        seoulstore_review_list = Review_seoulstore_heel.objects.all()
        ssf_review_list = Review_ssf_heel.objects.all()
        sent_value = SentValue_heel.objects.values()
        sent_list = SentScore_heel.objects.all()
        Jan = FashionScore_heel[0]['Jan']
        Feb = FashionScore_heel[0]['Feb']
        Mar = FashionScore_heel[0]['Mar']
        Apr = FashionScore_heel[0]['Apr']
        May = FashionScore_heel[0]['May']
        June = FashionScore_heel[0]['June']
        July = FashionScore_heel[0]['July']
        Aug = FashionScore_heel[0]['Aug']
        Sep = FashionScore_heel[0]['Sep']
        Oct = FashionScore_heel[0]['Oct']
        Nov = FashionScore_heel[0]['Nov']
        Dec = FashionScore_heel[0]['Dec']
        month_1 = FashionScore_heel[0]['month_1']
        month_2 = FashionScore_heel[0]['month_2']
        month_3 = FashionScore_heel[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
    elif keyword == "로퍼" or keyword == "플랫슈즈" or keyword == "구두":
        musinsa_review_list = Review_musinsa_loafers.objects.all()
        seoulstore_review_list = Review_seoulstore_loafers.objects.all()
        ssf_review_list = Review_ssf_loafers.objects.all()
        sent_value = SentValue_loafers.objects.values()
        sent_list = SentScore_loafers.objects.all()
        Jan = FashionScore_loafers[0]['Jan']
        Feb = FashionScore_loafers[0]['Feb']
        Mar = FashionScore_loafers[0]['Mar']
        Apr = FashionScore_loafers[0]['Apr']
        May = FashionScore_loafers[0]['May']
        June = FashionScore_loafers[0]['June']
        July = FashionScore_loafers[0]['July']
        Aug = FashionScore_loafers[0]['Aug']
        Sep = FashionScore_loafers[0]['Sep']
        Oct = FashionScore_loafers[0]['Oct']
        Nov = FashionScore_loafers[0]['Nov']
        Dec = FashionScore_loafers[0]['Dec']
        month_1 = FashionScore_loafers[0]['month_1']
        month_2 = FashionScore_loafers[0]['month_2']
        month_3 = FashionScore_loafers[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
    elif keyword == "워커" or keyword == "부츠":
        musinsa_review_list = Review_musinsa_walker.objects.all()
        seoulstore_review_list = Review_seoulstore_walker.objects.all()
        ssf_review_list = Review_ssf_walker.objects.all()
        sent_value = SentValue_walker.objects.values()
        sent_list = SentScore_walker.objects.all()
        Jan = FashionScore_walker[0]['Jan']
        Feb = FashionScore_walker[0]['Feb']
        Mar = FashionScore_walker[0]['Mar']
        Apr = FashionScore_walker[0]['Apr']
        May = FashionScore_walker[0]['May']
        June = FashionScore_walker[0]['June']
        July = FashionScore_walker[0]['July']
        Aug = FashionScore_walker[0]['Aug']
        Sep = FashionScore_walker[0]['Sep']
        Oct = FashionScore_walker[0]['Oct']
        Nov = FashionScore_walker[0]['Nov']
        Dec = FashionScore_walker[0]['Dec']
        month_1 = FashionScore_walker[0]['month_1']
        month_2 = FashionScore_walker[0]['month_2']
        month_3 = FashionScore_walker[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
    elif keyword == "원피스" or keyword == "미니원피스" or keyword == "미디원피스" or keyword == "드레스":
        musinsa_review_list = Review_musinsa_dress.objects.all()
        seoulstore_review_list = Review_seoulstore_dress.objects.all()
        ssf_review_list = Review_ssf_dress.objects.all()
        sent_value = SentValue_dress.objects.values()
        sent_list = SentScore_dress.objects.all()
        Jan = FashionScore_dress[0]['Jan']
        Feb = FashionScore_dress[0]['Feb']
        Mar = FashionScore_dress[0]['Mar']
        Apr = FashionScore_dress[0]['Apr']
        May = FashionScore_dress[0]['May']
        June = FashionScore_dress[0]['June']
        July = FashionScore_dress[0]['July']
        Aug = FashionScore_dress[0]['Aug']
        Sep = FashionScore_dress[0]['Sep']
        Oct = FashionScore_dress[0]['Oct']
        Nov = FashionScore_dress[0]['Nov']
        Dec = FashionScore_dress[0]['Dec']
        month_1 = FashionScore_dress[0]['month_1']
        month_2 = FashionScore_dress[0]['month_2']
        month_3 = FashionScore_dress[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
    elif keyword == "백팩" or keyword == "가방":
        musinsa_review_list = Review_musinsa_back_pack.objects.all()
        seoulstore_review_list = Review_seoulstore_back_pack.objects.all()
        ssf_review_list = Review_ssf_back_pack.objects.all()
        sent_value = SentValue_back_pack.objects.values()
        sent_list = SentScore_back_pack.objects.all()
        Jan = FashionScore_back_pack[0]['Jan']
        Feb = FashionScore_back_pack[0]['Feb']
        Mar = FashionScore_back_pack[0]['Mar']
        Apr = FashionScore_back_pack[0]['Apr']
        May = FashionScore_back_pack[0]['May']
        June = FashionScore_back_pack[0]['June']
        July = FashionScore_back_pack[0]['July']
        Aug = FashionScore_back_pack[0]['Aug']
        Sep = FashionScore_back_pack[0]['Sep']
        Oct = FashionScore_back_pack[0]['Oct']
        Nov = FashionScore_back_pack[0]['Nov']
        Dec = FashionScore_back_pack[0]['Dec']
        month_1 = FashionScore_back_pack[0]['month_1']
        month_2 = FashionScore_back_pack[0]['month_2']
        month_3 = FashionScore_back_pack[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
        sent_value = SentValue_tote_bag.objects.values()
        sent_list = SentScore_tote_bag.objects.all()
        Jan = FashionScore_tote_bag[0]['Jan']
        Feb = FashionScore_tote_bag[0]['Feb']
        Mar = FashionScore_tote_bag[0]['Mar']
        Apr = FashionScore_tote_bag[0]['Apr']
        May = FashionScore_tote_bag[0]['May']
        June = FashionScore_tote_bag[0]['June']
        July = FashionScore_tote_bag[0]['July']
        Aug = FashionScore_tote_bag[0]['Aug']
        Sep = FashionScore_tote_bag[0]['Sep']
        Oct = FashionScore_tote_bag[0]['Oct']
        Nov = FashionScore_tote_bag[0]['Nov']
        Dec = FashionScore_tote_bag[0]['Dec']
        month_1 = FashionScore_tote_bag[0]['month_1']
        month_2 = FashionScore_tote_bag[0]['month_2']
        month_3 = FashionScore_tote_bag[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
    elif keyword == "클러치백":
        musinsa_review_list = Review_musinsa_clutch_bag.objects.all()
        seoulstore_review_list = Review_seoulstore_clutch_bag.objects.all()
        ssf_review_list = Review_ssf_clutch_bag.objects.all()
        sent_value = SentValue_clutch_bag.objects.values()
        sent_list = SentScore_clutch_bag.objects.all()
        Jan = FashionScore_clutch_bag[0]['Jan']
        Feb = FashionScore_clutch_bag[0]['Feb']
        Mar = FashionScore_clutch_bag[0]['Mar']
        Apr = FashionScore_clutch_bag[0]['Apr']
        May = FashionScore_clutch_bag[0]['May']
        June = FashionScore_clutch_bag[0]['June']
        July = FashionScore_clutch_bag[0]['July']
        Aug = FashionScore_clutch_bag[0]['Aug']
        Sep = FashionScore_clutch_bag[0]['Sep']
        Oct = FashionScore_clutch_bag[0]['Oct']
        Nov = FashionScore_clutch_bag[0]['Nov']
        Dec = FashionScore_clutch_bag[0]['Dec']
        month_1 = FashionScore_clutch_bag[0]['month_1']
        month_2 = FashionScore_clutch_bag[0]['month_2']
        month_3 = FashionScore_clutch_bag[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
    elif keyword == "숄더백" or keyword == "쇼퍼백":
        musinsa_review_list = Review_musinsa_shoulder_bag.objects.all()
        seoulstore_review_list = Review_seoulstore_shoulder_bag.objects.all()
        ssf_review_list = Review_ssf_shoulder_bag.objects.all()
        sent_value = SentValue_shoulder_bag.objects.values()
        sent_list = SentScore_shoulder_bag.objects.all()
        Jan = FashionScore_shoulder_bag[0]['Jan']
        Feb = FashionScore_shoulder_bag[0]['Feb']
        Mar = FashionScore_shoulder_bag[0]['Mar']
        Apr = FashionScore_shoulder_bag[0]['Apr']
        May = FashionScore_shoulder_bag[0]['May']
        June = FashionScore_shoulder_bag[0]['June']
        July = FashionScore_shoulder_bag[0]['July']
        Aug = FashionScore_shoulder_bag[0]['Aug']
        Sep = FashionScore_shoulder_bag[0]['Sep']
        Oct = FashionScore_shoulder_bag[0]['Oct']
        Nov = FashionScore_shoulder_bag[0]['Nov']
        Dec = FashionScore_shoulder_bag[0]['Dec']
        month_1 = FashionScore_shoulder_bag[0]['month_1']
        month_2 = FashionScore_shoulder_bag[0]['month_2']
        month_3 = FashionScore_shoulder_bag[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
        sent_value = SentValue_eco_bag.objects.values()
        sent_list = SentScore_eco_bag.objects.all()
        Jan = FashionScore_eco_bag[0]['Jan']
        Feb = FashionScore_eco_bag[0]['Feb']
        Mar = FashionScore_eco_bag[0]['Mar']
        Apr = FashionScore_eco_bag[0]['Apr']
        May = FashionScore_eco_bag[0]['May']
        June = FashionScore_eco_bag[0]['June']
        July = FashionScore_eco_bag[0]['July']
        Aug = FashionScore_eco_bag[0]['Aug']
        Sep = FashionScore_eco_bag[0]['Sep']
        Oct = FashionScore_eco_bag[0]['Oct']
        Nov = FashionScore_eco_bag[0]['Nov']
        Dec = FashionScore_eco_bag[0]['Dec']
        month_1 = FashionScore_eco_bag[0]['month_1']
        month_2 = FashionScore_eco_bag[0]['month_2']
        month_3 = FashionScore_eco_bag[0]['month_3']
        positive_value = sent_value[0]['positive_value']
        negative_value = sent_value[0]['negative_value']
        neutral_value = sent_value[0]['neutral_value']
        context = {
            'Jan': Jan,
            'Feb': Feb,
            'Mar': Mar,
            'Apr': Apr,
            'May': May,
            'June': June,
            'July': July,
            'Aug': Aug,
            'Sep': Sep,
            'Oct': Oct,
            'Nov': Nov,
            'Dec': Dec,
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
    elif keyword not in product_list: # 품목 리스트에 없는 단어를 입력했을때
        return render(request, 'index/no_result.html')


def ranking(request):
    ranking_num = 10
    ranking_list = Ranking.objects.all().order_by('-ranking_score')[:ranking_num]
    context = {'ranking_list': ranking_list}

    return render(request, 'index/ranking.html', context)


def search(request):
    return render(request, 'index/search.html')

def about(request):
    return render(request, 'index/about.html')