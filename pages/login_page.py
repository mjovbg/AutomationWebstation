from base.selenium_driver import SeleniumDriver
from locators.locators_login_page import LocatorsLP


class LoginPage(SeleniumDriver, LocatorsLP):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

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
        Method for login tests (both valid and invalid) when eula is checked.
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
        """
        Performs logout.
        """
        self.elementClick(LocatorsLP.user_button_id)
        self.elementClick(LocatorsLP.logout_css, locatorType='css')
