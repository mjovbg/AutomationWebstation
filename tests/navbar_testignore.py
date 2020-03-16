from selenium import webdriver
import pytest, time, moment
from webstation.pages.login_page import LoginPage
from webstation.pages.home_page import HomePage
from webstation.tests.login_test import TestLogin
from webstation.utils import utils as utils

@pytest.mark.usefixtures("test_setup")
class TestNavbar():

    def test_valid_login(self):
        login = TestLogin
        login.test_valid_login()




