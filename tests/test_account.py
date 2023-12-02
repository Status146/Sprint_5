import data
from conftest import driver
from locators import Locators
from test_util import login
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestAccount:
    def test_account_page(self, driver):
        driver.find_element(*Locators.ENTER_IN_ACC_BTN).click()
        login(driver, data.email, data.password)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BTN))
        driver.find_element(*Locators.ACC_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.EXIT_BTN))
        assert driver.find_element(*Locators.EXIT_BTN).is_displayed()

    def test_logout(self, driver):
        driver.find_element(*Locators.ENTER_IN_ACC_BTN).click()
        login(driver, data.email, data.password)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BTN))
        driver.find_element(*Locators.ACC_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.EXIT_BTN))
        driver.find_element(*Locators.EXIT_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BTN))
        assert driver.find_element(*Locators.ENTER_BTN).is_displayed()

    def test_constructor_conversion(self, driver):
        driver.find_element(*Locators.ENTER_IN_ACC_BTN).click()
        login(driver, data.email, data.password)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BTN))
        driver.find_element(*Locators.ACC_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.EXIT_BTN))
        driver.find_element(*Locators.CONSTRUCTOR_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.HEADER_MK_BURGER))
        assert driver.find_element(*Locators.HEADER_MK_BURGER).is_displayed()

    def test_logo_conversion(self, driver):
        driver.find_element(*Locators.ENTER_IN_ACC_BTN).click()
        login(driver, data.email, data.password)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BTN))
        driver.find_element(*Locators.ACC_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.EXIT_BTN))
        driver.find_element(*Locators.LOGO_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.HEADER_MK_BURGER))
        assert driver.find_element(*Locators.HEADER_MK_BURGER).is_displayed()
