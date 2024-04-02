import time
from pages.form_signup_page import FillSignUpPage


class TestFormPage:
    def test_signup_form(self, driver):
        signin_page = FillSignUpPage(driver, "https://homerecipes.sytes.net/signup")
        signin_page.open()
        signin_page.fill_signup_fields_and_create_account()
        time.sleep(30)
        # form_page = FormPage(driver, "https://demoqa.com/automation-practice-form")
        # form_page.open()
        #     # first_name, last_name, email = form_page.fill_fields_and_submit()
        #     # result = form_page.form_result()
        #     # print(first_name, last_name, email)
        #     # print(result)
        #     # assert f'{first_name} {last_name}' == result[0], 'The form has not been filled'
        #     # assert email == result[1], 'The form has not been filled'
        # person = form_page.fill_fields_and_submit()
        # result = form_page.form_result()
        # print(person)
        # print(result)
        # assert f'{person.first_name} {person.last_name}' == result[0], 'The form has not been filled'
        # assert person.email == result[1], 'The form has not been filled'
