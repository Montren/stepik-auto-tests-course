from selenium import webdriver
import time
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

try:

    browser.find_element_by_css_selector("[placeholder='Enter first name']").send_keys('aaa')
    browser.find_element_by_css_selector("[placeholder='Enter last name']").send_keys('bbb')
    browser.find_element_by_css_selector("[placeholder='Enter email']").send_keys('ccc')

    directory = "/Users/montren/Desktop"
    file_name = "test.txt"
    file_path = os.path.join(directory, file_name)
    browser.find_element_by_id('file').send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(7)
    browser.quit()
