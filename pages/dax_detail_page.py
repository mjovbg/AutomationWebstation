from base.selenium_driver import SeleniumDriver
from locators.locators_login_page import LocatorsLP
from locators.locators_hp import LocatorsHp
from locators.locators_dax_dp import LocatorsDax, LocatorsDaxWaits, LocatorsDaxAsserts, LocatorsAdidas
from selenium import webdriver          # you need it for switching focus/windows.

class DaxDetailPage(SeleniumDriver, LocatorsDax, LocatorsAdidas):

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
        dax_element = self.isElementPresent(lda.overview_minichart_id)
        assert dax_element == True

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
        const_element = self.isElementPresent(lda.constituents_quoteboard_css, locatorType='css')
        assert const_element == True

    def click_overview(self):
        self.elementClick(LocatorsDax.overview_css, locatorType='css')
        self.waitForElement(ldw.overview_chart_1d_id)
        overview_element = self.isElementPresent(lda.overview_minichart_id)
        assert overview_element == True

    def click_chart(self):
        self.elementClick(LocatorsDax.chart_css, locatorType='css')
        self.waitForElement(ldw.chart_setdefault_id)
        chart_element = self.isElementPresent(lda.chart_savetemplate_id)
        assert chart_element == True

    def click_topflop(self):
        self.elementClick(LocatorsDax.topflop_css, locatorType='css')
        self.waitForElement(ldw.topflop_reload_css, locatorType='css')
        topflop_element = self.isElementPresent(lda.topflop_clos_css, locatorType='css')
        assert topflop_element == True

    def click_timessales(self):
        self.elementClick(LocatorsDax.timessales_css, locatorType='css')
        self.waitForElement(ldw.timesales_startdate_id)
        timesales_element = self.isElementPresent(lda.timesales_starthour_id)
        assert timesales_element == True

    def click_news(self):
        self.elementClick(LocatorsDax.news_css, locatorType='css')
        self.waitForElement(ldw.news_size_id)
        news_element = self.isElementPresent(lda.news_ecdata_css, locatorType='css')
        assert news_element == True

    def click_options(self):
        self.elementClick(LocatorsDax.options_css, locatorType='css')
        self.waitForElement(ldw.options_reset_id)
        options_element = self.isElementPresent(lda.options_search_id)
        assert options_element == True

    def click_derivatives(self):
        self.elementClick(LocatorsDax.derivatives_css, locatorType='css')
        self.waitForElement(ldw.derivatives_columnpicker_id)
        derivatives_element = self.isElementPresent(lda.derivatives_actionmenu_id)
        assert derivatives_element == True

    def click_adidas(self):
        self.click_constituents()
        self.elementClick(LocatorsAdidas.adidas_id)
        self.waitForElement(LocatorsAdidas.adidasid_wait_1D_id)
        adidas_element = self.isElementPresent(LocatorsAdidas.adidasid_assert_chart_id)
        assert adidas_element == True

    def click_adidas_profile(self):
        self.elementClick(LocatorsAdidas.profile_css, locatorType='css')
        self.waitForElement(LocatorsAdidas.profile_wait_website_css, locatorType='css')
        profile_element = self.isElementPresent(LocatorsAdidas.profile_assert_ir_css, locatorType= 'css')
        assert profile_element == True

    def click_adidas_financials(self):
        self.elementClick(LocatorsAdidas.financials_css, locatorType='css')
        self.waitForElement(LocatorsAdidas.financials_wait_picker_id)
        financials_element = self.isElementPresent(LocatorsAdidas.financials_assert_estimates_css, locatorType='css')
        assert financials_element == True

    def click_adidas_analyzer(self):
        self.elementClick(LocatorsAdidas.analyzer_css, locatorType= 'css')
        self.waitForElement(LocatorsAdidas.analyzer_wait_sortarrows_css, locatorType='css')
        analyzer_element = self.isElementPresent(LocatorsAdidas.analyzer_assert_chart_css, locatorType='css')
        assert analyzer_element == True

    def click_adidas_tradescreen(self):
        self.elementClick(LocatorsAdidas.traderscreen_css, locatorType='css')
        self.waitForElement(LocatorsAdidas.tradescreen_wait_picker_id)
        tradescreen_element = self.isElementPresent(LocatorsAdidas.tradescreen_assert_count_css, locatorType='css')
        assert tradescreen_element == True


