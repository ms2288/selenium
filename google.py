from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
driver = webdriver.Chrome()  # 다운받은 chromedriver를 변수에 저장해놓음
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element_by_name("q")  # 검색창 찾기
elem.send_keys("조코딩")  # 원하는 검색어 입력하기
elem.send_keys(Keys.RETURN)  # 엔터키 입력하기
SCROLL_PAUSE_SEC = 1

# 스크롤 높이 가져옴
# 브라우저의 높이를 찾아 그 결과값을 last_height에 저장
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # 끝까지 스크롤 다운
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 1초 대기
    time.sleep(SCROLL_PAUSE_SEC)

    # 스크롤 다운 후 스크롤 높이 다시 가져옴
    new_height = driver.execute_script(
        "return document.body.scrollHeight")  # 브라우저의 높이를 새로 계산
    if new_height == last_height:  # 이전 계산한 높이와 같다면 스크롤이 끝까지 내려갔다는 의미
        # 코드를 실행했는데 오류가 발생하면 except안 break로 이동
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for image in images:
    try:
        image.click()  # 검색된 데이터에서 이미지 클릭
        time.sleep(2)
        imageUrl = driver.find_element_by_xpath(
            '/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').get_attribute("src")  # 이미지 링크 가져오기
        # 저장하고자 하는 이미지링크와 저장시 이미지 이름 지정
        urllib.request.urlretrieve(imageUrl, str(count) + ".jpg")
        count = count + 1
    except:
        pass

driver.close()
