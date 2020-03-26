# Here you can define your setup and teardown functions
from utils import utils as utils
import pytest

@pytest.fixture(scope="class")
def test_setup(request, browser):
    from selenium import webdriver
    # driver = browser
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:\MJ\MJ\PROJECTS\AutomationFramework_2\Automation_from_scratch\drivers\chromedriver.exe")
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(utils.URL)
        request.cls.driver = driver
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="C:\MJ\MJ\PROJECTS\AutomationWebstation\drivers\geckodriver.exe")

        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(utils.URL)
        request.cls.driver = driver         # with this you are sending it to other classes
    # creating teardown
    if request.cls is not None:
        request.cls.driver = driver
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
