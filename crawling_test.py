import datetime
from time import sleep

import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def Data_Crawling(product_code):
    goods_code = product_code  # goods_code에 따라 크롤링할 품목이 변경됩니다.

    url = 'https://search.musinsa.com/category/' + goods_code
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

    f = open("C:/review.txt", 'w', encoding='utf-8') # C 드라이브에 위치하는 review.txt 파일 읽기전용으로 열기, review.txt 파일은 미리 생성해놔야 함

    review_list = []   #  리뷰 작성 날짜를 담기 위한 리스트
    origin_list = [0] * 12
    copied_list = [0] * 12

    for i in range(len(goods_links)):
        print(i + 1, "번째 상품의 리뷰 정보를 수집중입니다...")
        driver.get(goods_links[i])
        sleep(2)
        # ---- 리뷰 개수 파싱 시작 ---- #
        review_num = driver.find_element_by_css_selector('#estimate_style').text.split(' ')
        review_num = int(review_num[2].replace('(', '').replace(')', '').replace(',', ''))
        # ---- 리뷰 개수 파싱 끝 ---- #

        if review_num != 0:
            if review_num <= 10:  # 리뷰 개수 <= 10
                for j in range(1, review_num + 1):
                    j = str(j)
                    review = driver.find_element_by_css_selector(
                        '#wrapStyleEstimateList > div > div:nth-child(' + j + ') > div.review-contents > div.review-contents__text').text
                    review_list.append(review)

                    review_date = driver.find_element_by_css_selector(
                        '#wrapStyleEstimateList > div > div:nth-child(' + j + ') > div.review-profile > div > div.review-profile__text > p.review-profile__date').text

                    if "일" in review_date or "시간" in review_date:
                        if (datetime.today().day - 30) < 0:
                            origin_list[datetime.today().month - 2] += 1  # 저번달에 작성된 리뷰
                        else:
                            origin_list[datetime.today().month - 1] += 1  # 이번달에 작성된 리뷰
                    else:
                        origin_list[int(review_date.split('.')[1]) - 1] += 1
            else:  # 리뷰 개수 >= 11
                cnt = 0
                reviews_per_page = 10

                while True:
                    for button_num in range(3, 8): # 3번째 버튼(첫 페이지), 7번째 버튼(끝 페이지)
                        if cnt == review_num:
                            break
                        button_num = str(button_num)
                        driver.find_element_by_css_selector(
                            '#wrapStyleEstimateList > div > div.nslist_bottom > div.pagination.textRight > div > a:nth-child(' + button_num + ')').click()
                        sleep(1)
                        if review_num - cnt <= reviews_per_page:  # 마지막 페이지의 경우
                            reviews_per_page = review_num % 10
                        for j in range(1, reviews_per_page + 1):
                            cnt += 1
                            j = str(j)
                            review = driver.find_element_by_css_selector(
                                '#wrapStyleEstimateList > div > div:nth-child(' + j + ') > div.review-contents > div.review-contents__text').text # 리뷰 내용
                            review_list.append(review)

                            review_date = driver.find_element_by_css_selector(
                                '#wrapStyleEstimateList > div > div:nth-child(' + j + ') > div.review-profile > div > div.review-profile__text > p.review-profile__date').text # 리뷰 날짜

                            if "일" in review_date or "시간" in review_date:
                                if (datetime.today().day - 30) < 0:
                                    origin_list[datetime.today().month - 2] += 1  # 저번달에 작성된 리뷰
                                else:
                                    origin_list[datetime.today().month - 1] += 1  # 이번달에 작성된 리뷰
                            else:
                                origin_list[int(review_date.split('.')[1]) - 1] += 1
                    if cnt == review_num:
                        break
                    driver.find_element_by_css_selector(
                        '#wrapStyleEstimateList > div > div.nslist_bottom > div.pagination.textRight > div > a.fa.fa-angle-right.paging-btn.btn.next').click()  # 다음페이지 버튼
                    sleep(2)
    driver.close()

    print("리뷰 크롤링 완료")

    # origin_list 는 각 달마다의 언급량 횟수를 담고 있는 배열입니다.
    # 예) origin_list = [10, 21, 3, 5, 6, 7, 20, 11, 30, 99, 100, 106]
    # 리뷰 작성날짜가 1월 : 10개, 2월 : 21개, ... , 12월 106개

    for i in range(len(origin_list)):
        copied_list[i] = origin_list[i]

    copied_list.sort(reverse=True)  # 월별로 1씩 증가시킨 리스트를 내림차순으로 정렬

    month_1 = origin_list.index(copied_list[0]) + 1
    month_2 = origin_list.index(copied_list[1]) + 1
    month_3 = origin_list.index(copied_list[2]) + 1

    review_list = set(review_list)  # 중복된 리뷰를 제거하기 위해 review_list를 set 자료형으로 변환해줍니다.
    review_list = list(review_list) # set 자료형의 review_list를 다시 list 자료형으로 변환해줍니다.

    for review in review_list:
        f.write(review + '\n')
    f.close()