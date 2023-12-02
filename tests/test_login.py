import data
from conftest import driver
from locators import Locators
from test_util import login
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:

    def test_login_from_main_page(self, driver):
        driver.find_element(*Locators.ENTER_IN_ACC_BTN).click()
        login(driver, data.email, data.password)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BTN))
        assert driver.find_element(*Locators.ORDER_BTN).is_displayed()

    def test_login_from_lk(self, driver):
        driver.find_element(*Locators.ACC_BTN).click()
        login(driver, data.email, data.password)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BTN))
        assert driver.find_element(*Locators.ORDER_BTN).is_displayed()

    def test_login_from_registration(self, driver):
        driver.find_element(*Locators.ACC_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_LINK))
        driver.find_element(*Locators.REGISTRATION_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_LINK))
        driver.find_element(*Locators.ENTER_LINK).click()
        login(driver, data.email, data.password)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BTN))
        assert driver.find_element(*Locators.ORDER_BTN).is_displayed()

    def test_login_from_recover(self, driver):
        driver.find_element(*Locators.ACC_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.RECOVER_PWD_LINK))
        driver.find_element(*Locators.RECOVER_PWD_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_LINK))
        driver.find_element(*Locators.ENTER_LINK).click()
        login(driver, data.email, data.password)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BTN))
        assert driver.find_element(*Locators.ORDER_BTN).is_displayed()
