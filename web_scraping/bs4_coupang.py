# 쿠팡에서 상위 5페이지 내에 있는 노트북을 원하는 조건대로 검색

import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
for i in range(1, 6):
    print("<page " + str(i) + ">")
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class": re.compile("^search-product")})

    for item in items:
        # 광고제품 제외
        ad_badge = item.find("span",{"class":"ad-badge-text"})
        if ad_badge:
            continue

        # 리뷰 100개 이상, 평점 4.5이상 되는 것만 조회
        name = item.find("div", attrs={"class":"name"}).get_text()                      # 제품명
        price = item.find("strong", attrs={"class":"price-value"}).get_text()           # 가격
        rating = item.find("em", attrs={"class":"rating"})                              # 별점
        if rating:
            rating = rating.get_text()
        else:
            continue

        review = item.find("span", attrs={"class":"rating-total-count"})                # 별점 수
        if review:
            review = review.get_text() # ex) review : (24)
            review = review[1:-1]
        else:
            continue

        link = item.find("a", attrs={"class":"search-product-link"})["href"]

        if float(rating) >= 4.5 and int(review) >= 150:
            print("제품명 :", name)
            print("가격 :", price)
            print("별점 :", rating)
            print("별점 수 :", review)
            print("바로가기 :", "https://www.coupang.com" + link)
            print("-"*100)


