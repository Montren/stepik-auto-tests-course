from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)
try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = int(browser.find_element_by_id('input_value').text)
    y = calc(x)

    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_id('robotCheckbox').click()
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element_by_id('robotsRule').click()

    # button = browser.find_element_by_tag_name("button")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(7)
    browser.quit()


