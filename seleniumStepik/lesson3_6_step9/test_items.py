import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_basket_btn(browser):
    browser.get(link)
    time.sleep(30)
    assert len(browser.find_elements_by_class_name("btn-add-to-basket")) > 0, "Basket not found!"
