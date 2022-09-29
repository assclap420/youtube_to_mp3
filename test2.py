from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# TODO: Create a gui for the code to run and for the user to inspect progress.
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

# TODO: Set the browser into headless mode
"""This code enters the website which converts
youtube URL to mp3"""
driver = webdriver.Chrome()
driver.get("https://en.onlymp3.to/")

for index in range(len(YT_url)):
    try:
        url_box = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="txtUrl"]')))
        url_box.send_keys(YT_url[index])
        url_box.send_keys(Keys.RETURN)
        download_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="btn251003"]/button[1]/a')))
        download_button.click()
    except Exception as error:
        print(error)

