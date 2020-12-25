# requests 가 selenium 보다 빠르므로 동적페이지가 아닐 땐 selenium 을 사용하지 않는 게 더 빠름.

from bs4 import BeautifulSoup
import requests

url = "https://search.daum.net/search?w=tot&DA=UME&t__nil_searchbox=suggest&sug=&sugo=15&sq=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0&o=1&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"



res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")
res.raise_for_status()

data_rows = soup.find("table", attrs={"class": "tbl"}).find("tbody").find_all("tr")

for index, row in enumerate(data_rows):
    columns = row.find_all("td")

    print("==========매물 {}==========".format(index + 1))
    print("거래 :", columns[0].get_text().strip())
    print("면적 :", columns[1].get_text().strip(), "(공급/전용)")
    print("가격 :", columns[2].get_text().strip(), "(만원)")
    print("동 :", columns[3].get_text().strip())
    print("층 :", columns[4].get_text().strip())
