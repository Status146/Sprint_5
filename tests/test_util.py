from locators import Locators


def login(driver, email, password):
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PWD_INPUT).send_keys(password)
    driver.find_element(*Locators.ENTER_BTN).click()


def register(driver, name, email, password):
    driver.find_element(*Locators.REG_NAME_INPUT).send_keys(name)
    driver.find_element(*Locators.REG_EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.REG_PWD_INPUT).send_keys(password)
    driver.find_element(*Locators.REG_BTN).click()
