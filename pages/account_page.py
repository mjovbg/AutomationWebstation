from base.selenium_driver import SeleniumDriver
from locators.locators_login_page import LocatorsLP
from locators.account_settings import LocatorsAccountSettings
import utils.custom_logger as cl
import logging, time


class AccountPage(SeleniumDriver, LocatorsAccountSettings):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_account_settings(self):
        self.elementClick(LocatorsAccountSettings.user_button_id)
        self.elementClick(LocatorsAccountSettings.account_settings_css, locatorType='css')
        # self.waitForElement(LocatorsAccountSettings.check_account_email_id)

    def verify_account_settings(self):
        # Verifying we are on the right page by finding change password button:
        verify = self.isElementPresent(LocatorsAccountSettings.change_account_pass_id)
        return verify

    def clear_settings(self):
        self.elementClick(LocatorsAccountSettings.clear_chart_css, locatorType='css')
        self.elementClick(LocatorsAccountSettings.clear_custom_css, locatorType='css')
        self.elementClick(LocatorsAccountSettings.clear_button_id)
        time.sleep(1)

    def yes_on_popup(self):
        self.elementClick(LocatorsAccountSettings.clear_custom_yes_xpath, locatorType='xpath')
        self.waitForElement(LocatorsAccountSettings.markets_button_text, locatorType='link')
