import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from selenium import webdriver
from time import sleep

def intro(request):
    return render(request, 'index/data.html')

def index(request):
    kw = request.GET.get('kw', '')  # 검색어

    if kw: # 7가지 카테고리 각각의 상품코드 입력
        if kw == "카디건":
            product_code = "002020"
        elif kw == "레깅스": #예시1
            product_code = "003005"

        url = 'https://search.musinsa.com/category/' + product_code
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')  # lxml HTML parser 사용

        total_page = int(soup.find("span", {'class': "totalPagingNum"}).text) # 상품 페이지 최대갯수

        goods_links = []    # 개별 상품의 url을 저장하는 배열
        for i in range(1, total_page+1):
            i = str(i)
            page_url = 'https://search.musinsa.com/category/' + product_code + '?device=&d_cat_cd=' + product_code + '&brand=&rate=&page_kind=search&list_kind=small&sort=pop&sub_sort=&page='+i+'&display_cnt=90&sale_goods=&ex_soldout=&color=&price1=&price2=&exclusive_yn=&size=&tags=&sale_campaign_yn=&timesale_yn=&q='
            res = requests.get(page_url)
            soup = BeautifulSoup(res.text, 'lxml')  # lxml HTML parser 사용
            a_tags = soup.find_all("a", {'name': "goods_link"})

            for a_tag in a_tags:
                if a_tag["href"] not in goods_links:
                    goods_links.append(a_tag["href"])

        f = open("C:/새파일.txt", 'w', encoding='utf-8')
        print("전체 상품 개수 : ", len(goods_links)) # 상품 개수와 같은 데이터를 가진다.

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

        for i in range(len(goods_links)):
            TotalReview = 0
            print(i+1,"번째 상품의 리뷰 정보를 수집중입니다...")

            driver.get(goods_links[i])
            sleep(2)
            # ---- 리뷰 개수 파싱 시작 ---- #
            review_num = driver.find_element_by_css_selector('#estimate_style').text.split(' ')
            review_num = int(review_num[2].replace('(', '').replace(')', '').replace(',', ''))
            TotalReview += review_num
            # ---- 리뷰 개수 파싱 끝 ---- #

            if(review_num!=0):
                review_list = []
                if(review_num<=10): # 리뷰 개수가 10개 이하이면
                    for j in range(1, review_num+1):
                        j = str(j)
                        review = driver.find_element_by_css_selector(
                            '#wrapStyleEstimateList > div > div:nth-child('+j+') > div.postRight > div > div.pContent > div.summary > div > div.pContent_text > span').text
                        review_list.append(review)
                    for review in review_list:
                        f.write(review)
                else: # 리뷰 개수가 11개 이상일때
                    if(review_num % 10 == 0):
                        review_page = (review_num // 10)
                    else:
                        review_page = (review_num // 10) + 1
                    piece = review_num % 10
                    cnt = 0
                    reviews_per_page = 10

                    for k in range(review_page):
                        for i in range(3, 8):
                            if(cnt == review_num):
                                break
                            i=str(i)
                            driver.find_element_by_css_selector('#wrapStyleEstimateList > div > div.nslist_bottom > div.pagination.textRight > div > a:nth-child('+i+')').click()
                            sleep(1)
                            if(review_num-cnt<reviews_per_page):
                                reviews_per_page = piece
                            for j in range(1, reviews_per_page+1):
                                cnt += 1
                                j=str(j)
                                review = driver.find_element_by_css_selector('#wrapStyleEstimateList > div > div:nth-child('+j+') > div.postRight > div > div.pContent > div.summary > div > div.pContent_text > span').text
                                review_list.append(review)

                        if (cnt == review_num):
                            break
                        driver.find_element_by_css_selector(
                            '#wrapStyleEstimateList > div > div.nslist_bottom > div.pagination.textRight > div > a.fa.fa-angle-right.paging-btn.btn.next').click()  # 다음페이지 버튼
                        sleep(2)
                for review in review_list:
                    f.write(review)

        driver.close()

    context = {'kw': kw}
    return render(request, 'index/main.html', context)
