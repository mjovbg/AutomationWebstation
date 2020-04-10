from base.selenium_driver import SeleniumDriver
from locators.locators_login_page import LocatorsLP
from locators.locators_hp import LocatorsHp
from locators.locators_dax_dp import LocatorsDax
import time

class DaxDetailPage(SeleniumDriver, LocatorsDax):

    def __init__(self, driver):
        # main advantage of super is with multiple inheritance where troubles may happen.
        # super allows: to avoid using the base class name explicitly; Working with Multiple Inheritance
        super().__init__(driver)
        self.driver = driver

    def click_dax(self):
        self.elementClick(LocatorsDax.dax_symbol_id)
        time.sleep(3)

    def click_constituents(self):
        self.elementClick(LocatorsDax.constituents_css, locatorType='css')
        time.sleep(3)

    def click_overview(self):
        self.elementClick(LocatorsDax.overview_css, locatorType='css')
        time.sleep(3)

    def click_chart(self):
        self.elementClick(LocatorsDax.chart_css, locatorType='css')
        time.sleep(3)

    def click_topflop(self):
        self.elementClick(LocatorsDax.topflop_css, locatorType='css')
        time.sleep(3)

    def click_timessales(self):
        self.elementClick(LocatorsDax.timessales_css, locatorType='css')
        time.sleep(3)

    def click_news(self):
        self.elementClick(LocatorsDax.news_css, locatorType='css')
        time.sleep(3)

    def click_options(self):
        self.elementClick(LocatorsDax.options_css, locatorType='css')
        time.sleep(3)

    def click_derivatives(self):
        self.elementClick(LocatorsDax.derivatives_css, locatorType='css')
        time.sleep(3)