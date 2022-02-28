from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Configuration.config import TestData
import time

class Test_Home(BaseTest):

    def test_home_page_title(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.login(TestData.USER_EMAIL, TestData.PASSWORD)
        #Now Objects of Home Page could be called
        title = homePage.get_homePage_title(TestData.HOME_PAGE_TITLE)
        print("Verifying HomePage Title")
        assert title == TestData.HOME_PAGE_TITLE


    def test_home_page_header(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.login(TestData.USER_EMAIL, TestData.PASSWORD)
        header = homePage.get_header_value()
        print("Verifying HomePage Header")
        assert header == TestData.HOME_HEADER_VALUE


    def test_home_page_accountName(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.login(TestData.USER_EMAIL, TestData.PASSWORD)
        accountName = homePage.get_account_name()
        print("Verifying Account Name")
        assert accountName == TestData.ACCOUNT_NAME_VALUE


    def test_logout_button_visible(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.login(TestData.USER_EMAIL, TestData.PASSWORD)
        print("Verifying Logout Button")
        assert homePage.is_logout_button_visible()



