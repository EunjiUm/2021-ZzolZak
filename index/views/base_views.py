from django.shortcuts import render

from index.models import SentScore_shirt, SentValue_shirt, FashionScore, Review_ssf_shirt, Review_musinsa_shirt, Ranking_outer

def intro(request):
    keyword = request.GET.get('kw', '')  # 검색어
    product_list = ["셔츠", "후드", "청바지", "슬랙스"]
    if keyword in product_list:
        if keyword == "셔츠":
            musinsa_review_list = Review_musinsa_shirt.objects.all()
            ssf_review_list = Review_ssf_shirt.objects.all()
            month_value = FashionScore.objects.values()
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
                'ssf_review_list': ssf_review_list,
                'month_1': month_1,
                'month_2': month_2,
                'month_3': month_3,
                'positive_value' : positive_value,
                'negative_value' : negative_value,
                'neutral_value' : neutral_value,
                'sent_list' : sent_list
            }
            return render(request, 'index/data.html', context)


    # month_value = FashionScore.objects.values()
    # sent_value = SentValue.objects.values()
    # sent_list = SentScore.objects.all()
    #
    # Jan = month_value[0]['Jan']
    # Feb = month_value[0]['Feb']
    # Mar = month_value[0]['Mar']
    # Apr = month_value[0]['Apr']
    # May = month_value[0]['May']
    # June = month_value[0]['June']
    # July = month_value[0]['July']
    # Aug = month_value[0]['Aug']
    # Sep = month_value[0]['Sep']
    # Oct = month_value[0]['Oct']
    # Nov = month_value[0]['Nov']
    # Dec = month_value[0]['Dec']
    #
    # month_1 = month_value[0]['month_1']
    # month_2 = month_value[0]['month_2']
    # month_3 = month_value[0]['month_3']
    #
    # positive_value = sent_value[0]['positive_value']
    # negative_value = sent_value[0]['negative_value']
    # neutral_value = sent_value[0]['neutral_value']
    #
    # context = {'Jan': Jan,
    #            'Feb': Feb,
    #            'Mar': Mar,
    #            'Apr': Apr,
    #            'May': May,
    #            'June': June,
    #            'July': July,
    #            'Aug': Aug,
    #            'Sep': Sep,
    #            'Oct': Oct,
    #            'Nov': Nov,
    #            'Dec': Dec,
    #            'month_1': month_1,
    #            'month_2': month_2,
    #            'month_3': month_3,
    #            'positive_value' : positive_value,
    #            'negative_value' : negative_value,
    #            'neutral_value' : neutral_value,
    #            'sent_list' : sent_list,
    #            'review_list': review_list,
    #            'keyword': keyword,
    #            }
    # return render(request, 'index/data.html', context)

def index(request):
    kw = request.GET.get('kw', '')  # 검색어
    context = {'kw': kw}
    return render(request, 'index/main.html', context)

def ranking_outer(request):
    ranking_list = Ranking_outer.objects.all().order_by('-ranking_score')
    context = {'ranking_list': ranking_list}

    return render(request, 'index/ranking_outer.html', context)

def ranking_pants(request):
    ranking_list = Ranking_outer.objects.all().order_by('-ranking_score')
    context = {'ranking_list': ranking_list}

    return render(request, 'index/ranking_pants.html', context)

def search(request):
    return render(request, 'index/search.html')
