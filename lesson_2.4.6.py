from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/cats.html")
browser.implicitly_wait(5)

try:

    browser.find_element_by_id("button")

finally:
    time.sleep(3)
    browser.quit()
