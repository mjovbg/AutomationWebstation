from selenium import webdriver
import pytest, time, moment
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils import utils as utils

@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login_no_eula(self):
        '''
        Test in which eula is not checked.
        '''
        global driver
        driver = self.driver
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.uncheck_eula()
        login.click_login()
        time.sleep(2)

    def test_fail_username(self):
        '''
        Test with false username
        '''
        login = LoginPage(driver)
        login.enter_username(utils.FALSE_USERNAME)
        login.enter_password(utils.PASSWORD)
        login.check_eula()
        login.click_login()
        time.sleep(2)

    def test_fail_password(self):
        '''
        Test with false password
        '''
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.FALSE_PASSWORD)
        login.check_eula()
        login.click_login()
        time.sleep(2)

    def test_valid_login(self):
        '''
        valid login test
        '''
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.check_eula()
        login.click_login()
        time.sleep(8)

    def test_logout(self):
        """
        logout test and return to the login page.
        """
        hp = HomePage(driver)
        hp.click_user_button()
        hp.click_logout()
        time.sleep(3)





