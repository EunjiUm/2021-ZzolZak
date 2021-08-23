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

    elif keyword == "":
        pass


def ranking(request):
    ranking_list = Ranking.objects.all().order_by('-ranking_score')
    context = {'ranking_list': ranking_list}

    return render(request, 'index/ranking_outer.html', context)


def search(request):
    return render(request, 'index/search.html')
