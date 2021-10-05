from selenium import webdriver
from selenium.webdriver.support import select
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    num1 = int(browser.find_element_by_id("num1").text)
    num2 = int(browser.find_element_by_id("num2").text)
    res = num1 + num2
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(str(res))
    browser.find_element_by_class_name("btn").click()
finally:
    time.sleep(20)
    browser.quit()
