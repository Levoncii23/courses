from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/huge_form.html"
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
        element.send_keys("AB")
    button = browser.find_element_by_tag_name("button")
    button.click()
finally:
    time.sleep(30)
    browser.quit()
