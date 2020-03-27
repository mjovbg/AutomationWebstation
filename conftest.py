# Here you can define your setup and teardown functions
from utils import utils as utils
import pytest

@pytest.fixture(scope="class")
def test_setup(request, browser):
    from selenium import webdriver
    browser = str(browser).lower()
    driver = browser
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:\MJ\MJ\PROJECTS\AutomationFramework_2\Automation_from_scratch\drivers\chromedriver.exe")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="C:\MJ\MJ\PROJECTS\AutomationWebstation\drivers\geckodriver.exe")
    elif browser == 'ie':
        driver = webdriver.Ie(executable_path="C:\MJ\MJ\PROJECTS\AutomationWebstation\drivers\IEDriverServer.exe")
    elif browser == 'edge':
        driver = webdriver.Edge()

    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get(utils.URL)
    request.cls.driver = driver

    # creating teardown
    yield
    driver.close()
    driver.quit()
    print('Test Completed')

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
