# 네이버 웹툰 "더 복서"의 제목, 링크, 별점 등 가져오고 평균평점 구하기

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=736989&weekday=thu"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, features="lxml")

# # class="title" 인 모든 td element 반환. type : result_set
# cartoons = soup.find_all("td", attrs={"class":"title"})

# # 웹툰 첫 페이지 제목과 링크 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

# 별점 정보 가져와서 평균 별점 구하기
cartoons = soup.find_all("div", attrs={"class": "rating_type"})

sum = 0
for cartoon in cartoons:
    rating = cartoon.strong.get_text()
    sum += float(rating)

avg = sum / len(cartoons)
print(avg)
