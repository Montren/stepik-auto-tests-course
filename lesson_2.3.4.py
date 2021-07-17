from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

try:

    button = browser.find_element_by_tag_name("button")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = int(browser.find_element_by_id('input_value').text)
    y = calc(x)

    browser.find_element_by_id('answer').send_keys(y)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(7)
    browser.quit()
