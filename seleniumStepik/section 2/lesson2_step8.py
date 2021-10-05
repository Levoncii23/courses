from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    firstName = browser.find_element_by_name("firstname").send_keys("Lev")
    lastName = browser.find_element_by_name("lastname").send_keys("Grechishnikov")
    email = browser.find_element_by_name("email").send_keys("levoncii")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    upload_btn = browser.find_element_by_id("file").send_keys(file_path)
    sedn_btn = browser.find_element_by_tag_name("button").click()
finally:
    time.sleep(20)
    browser.quit()
