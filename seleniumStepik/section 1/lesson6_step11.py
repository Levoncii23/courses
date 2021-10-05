from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException  
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    fname = browser.find_element_by_xpath("//*[contains(@placeholder, 'name')]")
    fname.send_keys("a")

    try:
        sname = browser.find_element_by_xpath("//*[contains(@placeholder, 'last')]")
        sname.send_keys("s")
    except NoSuchElementException:
        print("False")
    email = browser.find_element_by_xpath("//*[contains(@placeholder, 'email')]")
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