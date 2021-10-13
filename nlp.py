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
            if float(sentence.sentiment.score) >= 0.2:  # 긍정일 때
                positive_value += 1
            elif float(sentence.sentiment.score) >= -0.1 or float(sentence.sentiment.score) < 0.2:  # 부정일 때
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
    elif product == "":
        pass

    print("NLP 종료")


print("분석할 옷의 이름을 영어로 입력해주세요 (예시) shirt")
product = input()
Data_Nlp(product)
