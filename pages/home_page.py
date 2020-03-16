
class HomePage():
    def __init__(self, driver):
        self.driver = driver
        # Locators - Header:
        self.user_button_id      = 'user-button'
        self.logout_button_css   = '#user-menu > ul > li:nth-child(11) > a'

        # Locators - Navigation - Vertical bar:
        self.markets_css    =   '#lowerDiv > div.navigation-vertical-container > table > tbody > tr:nth-child(1) > td > div > table > tbody > tr > td.icon-container.icon-container-with-tree > a'


    def click_user_button(self):
        self.driver.find_element_by_id(self.user_button_id).click()

    def click_logout(self):
        self.driver.find_element_by_css_selector(self.logout_button_css).click()


