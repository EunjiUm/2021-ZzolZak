import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'config.settings')
django.setup()
import re
from collections import Counter
from konlpy.tag import Okt
from index.models import *

with open("C:/negative_words_self.txt", encoding='utf-8') as neg:
    negative = neg.readlines()

with open("C:/positive_words_self.txt", encoding='utf-8') as pos:
    positive = pos.readlines()

with open("stopwords.txt", encoding='utf-8') as f:
    stopwords = f.read().splitlines()

negative = [neg.replace("\n", "") for neg in negative]
positive = [pos.replace("\n", "") for pos in positive]


def NLP(product):
    print(product + "에 대한 NLP 시작")
    reviews = []
    top_word_count = 10
    filepath = "data/" + product + ".txt"
    file = open(filepath, 'r', encoding='utf-8')
    lines = file.readlines()
    for line in lines:
        reviews.append(line)
    file.close()
    reviews = list(set(reviews))[:len(reviews)//2]

    positive_value = 0
    negative_value = 0
    neutral_value = 0
    adj_list = []

    okt = Okt()
    corpus = okt.pos(''.join(reviews))

    for word, tag in corpus:
        if tag in ['Adjective'] and word not in stopwords:
            adj_list.append(word)

    for adj in adj_list:
        if adj in positive:
            positive_value += 1
        elif adj in negative:
            negative_value += 1
        else:
            neutral_value += 1

    positive_value += neutral_value * 0.25
    negative_value += neutral_value * 0.25
    neutral_value *= 0.5
    total_value = positive_value + negative_value + neutral_value

    try:
        positive_value = int(positive_value / total_value * 100)
        negative_value = int(negative_value / total_value * 100)
        neutral_value = int(neutral_value / total_value * 100)
    except ZeroDivisionError:
        positive_value = 0
        negative_value = 0
        neutral_value = 0

    word_list = []
    frequency_list = []
    group_list = []
    counter = Counter(adj_list)
    counts = Counter({x: counter[x] for x in counter if len(x) > 1})

    for i in range(top_word_count):
        index = str(counts.most_common(top_word_count)[i]).rfind('\'')
        word = str(counts.most_common(top_word_count)[i])[2:index]
        word_list.append(word)
        frequency = re.sub(r'[^0-9]', '', str(counts.most_common(top_word_count)[i]))
        frequency_list.append(int(frequency))

    def sent_value(text):
        if text in positive:
            return "긍정"
        elif text in negative:
            return "부정"
        else:
            return "중립"

    for word in word_list:
        group_list.append(sent_value(word))

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

product_list = [
                'fur_jacket',
                'short_sleeve_jacket',
                'long_sleeve_jacket',
                'shirt',
                'blouse',
                'neat',
                'hoodie',
                'sweat_shirt',
                'denim_pants',
                'mini_skirt',
                'skirt',
                'slacks',
                'short_pants',
                'sports_wear',
                'leggings',
                'sports_shoes',
                'sandal',
                'heel',
                'loafers',
                'walker',
                'dress',
                'back_pack',
                'tote_bag',
                'clutch_bag',
                'shoulder_bag',
                'eco_bag']
for product in product_list:
    NLP(product)
print("-"*50)
print("NLP 종료")