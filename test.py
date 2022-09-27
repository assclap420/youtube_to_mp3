from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://hk.yahoo.com/?p=us")
try:
    url_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="header-search-input"]')))
    url_box.send_keys("success")
    url_box.send_keys(Keys.RETURN)
except Exception as e:
    print(e)
url_box = driver.find_element(By.XPATH,'//*[@id="header-search-input"]')
url_box.send_keys("success")

