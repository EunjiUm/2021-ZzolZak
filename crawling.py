import os

import django
from selenium.webdriver.common.keys import Keys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'config.settings')
django.setup()
import requests
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver


def code_matching(company, product):
    global goods_code
    if company == "musinsa":
        if product == "trench_coat":
            goods_code = "002008"
        elif product == "coat":
            print("겨울싱글코트 : 1 입력, 겨울더블코트 : 2 입력, 겨울기타코트 : 3 입력")
            detail = int(input())
            if detail == 1:
                goods_code = "002007"
            elif detail == 2:
                goods_code = "002024"
            else:
                goods_code = "002009"
        elif product == "slacks":
            goods_code = "003008"

        return goods_code
    elif company == "seoulstore":
        if product == "trench_coat":
            print("남성 옷 크롤링 : 1 입력, 여성 옷 크롤링 : 2 입력")
            gender = int(input())
            if gender == 1:
                goods_code = "1165"
            else:
                goods_code = "1066"
        elif product == "slacks":
            print("남성 옷 크롤링 : 1 입력, 여성 옷 크롤링 : 2 입력")
            gender = int(input())
            if gender == 1:
                goods_code = "1134"
            else:
                goods_code = "1027"

        return goods_code

    elif company == "ssf":
        if product == "trench_coat":
            print("남성 옷 크롤링 : 1 입력, 여성 옷 크롤링 : 2 입력")
            gender = int(input())
            if gender == 1:
                goods_code = "SFMA42A05A02A02"
                ssf_goods_code = "Trench-Coats"
            else:
                goods_code = "SFMA41A07A02A02"
                ssf_goods_code = "Trench-Coats"

        elif product == "slacks":
            print("남성 옷 크롤링 : 1 입력, 여성 옷 크롤링 : 2 입력")
            gender = int(input())
            if gender == 1:
                goods_code = "SFMA42A04A02"
                ssf_goods_code = "Formal"
            else:
                goods_code = "SFMA41A04A02A01"
                ssf_goods_code = "Long-Midi"

        return goods_code, ssf_goods_code


def musinsa_crawling(goods_code, goods_links, like):
    url = 'https://search.musinsa.com/category/' + goods_code
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')  # lxml HTML parser 사용

    total_page = int(soup.find("span", {'class': "totalPagingNum"}).text)  # 상품 페이지 최대갯수

    for i in range(1, total_page + 1):
        i = str(i)
        page_url = 'https://search.musinsa.com/category/' + goods_code + '?device=&d_cat_cd=' + goods_code + '&brand=&rate=&page_kind=search&list_kind=small&sort=pop&sub_sort=&page=' + i + '&display_cnt=90&sale_goods=&ex_soldout=&color=&price1=&price2=&exclusive_yn=&size=&tags=&sale_campaign_yn=&timesale_yn=&q='
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
    # ---- 팝업체크 끝---- #
    # ---- driver 기본 세팅 끝 ---- #

    for i in range(len(goods_links)):
        print(i + 1, "번째 상품의 리뷰 정보를 수집중입니다...")
        print("좋아요 개수 : ", like)
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
                    review = review.replace('\n', ' ')
                    f.write(review + " (작성날짜:")  # 해당 사이트의 옷 리뷰 txt 파일 쓰기
                    review_date = driver.find_element_by_css_selector(
                        '#wrapStyleEstimateList > div > div:nth-child(' + j + ') > div.review-profile > div > div.review-profile__text > p.review-profile__date').text
                    try:
                        like += int(driver.find_element_by_xpath(('//*[@id="product-top-like"]/p[2]/span').text).replace(",", ""))
                    except:
                        like += 0
                    if "일" in review_date or "시간" in review_date:
                        if (datetime.today().day - 30) < 0:
                            f.write(str(datetime.today().month - 2) + '월)\n')
                        else:
                            f.write(str(datetime.today().month - 1) + '월)\n')
                    else:
                        f.write([int(review_date.split('.')[1]) - 1] + '월)\n')
            else:  # 리뷰 개수 >= 11
                cnt = 0
                reviews_per_page = 10
                while True:
                    for button_num in range(3, 8):  # 3번째 버튼(첫 페이지), 7번째 버튼(끝 페이지)
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
                                '#wrapStyleEstimateList > div > div:nth-child(' + j + ') > div.review-contents > div.review-contents__text').text  # 리뷰 내용
                            review = review.replace('\n', ' ')
                            f.write(review + ' (작성날짜:')  # 해당 사이트의 옷 리뷰 txt 파일 쓰기

                            review_date = driver.find_element_by_css_selector(
                                '#wrapStyleEstimateList > div > div:nth-child(' + j + ') > div.review-profile > div > div.review-profile__text > p.review-profile__date').text  # 리뷰 날짜
                            try:
                                like += int(
                                    driver.find_element_by_xpath(('//*[@id="product-top-like"]/p[2]/span').text).replace(",", ""))
                            except:
                                like += 0
                            if "일" in review_date or "시간" in review_date:
                                if (datetime.today().day - 30) < 0:
                                    f.write(str(datetime.today().month - 2) + '월)\n')
                                else:
                                    f.write(str(datetime.today().month - 1) + '월)\n')
                            else:
                                f.write(str(int(review_date.split('.')[1]) - 1) + '월)\n')
                    if cnt == review_num:
                        break
                    driver.find_element_by_css_selector(
                        '#wrapStyleEstimateList > div > div.nslist_bottom > div.pagination.textRight > div > a.fa.fa-angle-right.paging-btn.btn.next').click()  # 다음페이지 버튼
                    sleep(2)
    driver.close()


def seoulstore_crawling(goods_code, goods_links, like):
    driver = webdriver.Chrome('C:\Chrome_Driver\chromedriver.exe')
    driver.set_window_size(1920, 1080)
    driver.get('https://www.seoulstore.com/categories/' + goods_code + '/recommend/desc')
    sleep(2)

    prev_height = driver.execute_script("return document.body.scrollHeight")

    # 웹페이지 맨 아래까지 무한 스크롤
    while True:
        # 화면가장 아래로 스크롤 내리기
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # 페이지 로딩 대기
        sleep(1)

        # 현재 문서 높이를 가져와서 저장
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")

        # 현재문서 높이를 가져와 저장
        curr_height = driver.execute_script("return document.body.scrollHeight")

        if curr_height == prev_height:
            break
        else:
            prev_height = driver.execute_script("return document.body.scrollHeight")
    num = 1
    while True:
        try:
            goods_links.append(driver.find_element_by_xpath(
                "//*[@id=\"" + goods_code + "\"]/div/div/div[2]/div/div[5]/div/div[1]/div[" + str(
                    num) + "]/a").get_attribute('href'))
            num += 1
        except:
            break
    review_num = []
    for i in range(1, num + 1):
        try:  # 리뷰가 있는 상품
            review_count = driver.find_element_by_xpath(
                "//*[@id=\"" + goods_code + "\"]/div/div/div[2]/div/div[5]/div/div[1]/div[" + str(
                    i) + "]/div/div[4]/span[3]").text
            review_num.append(int(str(review_count).replace("(", "").replace(")", "")))
            like += int(driver.find_element_by_xpath(
                "//*[@id=\"" + goods_code + "\"]/div/div/div[2]/div/div[5]/div/div[1]/div[" + str(
                    i) + "]/div/div[4]/span[5]"
            ).text)
        except:  # 리뷰가 없는 상품
            review_num.append(0)
            like += int(driver.find_element_by_xpath(
                "//*[@id=\"" + goods_code + "\"]/div/div/div[2]/div/div[5]/div/div[1]/div[" + str(
                    i) + "]/div/div[4]/span"
            ).text)
        finally:  # 리뷰도 없고 좋아요도 없는 상품
            continue

    sleep(2)
    driver.quit()

    driver = webdriver.Chrome('C:\Chrome_Driver\chromedriver.exe')
    driver.set_window_size(1920, 1080)
    for i in range(len(goods_links)):
        if review_num[i] == 0:
            continue
        r_idx = goods_links[i].rfind("/")
        product_id = goods_links[i][36:r_idx]
        print(i + 1, "번째 상품의 리뷰 정보를 수집중입니다...", end='')
        print("(", review_num[i], "개의 리뷰)")
        print("누적 좋아요 개수 : ", like)
        goods_links[i] = goods_links[i].replace("detail", "reviews")
        driver.get(goods_links[i])
        sleep(2)

        prev_height = driver.execute_script("return document.body.scrollHeight")

        # 무한 스크롤
        while True:
            # 화면가장 아래로 스크롤 내리기
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # 페이지 로딩 대기
            sleep(1)
            # 현재 문서 높이를 가져와서 저장
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
            # 현재문서 높이를 가져와 저장
            curr_height = driver.execute_script("return document.body.scrollHeight")
            if curr_height == prev_height:
                break
            else:
                prev_height = driver.execute_script("return document.body.scrollHeight")

        for i in range(1, review_num[i] + 1):
            try:
                review_date = str(driver.find_element_by_xpath(
                    "//*[@id=" + product_id + "]/div/div[2]/div[1]/div[" + str(
                        i) + "]/div/div[2]/span[2]").text).replace(" ", "")
                review = driver.find_element_by_xpath(
                    "//*[@id=" + product_id + "]/div/div[2]/div[1]/div[" + str(i) + "]/div/div[2]/p[2]").text
                review = review.replace('\n', ' ')
                f.write(review + " (작성날짜:")  # 해당 사이트의 옷 리뷰 txt 파일 쓰기
                f.write(str(int(review_date.split('.')[1]) - 1) + '월)\n')
            except:
                continue
    driver.close()


def ssf_crawling(goods_code, ssf_goods_code, like):
    # ---- driver 기본 세팅 시작 ---- #
    driver = webdriver.Chrome('C:\Chrome_Driver\chromedriver.exe')
    driver.set_window_size(1920, 1080)
    # ---- driver 기본 세팅 끝 ---- #

    url = "https://www.ssfshop.com/" + ssf_goods_code + "/list?dspCtgryNo=" + goods_code
    driver.get(url)
    driver.refresh()
    sleep(2)
    total_num = int(driver.find_element_by_xpath("//*[@id=\"godTotalCount\"]").text.replace("(", "").replace(")", "").replace(",",
                                                                                                                              ""))  # 상품 갯수
    if total_num <= 60:
        total_page = 1
    elif total_num % 60 == 0:
        total_page = total_num // 60
    else:
        total_page = total_num // 60 + 1

    for i in range(1, total_page + 1):
        i = str(i)
        print(f"상품의 {i}번 페이지입니다.")
        print("누적 좋아요 개수 : ", like)
        page_url = url + '&currentPage=' + i
        driver.get(page_url)
        review_tag_num = []
        one_page_max = 60
        if int(i) == total_page:  # 마지막 페이지에서
            one_page_max = total_num % 60
        for j in range(1, one_page_max + 1):
            if driver.find_element_by_xpath("//*[@id=\"dspGood\"]/li[" + str(j) + "]/a/div[2]/span[4]/span/em").text == '':
                continue
            else:
                try:  # 리뷰 있을때
                    driver.find_element_by_xpath('//*[@id="dspGood"]/li[' + str(j) + ']/a/div[2]/span[4]/span[2]')
                    like += int(
                        driver.find_element_by_xpath("//*[@id=\"dspGood\"]/li[" + str(j) + "]/a/div[2]/span[4]/span/em").text)
                    review_tag_num.append(j)
                except:  # 리뷰 없을때
                    like += int(
                        driver.find_element_by_xpath("//*[@id=\"dspGood\"]/li[" + str(j) + "]/a/div[2]/span[4]/span/em").text)

        for j in review_tag_num:
            driver.find_element_by_xpath("//*[@id=\"dspGood\"]/li[" + str(j) + "]/a").send_keys(Keys.ENTER)
            print(j, "번째 상품의 리뷰 정보를 수집중입니다...")
            sleep(1)
            total_review = int(
                (driver.find_element_by_xpath('//*[@id="review"]/h3[1]/em').text).replace("(", "").replace(")", "").replace(
                    ",", ""))  # 상품 리뷰 최대갯수
            if total_review == 1:  # 리뷰가 1개 있을 때
                review = (driver.find_element_by_xpath(
                    '//*[@id="searchGoodsReviewList"]/ul/li/dl/dd/div[2]').text)
                review_date = (
                    driver.find_element_by_xpath('//*[@id="searchGoodsReviewList"]/ul/li/dl/dd/div[3]/em[2]').text).split(".")
                review = review.replace('\n', ' ')
                f.write(review + " (작성날짜:")  # 해당 사이트의 옷 리뷰 txt 파일 쓰기
                f.write(str(int(review_date[1]) - 1) + '월)\n')
            elif total_review <= 10:  # 리뷰가 10개 이하일 때
                for i in range(1, total_review + 1):
                    review = (driver.find_element_by_xpath(
                        "//*[@id=\"searchGoodsReviewList\"]/ul/li[" + str(i) + "]/dl/dd/div[2]").text)
                    review_date = (
                        driver.find_element_by_xpath(
                            '//*[@id="searchGoodsReviewList"]/ul/li[' + str(i) + ')]/dl/dd/div[3]/em[2]').text).split(".")
                    review = review.replace('\n', ' ')
                    f.write(review + " (작성날짜:")  # 해당 사이트의 옷 리뷰 txt 파일 쓰기
                    f.write(str(int(review_date[1]) - 1) + '월)\n')
            else:  # 리뷰가 11개 이상일 때
                if total_review % 10 == 0:
                    total_review_page = total_review // 10
                else:
                    total_review_page = total_review // 10 + 1
                for review_page in range(1, total_review_page + 1):
                    if review_page <= 2:
                        click_num = review_page
                    else:
                        click_num = review_page + 1
                    driver.find_element_by_xpath('//*[@id="searchGoodsReviewList"]/div/a[' + str(click_num) + ']').click()
                    sleep(1)
                    if review_page == total_review_page:
                        one_review_max = total_review % 10
                    else:
                        one_review_max = 10
                    for i in range(1, one_review_max + 1):
                        review = (driver.find_element_by_xpath(
                            "//*[@id=\"searchGoodsReviewList\"]/ul/li[" + str(i) + "]/dl/dd/div[2]").text)
                        review_date = (
                            driver.find_element_by_xpath(
                                '//*[@id="searchGoodsReviewList"]/ul/li[' + str(i) + ']/dl/dd/div[3]/em[2]').text).split(".")
                        review = review.replace('\n', ' ')
                        f.write(review + " (작성날짜:")  # 해당 사이트의 옷 리뷰 txt 파일 쓰기
                        f.write(str(int(review_date[1]) - 1) + '월)\n')

            driver.get(page_url)
    driver.close()


print("크롤링할 사이트와 옷의 이름을 영어로 입력해주세요 (예시) musinsa shirt")
company, product = map(str, input().split())
f = open("data/" + company + "_" + product + ".txt", 'a+', encoding='utf-8')

goods_links = []  # 개별 상품의 url 주소를 저장하는 배열
like = 0  # 좋아요 개수

if company == "musinsa":
    goods_code = code_matching(company, product)
    musinsa_crawling(goods_code, goods_links, like)
elif company == "seoulstore":
    goods_code = code_matching(company, product)
    seoulstore_crawling(goods_code, goods_links, like)
else:
    goods_code, ssf_goods_code = code_matching(company, product)
    ssf_crawling(goods_code, ssf_goods_code, like)

print("리뷰 크롤링 완료")
f.close()
