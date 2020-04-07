# Here you can define your setup and teardown functions
from utils import utils as utils
import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def test_setup(request, browser):
    driver = str(browser).lower()
    if browser == 'firefox':
        driver = webdriver.Firefox(executable_path='C:\MJ\MJ\PROJECTS\AutomationWebstation\drivers\geckodriver.exe')
    elif browser == 'edge':
        driver = webdriver.Edge()
    # elif browser == 'ie':
    #     driver = webdriver.Ie()
    else:
        driver = webdriver.Chrome(executable_path='C:\MJ\MJ\PROJECTS\AutomationWebstation\drivers\chromedriver.exe')

    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get(utils.URL)
    request.cls.driver = driver  # with this you are sending it to other classes
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


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
