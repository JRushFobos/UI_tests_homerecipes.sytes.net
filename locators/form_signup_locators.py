from selenium.webdriver.common.by import By
from random import randint


class FormSignUpLocators:
    FIRST_NAME = (By.CSS_SELECTOR, "input[name='first_name']")
    LAST_NAME = (By.CSS_SELECTOR, "input[name='last_name']")
    NICKNAME = (By.CSS_SELECTOR, "input[name='username']")
    EMAIL = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    CREATEACCOUNT = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")

    # HOBBIES = (By.CSS_SELECTOR, f"label[for='hobbies-checkbox-{randint(1,3)}']")
    # FILE_INPUT = (By.CSS_SELECTOR, "#uploadPicture")
    # CURRENT_ADDRESS = (By.CSS_SELECTOR, "#currentAddress")
    # SUBMIT = (By.CSS_SELECTOR, "#submit")
    # RESULT_TABLE = (By.XPATH, "//div[@class='table-responsive']//td[2]")
    # GROUP_HEADER = (By.CSS_SELECTOR, "span.group-header > div.header-wrapper > div.header-text > span.pr-1")