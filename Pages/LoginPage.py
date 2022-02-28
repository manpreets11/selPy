from Configuration.config import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage


class LoginPage(BasePage):

    #By Locators
    EMAIl_FIELD = (By.ID, "Email")
    PASSWORD_FIELD = (By.ID, "Password")
    CONTINUE_BUTTON = (By.ID, "continue")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    #Constrcutor of page class
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        self.driver.maximize_window()
    #Page Actions
    def get_loginPage_title(self, title):
        return self.get_title(title)

    def is_loginButtonVisible(self):
        return self.is_element_visible(self.LOGIN_BUTTON)

    #After Logging in, Object of Next Landing page i.e HomePage is returened to obtain
    #page chaining concept
    def login(self, username, password):
        self.send_keys(self.EMAIl_FIELD, username )
        self.send_keys(self.PASSWORD_FIELD, password )
        self.click(self.LOGIN_BUTTON)
        return HomePage(self.driver)


