from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
import time

#Base Page : Parent of all classes : contains all the generic methods and utilities for all the pages

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        wait = WebDriverWait(self.driver, timeout=10)
        element = wait.until(EC.visibility_of_element_located(by_locator))
        element.click()

    def send_keys(self, by_locator, text):
        wait = WebDriverWait(self.driver, timeout=10)
        element = wait.until(EC.visibility_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)

    def get_element_text(self, by_locator):
        wait = WebDriverWait(self.driver, timeout=10)
        element = wait.until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_element_visible(self, by_locator):
        wait = WebDriverWait(self.driver, timeout=10)
        element = wait.until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        wait = WebDriverWait(self.driver, timeout=10)
        element = wait.until(EC.title_is(title))
        return self.driver.title