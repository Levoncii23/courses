from selenium import webdriver
options = webdriver.ChromeOptions()

binary_yandex_driver_file = "C:/chromedriver/yandexdriver.exe" # path to YandexDriver

driver = webdriver.Chrome(binary_yandex_driver_file, options=options)
driver.get('https://yandex.ru')
driver.quit()