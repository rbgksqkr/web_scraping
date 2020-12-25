# BeautifulSoup 을 이용해 오늘의 날씨, 네이버 종합 뉴스, IT 뉴스, 해커스 회화문장 가져오기

import requests
from bs4 import BeautifulSoup


def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


# 오늘의 날씨
def today_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
    main_info = soup.find("div", attrs={"class": "info_data"})
    curr_weather = main_info.find("p", attrs={"class": "cast_txt"}).get_text().strip()
    today_temp = main_info.find("p", attrs={"class": "info_temperature"}).get_text().replace("도씨", "")
    min_temp = main_info.find("span", attrs={"class": "min"}).get_text()
    max_temp = main_info.find("span", attrs={"class": "max"}).get_text()

    rain = soup.find("li", attrs={"class": "date_info today"}).find_all("span", attrs={"class": "rain_rate"})
    morning = rain[0].get_text().strip()
    afternoon = rain[1].get_text().strip()

    dust = soup.find("dd", attrs={"class": "lv1"}).get_text()
    fine_dust = soup.find("dd", attrs={"class": "lv2"}).get_text()

    print(curr_weather)
    print("현재 {0} (최저 : {1} / 최고 : {2})".format(today_temp, min_temp, max_temp))
    print("오전 : {0} / 오후 : {1}".format(morning, afternoon))
    print()
    print("미세먼지 {}".format(dust))
    print("초미세먼지 {}".format(fine_dust))
    print("\n\n")


# 네이버 헤드라인 뉴스
def headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com/"
    soup = create_soup(url)

    head_news = soup.find("ul", attrs={"class": "hdline_article_list"}).find_all("li", limit=3)

    for index, news in enumerate(head_news):
        title = news.find("a").get_text().strip()
        link = news.find("a")["href"]
        print("{0}.{1}".format(index+1, title))
        print("(링크 : {})".format(url + link))

    print("\n\n")


# 네이버 IT 관련 뉴스
def it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)

    news_list = soup.find("ul", attrs={"class": "type06_headline"}).find_all("li", limit=3)

    for index, news in enumerate(news_list):
        img_tag = news.find("img")
        a_index = 0
        if img_tag:
            a_index = 1

        a_tag = news.find_all("a")[a_index]
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        print("{0}.{1}".format(index+1, title))
        print("(링크 : {})".format(link))

    print("\n\n")


# 해커스토익 오늘의 회화
def today_english():
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)

    sen_list = soup.find_all("div", attrs={"class": "conv_txt"})

    print("(영어 지문)")
    korean = sen_list[1].find_all("div")
    for sentence in korean:
        sentence = sentence.find("b").get_text().strip()
        print(sentence)

    print()

    print("(한글 지문)")
    english = sen_list[0].find_all("div")
    for sentence in english:
        sentence = sentence.find("b").get_text().strip()
        print(sentence)

    print()


if __name__ == "__main__":
    today_weather()
    headline_news()
    it_news()
    today_english()
