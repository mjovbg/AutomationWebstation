from locators.locators_hp import LocatorsHp
from locators.locators_login_page import LocatorsLP
from base.selenium_driver import SeleniumDriver

class HomePage(LocatorsHp, LocatorsLP, SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_user_button(self):
        self.driver.find_element_by_id(LocatorsLP.user_button_id).click()

    def click_logout(self):
        self.driver.find_element_by_css_selector(LocatorsLP.logout_css, locatorType='css').click()

    def click_markets(self):
        self.elementClick(LocatorsHp.markets_css, locatorType='css')
        self.waitForElement(LocatorsHp.arrows_id)
        markets_element = self.isElementPresent(LocatorsHp.column_picker_class, locatorType='class')
        assert markets_element == True

    def click_currencies(self):
        self.elementClick(LocatorsHp.currencies_css, locatorType='css')
        self.waitForElement(LocatorsHp.arrows_id)
        currencies_element = self.isElementPresent(LocatorsHp.column_picker_class, locatorType='class')
        assert currencies_element == True

    def click_commodities(self):
        self.elementClick(LocatorsHp.commodities_css, locatorType='css')
        self.waitForElement(LocatorsHp.arrows_id)
        commodities_element = self.isElementPresent(LocatorsHp.column_picker_class, locatorType='class')
        assert commodities_element == True

    def click_fixincome(self):
        self.elementClick(LocatorsHp.fix_income_css, locatorType='css')
        self.waitForElement(LocatorsHp.arrows_id)
        fixincome_element = self.isElementPresent(LocatorsHp.column_picker_class, locatorType='class')
        assert fixincome_element == True

    def click_futures(self):
        self.elementClick(LocatorsHp.futures_css, locatorType='css')
        self.waitForElement(LocatorsHp.arrows_id)
        futures_element = self.isElementPresent(LocatorsHp.column_picker_class, locatorType='class')
        assert futures_element == True

    def click_news(self):
        self.elementClick(LocatorsHp.news_css, locatorType='css')
        self.waitForElement(LocatorsHp.news_home_css, locatorType='css')
        news_element = self.isElementPresent(LocatorsHp.news_search_class, locatorType='class')
        assert news_element == True

    def click_workspace(self):
        self.elementClick(LocatorsHp.workspace_css, locatorType='css')
        self.waitForElement(LocatorsHp.workspace_new_css, locatorType='css')
        workspace_element = self.isElementPresent(LocatorsHp.workspace_assert_css, locatorType='css')
        assert workspace_element == True

    def click_watchlist(self):
        self.elementClick(LocatorsHp.watchlist_css, locatorType='css')
        self.waitForElement(LocatorsHp.watchlist_new_css, locatorType='css')
        watchlist_element = self.isElementPresent(LocatorsHp.watchlist_assert_css, locatorType='css')
        assert watchlist_element == True

    def click_covid(self):
        self.elementClick(LocatorsHp.covid_css, locatorType='css')
        self.waitForElement(LocatorsHp.covid_map_css, locatorType='css')
        covid_element = self.isElementPresent(LocatorsHp.covid_assert_css, locatorType='css')
        assert covid_element == True

    def click_trump(self):
        self.elementClick(LocatorsHp.trump_css, locatorType='css')
        self.waitForElement(LocatorsHp.trump_icon_css, locatorType='css')
        trump_element = self.isElementPresent(LocatorsHp.trump_assert_css, locatorType='css')
        assert trump_element == True

    def click_screener(self):
        self.elementClick(LocatorsHp.screener_css, locatorType='css')
        self.waitForElement(LocatorsHp.screener_tab_css, locatorType='css')
        screener_element = self.isElementPresent(LocatorsHp.screener_assert_css, locatorType='css')
        assert screener_element == True

    def click_funds(self):
        self.elementClick(LocatorsHp.funds_css, locatorType='css')
        self.waitForElement(LocatorsHp.funds_overview_css, locatorType='css')
        funds_element = self.isElementPresent(LocatorsHp.funds_assert_css, locatorType='css')
        assert funds_element == True

    def click_portfolio(self):
        self.elementClick(LocatorsHp.portfolio_css, locatorType='css')
        self.waitForElement(LocatorsHp.portfolio_new_css, locatorType='css')
        portfolio_element = self.isElementPresent(LocatorsHp.portfolio_assert_css, locatorType='css')
        assert portfolio_element == True

    def click_calednar(self):
        self.elementClick(LocatorsHp.calendar_css, locatorType='css')
        self.waitForElement(LocatorsHp.calendar_filter_css, locatorType='css')
        calendar_element = self.isElementPresent(LocatorsHp.calendar_assert_css, locatorType='css')
        assert calendar_element == True

    def click_analyzer(self):
        self.elementClick(LocatorsHp.analyzer_css, locatorType='css')
        self.waitForElement(LocatorsHp.analyzer_filter_css, locatorType='css')
        analyzer_element = self.isElementPresent(LocatorsHp.analyzer_assert_css, locatorType='css')
        assert analyzer_element == True

    def click_backtester(self):
        self.elementClick(LocatorsHp.backtester_css, locatorType='css')
        self.waitForElement(LocatorsHp.backtester_help_css, locatorType='css')
        backtester_element = self.isElementPresent(LocatorsHp.backtester_assert_css, locatorType='css')
        assert backtester_element == True

    def click_alerts(self):
        self.elementClick(LocatorsHp.alerts_css, locatorType='css')
        self.waitForElement(LocatorsHp.alerts_calendar_css, locatorType='css')
        alerts_element = self.isElementPresent(LocatorsHp.alerts_assert_css, locatorType='css')
        assert alerts_element == True

    def click_ecdata(self):
        self.elementClick(LocatorsHp.economic_data_css, locatorType='css')
        self.waitForElement(LocatorsHp.economic_filter_css, locatorType='css')
        ecdata_element = self.isElementPresent(LocatorsHp.economic_assert_css, locatorType='css')
        assert ecdata_element == True

    def click_etf(self):
        self.elementClick(LocatorsHp.etfs_css, locatorType='css')
        self.waitForElement(LocatorsHp.etf_overview_css, locatorType='css')
        etf_element = self.isElementPresent(LocatorsHp.etf_assert_css, locatorType='css')
        assert etf_element == True

    def click_derivatives(self):
        self.elementClick(LocatorsHp.derivatives_css, locatorType='css')
        self.waitForElement(LocatorsHp.derivatives_issuers_css, locatorType='css')
        derivatives_element = self.isElementPresent(LocatorsHp.derivatives_assert_css, locatorType='css')
        assert derivatives_element == True

    def click_realtime(self):
        self.elementClick(LocatorsHp.realtime_css, locatorType='css')
        self.waitForElement(LocatorsHp.arrows_id)
        realtime_element = self.isElementPresent(LocatorsHp.realtime_assert_css, locatorType='css')
        assert realtime_element == True

    # Feedback??

