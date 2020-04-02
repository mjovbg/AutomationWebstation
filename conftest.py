# Here you can define your setup and teardown functions
from utils import utils as utils
import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def test_setup(request):
    driver = webdriver.Chrome(executable_path="C:\MJ\MJ\PROJECTS\AutomationFramework_2\Automation_from_scratch\drivers\chromedriver.exe")
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get(utils.URL)
    request.cls.driver = driver         # with this you are sending it to other classes
    # creating teardown
    yield
    driver.close()
    driver.quit()
    print('Test Completed')




