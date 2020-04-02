from selenium import webdriver
import pytest, time, moment

from selenium import webdriver
import pytest, time, moment
from pages.login_page import LoginPage
# from ion.pages.home_page import HomePage
from tests.login_test import TestLogin
from utils import utils as utils

@pytest.mark.usefixtures("test_setup")
class TestNavbar():

    def test_login(self):
        driver = self.driver
        login = LoginPage(driver)
        login.login_eula_check(utils.USERNAME, utils.PASSWORD)



