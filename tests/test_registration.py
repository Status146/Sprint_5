import data
import helpers
from conftest import driver
from locators import Locators
from test_util import register
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:
    def test_registration_user_succes(self, driver):
        driver.find_element(*Locators.ENTER_IN_ACC_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_LINK))
        driver.find_element(*Locators.REGISTRATION_LINK).click()
        register(driver, data.name, helpers.generate_email(), helpers.generate_password())
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BTN))
        assert driver.find_element(*Locators.ENTER_BTN).is_displayed()

    def test_registration_empty_name(self, driver):
        driver.find_element(*Locators.ENTER_IN_ACC_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_LINK))
        driver.find_element(*Locators.REGISTRATION_LINK).click()
        register(driver, '', data.email, data.password)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REG_BTN))
        assert driver.find_element(*Locators.REG_BTN).is_displayed()

    def test_registration_empty_email(self, driver):
        driver.find_element(*Locators.ENTER_IN_ACC_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_LINK))
        driver.find_element(*Locators.REGISTRATION_LINK).click()
        register(driver, data.name, "", data.password)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REG_BTN))
        assert driver.find_element(*Locators.REG_BTN).is_displayed()

    def test_registration_pwd_not_valid(self, driver):
        driver.find_element(*Locators.ENTER_IN_ACC_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_LINK))
        driver.find_element(*Locators.REGISTRATION_LINK).click()
        register(driver, data.name, data.email, "123")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.INCORRECT_PWD_MSG))
        assert driver.find_element(*Locators.INCORRECT_PWD_MSG).is_displayed()

    def test_registration_user_exist(self, driver):
        driver.find_element(*Locators.ENTER_IN_ACC_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_LINK))
        driver.find_element(*Locators.REGISTRATION_LINK).click()
        register(driver, data.name, data.email, data.password)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.USER_EXIST))
        assert driver.find_element(*Locators.USER_EXIST).is_displayed()
