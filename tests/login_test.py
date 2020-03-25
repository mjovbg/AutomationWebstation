from selenium import webdriver
import pytest, time, moment
from pages.login_page_lkd import LoginPage
from pages.home_page import HomePage
from utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestLogin:
    def test_no_eula(self):
        '''
        Invalid Login test with correct username and password, but without eula checked.
        '''
        global driver
        driver = self.driver
        # driver.get(utils.URL)
        global login
        login = LoginPage(driver)
        login.login_no_eula(utils.USERNAME, utils.PASSWORD)
        time.sleep(2)

    def test_false_username(self):
        '''
        Invalid Login test with the wrong username.
        '''
        login.login_eula_check(utils.USERNAME, utils.FALSE_PASSWORD)
        time.sleep(2)

    def test_false_password(self):
        '''
        Invalid Login test with a wrong password.
        '''
        login.login_eula_check(utils.FALSE_USERNAME, utils.PASSWORD)
        time.sleep(2)

    def test_valid_login(self):
        '''
        Valid login test
        '''
        login.login_eula_check(utils.USERNAME, utils.PASSWORD)
        time.sleep(3)











