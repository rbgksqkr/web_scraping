# headless : 브라우저를 띄우지 않고 백그라운드에서 동작. 내부적으로 접근.

from bs4 import BeautifulSoup
from selenium import webdriver
import time

# --------------selenium_movies2.py와 달라진 부분----------------
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options=options)
# -------------------------------------------------------------

browser.maximize_window()
url = "https://play.google.com/store/movies/top"
browser.get(url)

interval = 2

# 현재 문서 높이를 저장
curr_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # 화면 맨 밑으로 스크롤 내리기
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 스크롤 내린 후의 화면 높이 저장
    next_height = browser.execute_script("return document.body.scrollHeight")

    if curr_height == next_height:
        break

    curr_height = next_height

browser.get_screenshot_as_file("google_movie.png")

soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class": "Vpfmgd"})

for movie in movies:
    title = movie.find("div", attrs={"class": "WsMG1c nnK0zc"}).get_text()

    # 할인 전 가격
    origin_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if origin_price:
        origin_price = origin_price.get_text()
    # origin_price 가 존재하지 않으면 할인되지 않는 영화이므로 제외
    else:
        continue

    # 할인 후 가격
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    # 영화 구매 링크
    link = "https://play.google.com" + movie.find("a", attrs={"class":"JC71ub"})["href"]

    print("제목 :", title)
    print("할인 전 금액 :", origin_price)
    print("할인 후 금액 :", price)
    print("링크 :", link)
    print("-"*100)

browser.quit()
