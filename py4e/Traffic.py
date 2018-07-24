!pip install selenium
from selenium import webdriver

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
url = 'http://topis.seoul.go.kr/refRoom/openRefRoom_1_3.do'
driver.get(url)

# 년도 선택
year = driver.find_element_by_id('selYear')
year.click()
year2017 = driver.find_element_by_xpath('//*[@id="selYear"]/option[7]')
year2017.click()

# 지역 선택
# 종로구 ~ 강동구 option[i] 돌리기 4 ~ 22
region = driver.find_element_by_id('selRegCd')
region.click()
selReg = driver.find_element_by_xpath('//*[@id="selRegCd"]/option[4]')
selReg.click()

# 월 선택
# 1 ~ 12 월까지 option[i] 돌리기 1 ~ 12
month = driver.find_element_by_id('selMon')
month.click()
selMon = driver.find_element_by_xpath('//*[@id="selMon"]/option[1]')
selMon.click()


# 시간 선택
# 오전, 낮, 오후, 전일, 전체, 시간대별 option[i] 돌리기 1 ~ 22
i = 1
for i in 1:23
    time = driver.find_element_by_id('selTimeGrp')
    time.click()
    selTime = driver.find_element_by_xpath('//*[@id="selTimeGrp"]/option['+i+']')
    selTime.click()

    # 검색
    search = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr/td/table/tbody/tr/td[5]/button')
    search.click()

    # 엑셀 다운로드
    excel = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr/td/table/tbody/tr/td[6]/button[1]')
    excel.click()

    i = i + 1
