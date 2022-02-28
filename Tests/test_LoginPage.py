import pytest

from Configuration.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from ddt import ddt, data, unpack

class Test_Login(BaseTest):

    def test_loginButton_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_loginButtonVisible()
        assert flag

    def test_loginPage_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_loginPage_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login(TestData.USER_EMAIL, TestData.PASSWORD)

