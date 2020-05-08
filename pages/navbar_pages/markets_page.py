from locators.locators_navbar.markets_locators import MarketsLocators
from base.selenium_driver import SeleniumDriver
import utils.custom_logger as cl
import logging


class MarketsPage(MarketsLocators, SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_markets(self):
        # Click on markets button in the navbar:
        self.elementClick(MarketsLocators.markets_css, locatorType='css')
        self.waitForElement(MarketsLocators.market_performance_arrows_xpath, locatorType='xpath')

    def verify_markets_performance(self):
        # Verify markets
        verify_markets = self.isElementPresent(MarketsLocators.market_performance_columnpicker_id)
        return verify_markets

    def click_markets_quick_performance(self):
        self.elementClick(MarketsLocators.market_quick_performance_css, locatorType='css')
        self.waitForElement(MarketsLocators.market_quick_performance_group_id)

    def verify_markets_quick_performance(self):
        verify_quick_performance = self.isElementPresent(MarketsLocators.market_quick_performance_next_id)
        return verify_quick_performance

    def click_markets_overview(self):
        self.elementClick(MarketsLocators.market_overview_css, locatorType= 'css')
        self.waitForElement(MarketsLocators.market_overivew_arrows_xpath, locatorType='xpath')

    def verify_markets_overview(self):
        verify_overview = self.isElementPresent(MarketsLocators.market_overview_picker_id)
        return verify_overview

    def click_markets_charts(self):
        self.elementClick(MarketsLocators.market_chart_css, locatorType= 'css')
        self.waitForElement(MarketsLocators.market_chart_reload_css, locatorType='css')

    def verify_markets_chart(self):
        verify_charts = self.isElementPresent(MarketsLocators.market_chart_picker_id)
        return verify_charts

    def click_quoteboard(self):
        self.elementClick(MarketsLocators.market_quoteboard_css, locatorType='css')
        self.waitForElement(MarketsLocators.market_quoteboard_group_id)

    def verify_quoteboard(self):
        verify_quoteboard = self.isElementPresent(MarketsLocators.market_quoteboard_picker_id)
        return verify_quoteboard
