from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    fname = browser.find_element_by_class_name("first")
    fname.send_keys("a")
    sname = browser.find_element_by_class_name("second")
    sname.send_keys("b")
    email = browser.find_element_by_class_name("third")
    email.send_keys("c")
    button = browser.find_element_by_class_name("btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(20)
    browser.quit()