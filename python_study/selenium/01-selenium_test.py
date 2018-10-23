from selenium import webdriver
import requests
import time
import re

driver = webdriver.Firefox()

driver.get("https://www.qichacha.com/")

cookies = driver.get_cookies()
#print(cookies)
cookies = {i["name"]:i["value"] for i in cookies}

headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36","cookie":str(cookies)}

driver.find_element_by_id("searchkey").send_keys("无锡兆辉贸易有限公司")
driver.find_element_by_id("V3_Search_bt").click()

#print(driver.page_source)

searchObj = re.search(r"firm_.*?.html",driver.page_source)

print(searchObj.group())

url = "https://m.qichacha.com/" + searchObj.group()

response = requests.get(url,headers=headers)

print(response.content.decode())

time.sleep(1)

driver.quit()


