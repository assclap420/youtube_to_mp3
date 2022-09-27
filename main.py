from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

"""This opens the text file which contains the 
youtube url, confirms whether the urls are from YouTube
"""
YT_url = []
url_txt = open("URL.txt", "r")
url_check = [*url_txt.read().split("\n")]
for i in url_check:
    if "https://www.youtube.com/" in i:
        YT_url.append(i)
url_txt.close()

browser = webdriver.Chrome()

"""This code enters the website which converts
youtube URL to mp3"""
driver = webdriver.Chrome()
driver.get("https://en.onlymp3.to/")

try:
    url_box = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.ID,"txtUrl")))
    for i in YT_url:
        url_box.send_keys(i)
        url_box.send_keys(Keys.RETURN)
except Exception as e:
    print(e)
# url_box = driver.find_elements("txtUrl")
for i in YT_url:
    url_box.send_keys(i)


