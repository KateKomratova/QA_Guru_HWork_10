import os

import command
from selene import browser, have


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def fill_gender(self):
        browser.element('[for=gender-radio-2]').click()

    def fill_phone(self, number):
        browser.element('#userNumber').type(number)

    def fill_date_of_birth(self, year, month, day):
        # Выбираем дату рождения в календаре
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.all('.react-datepicker__month-select option').element_by(have.exact_text(month)).click()
        browser.element('.react-datepicker__year-select').click()
        browser.all('.react-datepicker__year-select option').element_by(have.value(year)).click()
        browser.all('.react-datepicker__day').element_by(have.exact_text(day)).click()

    def fill_subjects(self,value):
        browser.element('#subjectsInput').type(value).press_enter()

    def fill_hobbies(self):
        browser.element('[for=hobbies-checkbox-2]').click()

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)

    def fill_state(self,value):
        browser.element('#state').click()
        browser.element('#react-select-3-input').set_value(value).press_tab()

    def fill_city(self,value):
        browser.element('#city').click()
        browser.element('#react-select-4-input').set_value(value).press_tab()

    def upload_picture(self, file_name):
        browser.element('#uploadPicture').send_keys(os.path.abspath(file_name))

    def submit(self):
        browser.element('#submit').click()

    def should_title_form(self, value):
        browser.element('#example-modal-sizes-title-lg').should(have.exact_text(value))

    def should_registred_user_with(self, labels, full_name, email, gender, mobile, date_of_birth, subjects, hobbies, picture, address,
                                   state_and_city):
        browser.element('.table').all('tr').should(have.exact_texts(
        labels,
            full_name,
            email,
            gender,
            mobile,
            date_of_birth,
            subjects,
            hobbies,
            picture,
            address,
            state_and_city
        )
    )

    def remove_baner_footer(self):
            browser.driver.execute_script("$('#fixedban').remove()")
            browser.driver.execute_script("$('footer').remove()")
