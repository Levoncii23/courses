from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_value = browser.find_element_by_id("treasure")
    x = x_value.get_attribute("valuex")
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    robot_chk = browser.find_element_by_id("robotCheckbox")
    robot_chk.click()
    robot_rule = browser.find_element_by_id("robotsRule")
    robot_rule.click()
    btn = browser.find_element_by_tag_name("button")
    btn.click()
finally:
    time.sleep(30)
    browser.quit()