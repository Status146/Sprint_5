from conftest import driver
from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructor:
    def test_sauces_conversion(self, driver):
        driver.find_element(*Locators.SAUCES_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.SAUCES_SECTION))
        assert driver.find_element(*Locators.SAUCES_SECTION).is_displayed()

    def test_filling_conversion(self, driver):
        driver.find_element(*Locators.FILLINGS_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.FILLINGS_SECTION))
        assert driver.find_element(*Locators.FILLINGS_SECTION).is_displayed()

    def test_buns_conversion_from_filling(self, driver):
        driver.find_element(*Locators.FILLINGS_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.FILLINGS_SECTION))
        driver.find_element(*Locators.BUNS_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BUNS_SECTION))
        assert driver.find_element(*Locators.BUNS_SECTION).is_displayed()
