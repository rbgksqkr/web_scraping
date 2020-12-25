# BeautifulSoup을 이용해 웹 페이지의 데이터 가져오는 법 연습

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, features="lxml")
# print(soup.title)
# print(soup.a) # soup 객체에서 처음 발견되는 a element 출력
# print(soup.a.attrs) # a element 의 속성정보 출력
# print(soup.a["href"]) # a element 의 href 속성 '값' 정보 출력

# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload" 인 a element 찾기
# print(soup.find(attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload" 인 어떤 element 찾기

# rank1 = soup.find("li", attrs={"class": "rank01"})
# print(rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
# rank1 = rank2.find_previous_sibling("li")
# print(rank1.a.get_text())

# ranks = rank1.find_next_siblings("li")

webtoon = soup.find("a", text="하렘의 남자들-5화")
print(webtoon.get_text())
