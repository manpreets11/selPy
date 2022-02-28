from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class HomePage(BasePage):

    HEADER = (By.XPATH, "//div[@class='content-header']/h1")
    ACCOUNT_NAME = (By.XPATH, "//div[@id='navbarText']//a[@class='nav-link disabled']")
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Logout']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_homePage_title(self, title):
        return self.get_title(title)

    def is_logout_button_visible(self):
        return self.is_element_visible(self.LOGOUT_BUTTON)

    def get_header_value(self):
        if self.is_element_visible(self.HEADER):
            return self.get_element_text(self.HEADER)

    def get_account_name(self):
        if self.is_element_visible(self.ACCOUNT_NAME):
            return self.get_element_text(self.ACCOUNT_NAME)

