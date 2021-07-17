from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element_by_id('num1').text)
    y = int(browser.find_element_by_id('num2').text)

    z = str(x + y)

    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_visible_text(z)

    browser.find_element_by_css_selector('.btn.btn-default').click()

finally:
    time.sleep(5)
    browser.quit()
