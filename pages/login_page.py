from base.selenium_driver import SeleniumDriver
from locators.locators_login_page import LocatorsLP

class LoginPage(SeleniumDriver, LocatorsLP):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # # Locators:
        # self.username_id        = "userName"
        # self.password_id        = "password"
        # self.eula_css_check     = '#login > table:nth-child(4) > tbody > tr:nth-child(4) > td > label.checkBoxLabel > span'
        # self.eula_confirm       = '//*[@id="login"]/table[1]/tbody/tr[4]/td/label[1]/span'
        # self.login_btn_id       = "loginUser"
        # self.eula_warning_id    =  'diseabledCookiesMessage'
        # self.user_button_id     = 'user-button'

    def enterUsername(self, username):
        self.clearElement(LocatorsLP.username_id)
        self.sendKeys(username, LocatorsLP.username_id)

    def enterPassword(self, password):
        self.clearElement(LocatorsLP.password_id)
        self.sendKeys(password, LocatorsLP.password_id)

    def clickEula(self):
        self.elementClick(LocatorsLP.eula_css_check, locatorType='css')

    def clickLogin(self):
        self.elementClick(LocatorsLP.login_btn_id)

    def verifyInvalidLogin(self):
        result = self.isElementPresent(LocatorsLP.eula_warning_id)
        return result

    def verifyValidLogin(self):
        result = self.isElementPresent(LocatorsLP.user_button_id)
        return result

    def login_eula_check(self, username, password):
        """
        Method for login tests when eula is checked.
        """
        self.enterUsername(username)
        self.enterPassword(password)
        if self.checkAttribute('eulaAccepted') != 'true':
            self.clickEula()
        self.clickLogin()

    def login_no_eula(self, username, password):
        """
        Method for login tests when eula is NOT checked.
        """
        self.enterUsername(username)
        self.enterPassword(password)
        if self.checkAttribute('eulaAccepted') == 'true':
            self.clickEula()
        self.clickLogin()

    def logout(self):
        self.elementClick(LocatorsLP.user_button_id)
        self.elementClick(LocatorsLP.logout_css, locatorType='css')