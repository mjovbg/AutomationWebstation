from base.selenium_driver import SeleniumDriver
from utils import utils as utils

class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators:
        self.username_id    =   "userName"
        self.password_id    =   "password"
        self.eula_css_check =   '#login > table:nth-child(4) > tbody > tr:nth-child(4) > td > label.checkBoxLabel > span'
        self.eula_confirm_id=   'eulaAccepted'
        self.login_btn_id   =   "loginUser"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_id).clear()
        self.driver.find_element_by_id(self.username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def check_eula(self):
        attribute = self.driver.find_element_by_id('eulaAccepted').get_attribute("checked")
        if attribute != 'true':
            self.driver.find_element_by_css_selector(self.eula_css_check).click()
    def uncheck_eula(self):
        attribute = self.driver.find_element_by_id('eulaAccepted').get_attribute("checked")
        if attribute == 'true':
            self.driver.find_element_by_css_selector(self.eula_css_check).click()
    def click_login(self):
        self.driver.find_element_by_id(self.login_btn_id).click()





