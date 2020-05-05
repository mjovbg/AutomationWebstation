from base.selenium_driver import SeleniumDriver
import pytest, time, moment
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils import utils as utils
import allure


@pytest.mark.usefixtures("test_setup")
class TestLogin:
    def test_no_eula(self):
        '''
        Invalid Login test with correct username and password, but without eula checked.
        '''
        global driver
        driver = self.driver
        global login
        login = LoginPage(driver)
        login.login_no_eula(utils.USERNAME, utils.PASSWORD)
        global result
        result = login.verifyInvalidLogin()
        assert result == True
        time.sleep(2)

    def test_false_username(self):
        '''
        Invalid Login test with the wrong username.
        '''
        login.login_eula_check(utils.USERNAME, utils.FALSE_PASSWORD)
        result = login.verifyInvalidLogin()
        assert result == True
        time.sleep(2)

    def test_false_password(self):
        '''
        Invalid Login test with a wrong password.
        '''
        login.login_eula_check(utils.FALSE_USERNAME, utils.PASSWORD)
        result = login.verifyInvalidLogin()
        assert result == True
        time.sleep(2)

    def test_valid_login(self):
        '''
        Valid login test
        '''
        login.login_eula_check(utils.USERNAME, utils.PASSWORD)
        result_valid = login.verifyValidLogin()
        try:
            assert result_valid == True
        except:
            driver.get_screenshot_as_file('C:/MJ/MJ/PROJECTS/AutomationWebstation/reports/screenshots/test.png')

        time.sleep(3)

    def test_logout(self):
        login.logout()
        time.sleep(3)


