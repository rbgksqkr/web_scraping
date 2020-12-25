# 네이버 항공권에 접속해 항공권 검색. 다음 화면 로딩됐을 때 처리하는 방법 배움.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
browser.maximize_window()  # 전체화면

url = "https://flight.naver.com/flights/"

browser.get(url)

# 가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# 이번 달 27일, 다음 달 28일 선택
browser.find_elements_by_link_text("27")[0].click()
browser.find_elements_by_link_text("28")[1].click()

# 목적지 선택 후 검색 ex)제주도
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()
browser.find_element_by_link_text("항공권 검색").click()

try:
    # WebDriverWait 을 이용하여 최대 10초동안 응답을 기다림. 10초안에 그 뒤에 조건에 해당하는 element가 나온다면 바로 처리. 10초 넘으면 에러.
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    print(elem.text)
    # 가장 빠른 항공편
    # browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]").click()
    # browser.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/div[4]/ul/li[1]").click()
    # prices = browser.find_element_by_class_name("txt_total").text
    # print(prices)

except Exception as err:
    print(err)
# finally:
#     browser.quit()


