# "google movie"에서 영화정보를 가져올 때 동적인 페이지이기 때문에 로딩되지 않은 영화 정보는 가져올 수 없음.

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
}
url = "https://play.google.com/store/movies/top"
res = requests.get(url, headers=headers)
res.raise_for_status()


soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div",attrs={"class":"ImZGtf mpg5gc"})
for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)
