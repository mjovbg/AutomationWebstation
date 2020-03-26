from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators:
        self.username_id        = "userName"
        self.password_id        = "password"
        self.eula_css_check     = '#login > table:nth-child(4) > tbody > tr:nth-child(4) > td > label.checkBoxLabel > span'
        self.eula_confirm       = '//*[@id="login"]/table[1]/tbody/tr[4]/td/label[1]/span'
        self.login_btn_id       = "loginUser"
        self.eula_warning_id    =  'diseabledCookiesMessage'
        self.user_button_id     = 'user-button'

    def enterUsername(self, username):
        self.clearElement(self.username_id)
        self.sendKeys(username, self.username_id)

    def enterPassword(self, password):
        self.clearElement(self.password_id)
        self.sendKeys(password, self.password_id)

    def clickEula(self):
        self.elementClick(self.eula_css_check, locatorType='css')

    def clickLogin(self):
        self.elementClick(self.login_btn_id)

    def verifyInvalidLogin(self):
        result = self.isElementPresent(self.eula_warning_id)
        return result

    def verifyValidLogin(self):
        result = self.isElementPresent(self.user_button_id)
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
