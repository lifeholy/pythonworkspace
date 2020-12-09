#셀레니움을 이용한 구글 크롤링
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

find_text = "조코딩"
driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko")
elem = driver.find_element_by_name("q")
elem.send_keys(find_text)
elem.send_keys(Keys.RETURN)

#--------스크롤 다운 코드 시작
SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break

    last_height = new_height
#--------스크롤 다운 코드 끝

#작은 사진이미지 선택
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd") #첫째와 빈칸은 .을 표기
count = 1

for image in images:
    try:
        image.click()  
        time.sleep(3) #3초 대기
        # imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")  #src 주소의 값을 추출하여 imgUrl에 저장
        imgUrl = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img").get_attribute("src")


        urllib.request.urlretrieve(imgUrl, str(find_text) + str(count) + ".jpg") # imgUrl의 그림파일을 test.jpg로 저장함
        count = count + 1
    except:
        pass


driver.close()