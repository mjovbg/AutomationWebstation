import pytest, time
from pages.login_page import LoginPage
from pages.navbar_pages.currencies_page import CurrenciesPage
from pages.account_page import AccountPage
from utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestCurrencies:
    # Test case 2.1.1 and 2.1.2
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

    def test_currencies_open(self):
        global cp
        cp = CurrenciesPage(driver)
        cp.click_currencies()
        assert cp.verify_currencies_performance() == True

    def test_currencies_quick_performance(self):
        cp.click_currencies_quick_performance()
        assert cp.verify_currencies_quick_performance() == True

    def test_currencies_overview(self):
        cp.click_currencies_overview()
        assert cp.verify_currencies_overview() == True





