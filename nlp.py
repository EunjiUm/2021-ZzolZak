import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'config.settings')
django.setup()
from index.models import *
import re
from collections import Counter
from konlpy.tag import Okt
from google.cloud import language_v1


def Data_Nlp(product):
    print("NLP 시작")
    # 각 문장마다 감정분석
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\trendanalyzer-314714-b95748a6864c.json"
    top_word_count = 10
    # 파일 리스트
    company_list = ['musinsa', 'ssf', 'seoulstore']
    reviews = []
    for company in company_list:
        filepath = "data/" + company + "_" + product + ".txt"
        file = open(filepath, 'r', encoding='utf-8')
        lines = file.readlines()
        for line in lines:
            reviews.append(line)
        file.close()
    reviews=list(set(reviews))
    positive_value = 0
    neutral_value = 0
    negative_value = 0

    client = language_v1.LanguageServiceClient()
    type_ = language_v1.Document.Type.PLAIN_TEXT

    for review in reviews:
        language = ""
        document = {"content": review, "type_": type_, "language": language}

        encoding_type = language_v1.EncodingType.UTF8

        response = client.analyze_sentiment(request={'document': document, 'encoding_type': encoding_type})
        for sentence in response.sentences:
            sent_value = round(sentence.sentiment.score,2)
            if sent_value >= 0.2:  # 긍정일 때
                positive_value += 1
            elif 0.0 <= sent_value < 0.2:  # 중립일 때
                neutral_value += 1
            else:  # 부정일 때
                negative_value += 1

    total_value = positive_value + negative_value + neutral_value

    try:
        positive_value = int(positive_value / total_value * 100)
        negative_value = int(negative_value / total_value * 100)
        neutral_value = int(neutral_value / total_value * 100)
    except ZeroDivisionError:
        positive_value = 0
        neutral_value = 0
        negative_value = 0

    # 형용사만 추출하여 감정분석
    okt = Okt()
    pos = okt.pos(''.join(reviews))

    adj_list = []
    for word, tag in pos:
        if tag in ['Adjective']:
            adj_list.append(word)

    counts = Counter(adj_list)

    word_list = []
    frequency_list = []
    group_list = []

    for i in range(top_word_count):
        index = str(counts.most_common(top_word_count)[i]).rfind('\'')
        word = str(counts.most_common(top_word_count)[i])[2:index]
        word_list.append(word)
        frequency = re.sub(r'[^0-9]', '', str(counts.most_common(top_word_count)[i]))
        frequency_list.append(int(frequency))

    for word in word_list:
        language = ""
        document = {"content": word, "type_": type_, "language": language}

        encoding_type = language_v1.EncodingType.UTF8

        response = client.analyze_sentiment(request={'document': document, 'encoding_type': encoding_type})

        for sentence in response.sentences:
            group_list.append(round(float(sentence.sentiment.score), 2))

    for i in range(len(group_list)):
        if group_list[i] > 0.0:  # 긍정일 때
            group_list[i] = "긍정"
        elif group_list[i] == 0.0:
            group_list[i] = "중립"
        else:  # 부정일 때
            group_list[i] = "부정"

    if product == "trench_coat":
        SentValue_trench_coat(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node["word"] = word_list[i]
            node["value"] = frequency_list[i]
            node["group"] = group_list[i]
            nodes.append(node)

            SentScore_trench_coat(
                word=nodes[i]["word"],
                value=nodes[i]["value"],
                group=nodes[i]["group"],
            ).save()
    elif product == "coat":
        SentValue_coat(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_coat(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "padded_jacket":
        SentValue_padded_jacket(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_padded_jacket(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "military":
        SentValue_military(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_military(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "blazer":
        SentValue_blazer(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_blazer(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "leather_jacket":
        SentValue_leather_jacket(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_leather_jacket(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "fur_jacket":
        SentValue_fur_jacket(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_fur_jacket(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "short_sleeve_jacket":
        SentValue_short_sleeve_jacket(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_short_sleeve_jacket(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "long_sleeve_jacket":
        SentValue_long_sleeve_jacket(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_long_sleeve_jacket(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "shirt":
        SentValue_shirt(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_shirt(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "blouse":
        SentValue_blouse(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_blouse(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "neat":
        SentValue_neat(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_neat(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "hoodie":
        SentValue_hoodie(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_hoodie(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "sweat_shirt":
        SentValue_sweat_shirt(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_sweat_shirt(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "denim_pants":
        SentValue_denim_pants(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_denim_pants(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "mini_skirt":
        SentValue_mini_skirt(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_mini_skirt(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "skirt":
        SentValue_skirt(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_skirt(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "slacks":
        SentValue_slacks(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_slacks(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "short_pants":
        SentValue_short_pants(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_short_pants(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "sports_wear":
        SentValue_sports_wear(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_sports_wear(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "leggings":
        SentValue_leggings(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_leggings(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "sports_shoes":
        SentValue_sports_shoes(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_sports_shoes(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "sandal":
        SentValue_sandal(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_sandal(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "heel":
        SentValue_heel(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_heel(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "loafers":
        SentValue_loafers(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_loafers(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "walker":
        SentValue_walker(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_walker(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "dress":
        SentValue_dress(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_dress(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "back_pack":
        SentValue_back_pack(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_back_pack(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "tote_bag":
        SentValue_tote_bag(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_tote_bag(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "clutch_bag":
        SentValue_clutch_bag(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_clutch_bag(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "shoulder_bag":
        SentValue_shoulder_bag(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_shoulder_bag(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()
    elif product == "eco_bag":
        SentValue_eco_bag(
            positive_value=positive_value,
            negative_value=negative_value,
            neutral_value=neutral_value,
        ).save()
        nodes = []
        for i in range(top_word_count):
            node = dict()
            node['word'] = word_list[i]
            node['value'] = frequency_list[i]
            node['group'] = group_list[i]
            nodes.append(node)
        SentScore_eco_bag(
            word=nodes[i]['word'],
            value=nodes[i]['value'],
            group=nodes[i]['group'],
        ).save()

    print("NLP 종료")


print("분석할 옷의 이름을 영어로 입력해주세요 (예시) shirt")
product = input()
Data_Nlp(product)
