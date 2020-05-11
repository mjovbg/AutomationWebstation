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

    def click_currencies_chart(self):
        self.elementClick(CurrenciesLocators.currencies_chart_css, locatorType='css')
        self.waitForElement(CurrenciesLocators.currencies_chart_picker_id)

    def verify_currencies_chart(self):
        verify_chart = self.isElementPresent(CurrenciesLocators.currencies_chart_reload_css, locatorType='css')
        return verify_chart

    def click_currencies_quoteboard(self):
        self.elementClick(CurrenciesLocators.currencies_quoteboard_css, locatorType='css')
        self.waitForElement(CurrenciesLocators.currencies_quoteboard_picker_id)

    def verify_currencies_quoteboard(self):
        verify_quoteboard = self.isElementPresent(CurrenciesLocators.currencies_quote_board_aud_cad_css, locatorType='css')
        return verify_quoteboard

    def click_currencies_crossrates(self):
        self.elementClick(CurrenciesLocators.cross_rates_link, locatorType='link')
        self.waitForElement(CurrenciesLocators.cross_eur_usd_last_id)

    def verify_currencies_crossrates(self):
        verify_crossrates = self.isElementPresent(CurrenciesLocators.cross_usd_jpy_last_id)
        return verify_crossrates

    def click_currencies_cryptos(self):
        self.elementClick(CurrenciesLocators.cryptos_link, locatorType='link')
        self.waitForElement(CurrenciesLocators.cryptos_btc_flag_css, locatorType='css')

    def verify_currencies_cryptos(self):
        verify_cryptos = self.isElementPresent(CurrenciesLocators.cryptos_btc_link, locatorType='link')
        return verify_cryptos

    def click_currencies_crypto_pairs(self):
        self.elementClick(CurrenciesLocators.crypto_pairs_link, locatorType='link')
        self.waitForElement(CurrenciesLocators.crypto_pairs_group_id)

    def verify_currencies_crypto_pairs(self):
        verify_crypto_pairs = self.isElementPresent(CurrenciesLocators.crypto_pairs_picker_id)
        return verify_crypto_pairs

    def click_currencies_crypto_news(self):
        self.elementClick(CurrenciesLocators.crypto_news_link, locatorType='link')
        self.waitForElement(CurrenciesLocators.crypto_news_chart_reload_css, locatorType='css')

    def verify_currencies_crypto_news(self):
        verify_crypto_news = self.isElementPresent(CurrenciesLocators.crypto_news_chart_resizer_id)
        return verify_crypto_news
