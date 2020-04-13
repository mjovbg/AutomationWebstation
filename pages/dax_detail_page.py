from base.selenium_driver import SeleniumDriver
from locators.locators_login_page import LocatorsLP
from locators.locators_hp import LocatorsHp
from locators.locators_dax_dp import LocatorsDax, LocatorsDaxWaits, LocatorsDaxAsserts
from selenium import webdriver          # you need it for switching focus/windows.

class DaxDetailPage(SeleniumDriver, LocatorsDax):

    def __init__(self, driver):
        # main advantage of super is with multiple inheritance where troubles may happen.
        # super allows: to avoid using the base class name explicitly; Working with Multiple Inheritance
        super().__init__(driver)
        self.driver = driver
        global ldw
        ldw = LocatorsDaxWaits
        global lda
        lda = LocatorsDaxAsserts

    def click_dax(self):
        self.elementClick(LocatorsDax.dax_symbol_id)
        self.waitForElement(ldw.overview_chart_1d_id)
        self.isElementPresent(lda.overview_minichart_id)

    def open_new_window(self):
        self.elementClick(LocatorsDax.action_menu_id)
        self.elementClick(LocatorsDax.open_newwindow_css, locatorType='css')
        # Find parent handle -> Main Window
        parent_handle = self.driver.current_window_handle
        # Find all handles, there should two handles
        handles = self.driver.window_handles
        # Switch to new window:
        for handle in handles:
            if handle not in parent_handle:
                self.driver.switch_to.window(handle)
                self.driver.maximize_window()

    def click_constituents(self):
        self.elementClick(LocatorsDax.constituents_css, locatorType='css')
        self.waitForElement(ldw.constituents_columnpicker_id)
        self.isElementPresent(lda.constituents_quoteboard_css, locatorType='css')

    def click_overview(self):
        self.elementClick(LocatorsDax.overview_css, locatorType='css')
        self.waitForElement(ldw.overview_chart_1d_id)
        self.isElementPresent(lda.overview_minichart_id)

    def click_chart(self):
        self.elementClick(LocatorsDax.chart_css, locatorType='css')
        self.waitForElement(ldw.chart_setdefault_id)
        self.isElementPresent(lda.chart_savetemplate_id)

    def click_topflop(self):
        self.elementClick(LocatorsDax.topflop_css, locatorType='css')
        self.waitForElement(ldw.topflop_reload_css, locatorType='css')
        self.isElementPresent(lda.topflop_clos_css, locatorType='css')

    def click_timessales(self):
        self.elementClick(LocatorsDax.timessales_css, locatorType='css')
        self.waitForElement(ldw.timesales_startdate_id)
        self.isElementPresent(lda.timesales_starthour_id)

    def click_news(self):
        self.elementClick(LocatorsDax.news_css, locatorType='css')
        self.waitForElement(ldw.news_size_id)
        self.isElementPresent(lda.news_ecdata_css, locatorType='css')

    def click_options(self):
        self.elementClick(LocatorsDax.options_css, locatorType='css')
        self.waitForElement(ldw.options_reset_id)
        self.isElementPresent(lda.options_search_id)

    def click_derivatives(self):
        self.elementClick(LocatorsDax.derivatives_css, locatorType='css')
        self.waitForElement(ldw.derivatives_columnpicker_id)
        self.isElementPresent(lda.derivatives_actionmenu_id)