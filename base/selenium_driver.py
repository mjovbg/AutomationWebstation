from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utils.custom_logger as cl
import logging
import time, os, moment, inspect


class SeleniumDriver():
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self):

        # step by step Automation - lesson 52
        current_time = moment.now().strftime('%d-%m-%Y__%H-%M-%S')
        test_name = inspect.stack()[1][3]
        screenshot_name = test_name + '_ '+current_time
        self.driver.save_screenshot('C:/MJ/MJ/PROJECTS/AutomationWebstation/reports/screenshots/' + screenshot_name + '.png')

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator + " and locatorType: " + locatorType)
        return element

    def elementClick(self, locator, locatorType="id"):
        '''
        just clicks on the element
        :param locator:
        :param locatorType:
        :return:
        '''
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator, locatorType="id"):
        '''
        just sends data to elements!
        :param locator:
        :param locatorType:
        :return:
        '''
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def clearElement(self, locator, locatorType="id"):
        '''
        clear fields of any inputs.
        '''
        try:
            element = self.getElement(locator, locatorType)
            element.clear()
            self.log.info("Cleared the element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot clear the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def checkAttribute(self, locator, locatorType="id"):
        '''
        Used for checkboxes to check their status (checked/not checked).
        '''
        # element = None
        # try:
        element = self.getElement(locator, locatorType).get_attribute('checked')
        # print("Status of element with locator: " + locator + " locatorType: " + locatorType + 'is' + element)
        # except:
        #     print("Cannot confirm the status of the element with locator: " + locator + " locatorType: " + locatorType)
        #     print_stack()
        return element

    def isElementPresent(self, locator, locatorType='id'):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id",
                       timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             "stopFilter_stops-0")))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element