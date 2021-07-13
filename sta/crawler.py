import os
import requests
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime
from google.cloud import language_v1

product_code = "020006"  # product code를 변경하여서 크롤링할 품목을 변경할 수 있습니다.

url = 'https://search.musinsa.com/category/' + product_code
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')  # lxml HTML parser 사용

total_page = int(soup.find("span", {'class': "totalPagingNum"}).text)  # 상품 페이지 최대갯수

goods_links = []  # 개별 상품의 url 주소를 저장하는 배열

for i in range(1, total_page + 1):
    i = str(i)
    page_url = 'https://search.musinsa.com/category/' + product_code + '?device=&d_cat_cd=' + product_code + '&brand=&rate=&page_kind=search&list_kind=small&sort=pop&sub_sort=&page=' + i + '&display_cnt=90&sale_goods=&ex_soldout=&color=&price1=&price2=&exclusive_yn=&size=&tags=&sale_campaign_yn=&timesale_yn=&q='
    res = requests.get(page_url)
    soup = BeautifulSoup(res.text, 'lxml')  # lxml HTML parser 사용
    a_tags = soup.find_all("a", {'name': "goods_link"})

    for a_tag in a_tags:
        if a_tag["href"] not in goods_links:
            goods_links.append(a_tag["href"])

f = open("C:/새파일.txt", 'w', encoding='utf-8')

print("전체 상품 개수 : ", len(goods_links))  # 상품 개수와 같은 데이터를 가진다.

# ---- driver 기본 세팅 시작 ---- #
driver = webdriver.Chrome('C:\Chrome_Driver\chromedriver.exe')
driver.set_window_size(1920, 1080)
driver.get('https://store.musinsa.com/app/goods/1606138')
sleep(2)
# ---- 팝업체크 시작----#
driver.find_element_by_css_selector(
    '#page_product_detail > div.right_area.page_detail_product > div.popup_info.layer-suggest-join > div > a.btn-close').click()
sleep(1)
driver.find_element_by_css_selector(
    '#page_product_detail > div.right_area.page_detail_product > div.e-random-layer.is-active > button').click()
# ---- 팝업체크 끝---- #
# ---- driver 기본 세팅 끝 ---- #

TotalReviewNum = 0
review_list = []

# lists for review date

origin_list = [0 for i in range(12)]
copied_list = []
month_list = []

for i in range(len(goods_links)):

    print(i + 1, "번째 상품의 리뷰 정보를 수집중입니다...")
    driver.get(goods_links[i])
    sleep(2)
    # ---- 리뷰 개수 파싱 시작 ---- #
    review_num = driver.find_element_by_css_selector('#estimate_style').text.split(' ')
    review_num = int(review_num[2].replace('(', '').replace(')', '').replace(',', ''))
    TotalReviewNum += review_num
    # ---- 리뷰 개수 파싱 끝 ---- #

    if review_num != 0:
        if review_num <= 10:  # 리뷰 개수가 10개 이하 일 때
            for j in range(1, review_num + 1):
                j = str(j)
                review = driver.find_element_by_css_selector(
                    '#wrapStyleEstimateList > div > div:nth-child(' + j + ') > div.postRight > div > div.pContent > div.summary > div > div.pContent_text > span').text
                review_list.append(review)

                review_date = driver.find_element_by_css_selector(
                    '#wrapStyleEstimateList > div > div:nth-child(' + j + ') > div.postRight > div > div.profile > p > span.date.last').text
                if "일" or "시간" in review_date:
                    origin_list[datetime.today().month - 1] += 1  # 한달 이내에 작성된 리뷰
                else:
                    origin_list[int(review_date.split('.')[1]) - 1] += 1
        else:  # 리뷰 개수가 11개 이상 일 때
            if review_num % 10 == 0:
                review_page = (review_num // 10)
            else:
                review_page = (review_num // 10) + 1

            piece = review_num % 10
            cnt = 0
            reviews_per_page = 10

            for k in range(review_page):
                for div_num in range(3, 8):
                    if cnt == review_num:
                        break
                    div_num = str(div_num)
                    driver.find_element_by_css_selector(
                        '#wrapStyleEstimateList > div > div.nslist_bottom > div.pagination.textRight > div > a:nth-child(' + div_num + ')').click()
                    sleep(1)
                    if review_num - cnt < reviews_per_page:  # 마지막 페이지의 경우
                        reviews_per_page = piece
                    for j in range(1, reviews_per_page + 1):
                        cnt += 1
                        j = str(j)
                        review = driver.find_element_by_css_selector(
                            '#wrapStyleEstimateList > div > div:nth-child(' + j + ') > div.postRight > div > div.pContent > div.summary > div > div.pContent_text > span').text
                        review_list.append(review)

                        review_date = driver.find_element_by_css_selector(
                            '#wrapStyleEstimateList > div > div:nth-child(' + j + ') > div.postRight > div > div.profile > p > span.date.last').text
                        if "일" or "시간" in review_date:
                            origin_list[datetime.today().month - 1] += 1  # 한달 이내에 작성된 리뷰
                        else:
                            origin_list[int(review_date.split('.')[1]) - 1] += 1
                if cnt == review_num:
                    break
                driver.find_element_by_css_selector(
                    '#wrapStyleEstimateList > div > div.nslist_bottom > div.pagination.textRight > div > a.fa.fa-angle-right.paging-btn.btn.next').click()  # 다음페이지 버튼
                sleep(2)
driver.close()

print("리뷰 수집이 끝났습니다.")

copied_list = origin_list
copied_list.sort(reverse=True)  # 월별로 1씩 증가시킨 리스트를 내림차순으로 정렬

month_1 = origin_list.index(copied_list[0]) + 1
month_2 = origin_list.index(copied_list[1]) + 1
month_3 = origin_list.index(copied_list[2]) + 1

month_list.append(month_1)
if month_2 not in month_list:
    month_list.append(month_2)
if month_3 not in month_list:
    month_list.append(month_3)

print("패션 지수 출력 : ", end='')
for i in range(len(month_list)):
    print(f"{month_list[i]}월 ", end='')

review_list = set(review_list)
review_list = list(review_list)

for review in review_list:
    f.write(review + '\n')

f.close()

print("수집한 리뷰 개수 : ", TotalReviewNum)
################################################################################################################
# NLP

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\trendanalyzer-314714-63645bf47f21.json"

file = open('C:/무신사_미니원피스.txt', 'r', encoding='utf-8')
lines = file.readlines()
reviews = []
for line in lines:
    reviews.append(line)
file.close()

positive_value = 0
neutral_value = 0
negative_value = 0

for review in reviews:
    client = language_v1.LanguageServiceClient()
    type_ = language_v1.Document.Type.PLAIN_TEXT

    language = ""
    document = {"content": review, "type_": type_, "language": language}

    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_sentiment(request={'document': document, 'encoding_type': encoding_type})

    for sentence in response.sentences:
        if float(sentence.sentiment.score) > 0:
            positive_value += 1
        elif float(sentence.sentiment.score) < 0:
            negative_value += 1
        else:
            neutral_value += 1

print(f"긍정 : {positive_value/TotalReviewNum*100}%, 부정 : {negative_value/TotalReviewNum*100}%, 중립 : {neutral_value/TotalReviewNum*100}%")
