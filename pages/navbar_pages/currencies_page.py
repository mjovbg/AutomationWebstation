from locators.locators_navbar.currencies_locators import CurrenciesLocators
from base.selenium_driver import SeleniumDriver
import utils.custom_logger as cl
import logging


class CurrenciesPage(CurrenciesLocators, SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_currencies(self):
        # Performance page is the default currencies page
        self.elementClick(CurrenciesLocators.currencies_icon_link, locatorType='link')
        self.waitForElement(CurrenciesLocators.currencies_peformance_picker_id)

    def verify_currencies_performance(self):
        verify_performance = self.isElementPresent(CurrenciesLocators.currencies_performance_arrows_xpath, locatorType='xpath')
        return verify_performance

    def click_currencies_quick_performance(self):
        self.elementClick(CurrenciesLocators.currencies_quick_performance_css, locatorType='css')
        self.waitForElement(CurrenciesLocators.currencies_quick_performance_next_id)

    def verify_currencies_quick_performance(self):
        verify_qp = self.isElementPresent(CurrenciesLocators.currencies_quick_performance_arrows_xpath, locatorType='xpath')
        return verify_qp

    def click_currencies_overview(self):
        self.elementClick(CurrenciesLocators.currencies_overview_css, locatorType='css')
        self.waitForElement(CurrenciesLocators.currencies_overview_arrows_id)

    def verify_currencies_overview(self):
        verify_overview = self.isElementPresent(CurrenciesLocators.currencies_overview_picker_id)
        return verify_overview






