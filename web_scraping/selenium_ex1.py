# 네이버 로그인 시도

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()  # chrome webdriver 객체 생성

# 1. 웹사이트 이동
browser.get("https://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. ID, PW 입력
browser.find_element_by_id("id").send_keys("자신의 아이디")
browser.find_element_by_id("pw").send_keys("자신의 비밀번호")
browser.find_element_by_id("log.login").click()

# 4. 로그인 실패한 경우 ID, PW 재입력
time.sleep(3)
browser.find_element_by_id("id").send_keys("abc")
browser.find_element_by_id("pw").send_keys("abc")
browser.find_element_by_id("log.login").click()

# 5. html 문서 출력 후 닫기
print(browser.page_source)
browser.quit()


# elem = browser.find_element_by_id("query")  # 검색 엔진
# elem.send_keys("애플")
# elem.send_keys(Keys.ENTER)  # Keys.ENTER : 로그인 버튼 클릭 대신 엔터키 누르는 법. from selenium.webdriver.common.keys import Keys 필요
# browser.close()  # 탭 1개 종료
# browser.quit()  # 전체 종료

