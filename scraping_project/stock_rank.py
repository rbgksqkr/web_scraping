# 주식 실시간 인기 종목 1~10위 가져오기

from bs4 import BeautifulSoup
from selenium import webdriver
import time

# headless Chrome 구현
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://m.stock.naver.com/"
browser.get(url)

# 동적인 페이지 로딩
browser.execute_script("window.scrollTo(0, 540)")
time.sleep(2)

soup = BeautifulSoup(browser.page_source, "lxml")
browser.quit()

print("[실시간 종목 순위]")

data_rows = soup.find("div", attrs={"class":"ct_box trend_box _home_trend_wrapper"}).find("tbody").find_all("tr")

for index, data in enumerate(data_rows):
    elem = data.find_all("td")
    print("{0}. {1}".format(index+1, elem[2].text))



