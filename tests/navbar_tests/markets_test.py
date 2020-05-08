import pytest, time
from pages.login_page import LoginPage
from pages.navbar_pages.markets_page import MarketsPage
from pages.account_page import AccountPage
from utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestMarkets:
    # Test cases 2.1.9 and 2.1.10
    #

    def test_login(self):
        global driver
        driver = self.driver
        global login
        login = LoginPage(driver)
        login.login_eula_check(utils.USERNAME, utils.PASSWORD)
        time.sleep(3)

    def test_clear_settings(self):
        ap = AccountPage(driver)
        ap.open_account_settings()
        ap.clear_settings()
        ap.yes_on_popup()

    def test_markets_open(self):
        global mp
        mp = MarketsPage(driver)
        mp.click_markets()
        assert mp.verify_markets_performance() == True

    def test_markets_quick_performance(self):
        mp.click_markets_quick_performance()
        assert mp.verify_markets_quick_performance() == True

    def test_markets_overview(self):
        mp.click_markets_overview()
        assert mp.verify_markets_overview() == True

    def test_markets_charts(self):
        mp.click_markets_charts()
        assert mp.verify_markets_chart() == True

    def test_markets_quoteboard(self):
        mp.click_quoteboard()
        assert mp.verify_quoteboard() == True

    def test_logout(self):
        login.logout()
        time.sleep(3)

