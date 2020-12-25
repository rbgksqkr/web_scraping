# User-Agent : 웹사이트가 사람이 직접 접속한 지 식별하는 데이터. 브라우저마다 다름. user agent string 검색하면 알 수 있음.
# 컴퓨터가 크롤링, 스크래핑하려는 접근을 차단하는 웹사이트가 있음. User-Agent 값을 사용하면 사람이 웹사이트에 들어가는 것으로 인식.

import requests

url = "https://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
print("응답코드 :", res.status_code)  # 200 이면 정상

with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)