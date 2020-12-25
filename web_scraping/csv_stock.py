# 네이버 금융에서 BeautifulSoup으로 가져온 데이터를 csv파일로 저장

import csv
import requests
from bs4 import BeautifulSoup

filename = "2020_12_24_코스피_시가총액.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")  # 엑셀파일로 csv파일을 열 때 깨지는 경우 encoding="utf-8-sig"
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
# title = ["N", "종목명" ---]
writer.writerow(title)

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

for page in range(1, 2):
    url = url + str(page)
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")

    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1:  # 불필요한 데이터 skip(ex) 줄바꿈)
            continue
        data = [column.get_text().strip() for column in columns]  # string.strip() : 인자로 넣은 특정 문자 제거. 인자가 없으면 공백 제거
        writer.writerow(data)  # writer.writerow() : 인자로 list를 넣으면 csv파일에 순서대로 write
