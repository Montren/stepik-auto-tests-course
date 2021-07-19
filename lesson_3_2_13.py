import unittest
from selenium import webdriver
import time


class Test(unittest.TestCase):
    def test_1(self):
        browser = webdriver.Chrome()
        link1 = "http://suninjuly.github.io/registration1.html"
        browser.get(link1)
        input1 = browser.find_element_by_css_selector(".first_block .form-control.first")
        input2 = browser.find_element_by_css_selector(".first_block .form-control.second")
        input3 = browser.find_element_by_css_selector(".first_block .form-control.third")
        input1.send_keys("Ivan")
        input2.send_keys("Petrov")
        input3.send_keys("RANDOM.ORG")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    def test_2(self):
        browser = webdriver.Chrome()
        link2 = "http://suninjuly.github.io/registration2.html"
        browser.get(link2)
        input1 = browser.find_element_by_css_selector(".first_block .form-control.first")
        input2 = browser.find_element_by_css_selector(".first_block .form-control.second")
        input3 = browser.find_element_by_css_selector(".first_block .form-control.third")
        input1.send_keys("Ivan")
        input2.send_keys("Petrov")
        input3.send_keys("RANDOM.ORG")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()
