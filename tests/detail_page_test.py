import pytest, time, moment
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.dax_detail_page import DaxDetailPage
from utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestDetailPage:
    # DAX

    def test_login(self):
        global driver
        driver = self.driver
        global login
        login = LoginPage(driver)
        login.login_eula_check(utils.USERNAME, utils.PASSWORD)
        time.sleep(3)

    def test_markets(self):
        # global hp
        hp = HomePage(driver)
        hp.click_markets()

    def test_symbol(self):
        # DAX Index
        global dp
        dp = DaxDetailPage(driver)
        dp.click_dax()
        time.sleep(3)

    def test_constituents(self):
        dp.click_constituents()
        time.sleep(2)

    def test_overview(self):
        dp.click_overview()
        time.sleep(2)

    def test_chart(self):
        dp.click_chart()
        time.sleep(3)

    def test_topflop(self):
        dp.click_topflop()
        time.sleep(2)

    def test_timessales(self):
        dp.click_timessales()
        time.sleep(2)

    def test_news(self):
        dp.click_news()
        time.sleep(2)

    def test_options(self):
        dp.click_options()
        time.sleep(2)

    def test_derivatives(self):
        dp.click_derivatives()
        time.sleep(2)

    def test_logout(self):
        login.logout()
        time.sleep(2)