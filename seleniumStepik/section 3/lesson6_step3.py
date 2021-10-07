from selenium import webdriver
import pytest
import time 
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

list_ans = []

def get_answer():
    return str(math.log(int(time.time())))

@pytest.fixture
def browser():
    browser = webdriver.Chrome()

    yield browser
    browser.quit()

@pytest.mark.parametrize('links',["https://stepik.org/lesson/236895/step/1",
'https://stepik.org/lesson/236896/step/1',
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"])
def test_ufo(browser, links): 
    
    browser.get(links)
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
    text = browser.find_element_by_tag_name("textarea")
    text.send_keys(get_answer())
    btn = browser.find_element_by_class_name("submit-submission")
    btn.click()
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "pre")))
    correct = browser.find_element_by_tag_name("pre")
    assert correct.text == "Correct!", correct.text

