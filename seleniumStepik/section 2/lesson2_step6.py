from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    answer = browser.find_element_by_id("answer").send_keys(y)
    btn = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    robot_chk = browser.find_element_by_css_selector("[for='robotCheckbox']")
    robot_chk.click()
    robot_rule = browser.find_element_by_css_selector("[for='robotsRule']")
    robot_rule.click()
    btn.click()
finally:
    time.sleep(20)
    browser.quit()