import os

from google.cloud import language_v1

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\trendanalyzer-314714-63645bf47f21.json"

file = open('C:/무신사_레깅스.txt', 'r', encoding='utf-8')
lines = file.readlines()
reviews = []
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
        print(u"텍스트: {}".format(sentence.text.content))
        print(u"감정 점수: {:.2f}".format(float(sentence.sentiment.score)))
        if float(sentence.sentiment.score) > 0.1:     # 긍정일 때
            positive_value += 1
        elif float(sentence.sentiment.score) == 0.1:   # 부정일 때
            neutral_value += 1
        else:   # 부정일 때
            negative_value += 1

TotalReviewNum = positive_value + negative_value + neutral_value

print("긍정 : {:.2f}%, 부정 : {:.2f}%, 중립 : {:.2f}%".format(positive_value/TotalReviewNum*100, negative_value/TotalReviewNum*100, neutral_value/TotalReviewNum*100))
