import pytest, time
from selenium import webdriver
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils import utils as utils

@pytest.mark.usefixtures("test_setup")
class TestNavbar:

    def test_login(self):
        global driver
        driver = self.driver
        global login
        login = LoginPage(driver)
        login.login_eula_check(utils.USERNAME, utils.PASSWORD)
        time.sleep(3)

    def test_markets(self):
        global hp
        hp = HomePage(driver)
        hp.click_markets()

    def test_currencies(self):
        hp.click_currencies()

    def test_commodities(self):
        hp.click_commodities()

    def test_fixincome(self):
        hp.click_fixincome()

    def test_futures(self):
        hp.click_futures()

    def test_news(self):
        hp.click_news()

    def test_workspace(self):
        hp.click_workspace()

    def test_wathlist(self):
        hp.click_watchlist()

    def test_covid(self):
        hp.click_covid()

    def test_trump(self):
        hp.click_trump()

    def test_screener(self):
        hp.click_screener()

    def test_funds(self):
        hp.click_funds()

    def test_portfolio(self):
        hp.click_portfolio()

    def test_calendar(self):
        hp.click_calednar()

    def test_analyzer(self):
        hp.click_analyzer()

    def test_backtester(self):
        hp.click_backtester()

    def test_alerts(self):
        hp.click_alerts()

    def test_ecdata(self):
        hp.click_ecdata()

    def test_etf(self):
        hp.click_etf()

    def test_derivatives(self):
        hp.click_derivatives()

    def test_realtime(self):
        hp.click_realtime()

    def test_logout(self):
        login.logout()
        time.sleep(3)

