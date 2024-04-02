import time

from selenium.webdriver import Keys
from pages.base_page import BasePage
from locators.form_signup_locators import FormSignUpLocators as Locators

from generator.generator import generated_file, generator_person


class FillSignUpPage(BasePage):
    def fill_signup_fields_and_create_account(self):
        person = generator_person()
        # path = generated_file()
        self.element_is_visible(Locators.FIRST_NAME).send_keys(person.first_name)
        self.element_is_visible(Locators.LAST_NAME).send_keys(person.last_name)
        self.element_is_visible(Locators.NICKNAME).send_keys(person.nickname)
        self.element_is_visible(Locators.EMAIL).send_keys(person.email)
        self.element_is_visible(Locators.PASSWORD).send_keys(person.password)
        self.element_is_visible(Locators.CREATEACCOUNT).click()
        # first_name = 'Hello'
        # last_name = "World"
        # email = "fobos_media@mail.ru"
    #     person = generator_person()
    #     path = generated_file()
    #     # удаление футера
    #     self.remove_footer()
    #     self.element_is_visible(Locators.FIRST_NAME).send_keys(person.first_name)
    #     self.element_is_visible(Locators.LAST_NAME).send_keys(person.last_name)
    #     self.element_is_visible(Locators.EMAIL).send_keys(person.email)
    #     self.element_is_visible(Locators.GENDER).click()
    #     self.element_is_visible(Locators.MOBILE).send_keys(person.mobile)
    #     subject = self.element_is_visible(Locators.SUBJECT)
    #     subject.send_keys('English')
    #     subject.send_keys(Keys.RETURN)
    #     self.element_is_visible(Locators.HOBBIES).click()
    #     self.element_is_visible(Locators.FILE_INPUT).send_keys(path)
    #     self.element_is_visible(Locators.CURRENT_ADDRESS).send_keys(person.current_address)
    #     self.element_is_visible(Locators.SUBMIT).click()
    #     return person
    #
    # def form_result(self):
    #     result_list = self.elements_are_visible(Locators.RESULT_TABLE)
    #     result_text = [i.text for i in result_list]
    #     return result_text
