import allure

from modules.registration_page import RegistrationPage


def test_practice_form(browser_conf):
    registration_page = RegistrationPage()
    with allure.step("Открываем форму заполнения"):
        registration_page.open()

    # WHEN
    with allure.step("Заполняем поле 'Name'"):
        registration_page.fill_first_name('Oksana')
        registration_page.fill_last_name('Ivanova')
    with allure.step("Заполняем поле 'Email'"):
        registration_page.fill_email('ivanova_oksana@mail.ru')
    with allure.step("Заполняем поле 'Gender'"):
        registration_page.fill_gender()
    with allure.step("Заполняем поле 'Mobile'"):
        registration_page.fill_phone('8987456327')
    with allure.step("Заполняем поле 'Date of Birth'"):
        registration_page.fill_date_of_birth('1999','February','15')
    with allure.step("Заполняем поле 'Subjects'"):
        registration_page.fill_subjects('Physics')
    with allure.step("Заполняем поле 'Hobbies'"):
        registration_page.fill_hobbies()
    with allure.step("Добавляем изображение"):
        registration_page.upload_picture('../resources/test_image.jpg')
    with allure.step("Заполняем поле 'Current Address'"):
        registration_page.fill_address('ul. Pobednaya, d.7, kv.55')
    with allure.step("Заполняем поле 'State and City'"):
        registration_page.fill_state('Haryana')
        registration_page.fill_city('Panipat')
    with allure.step("Нажимаем на кнопку регистрации"):
        registration_page.submit()

    # THEN
    with allure.step("Проверяем, что заголовок окна содержит наименование 'Thanks for submitting the form'"):
        registration_page.should_title_form('Thanks for submitting the form')
    with allure.step("Проверяем, что форма заполнена корректно"):
        registration_page.should_registred_user_with(
        'Label Values',
        'Student Name Oksana Ivanova',
        'Student Email ivanova_oksana@mail.ru',
        'Gender Female',
        'Mobile 8987456327',
        'Date of Birth 15 February,1999',
        'Subjects Physics',
        'Hobbies Reading',
        'Picture test_image.jpg',
        'Address ul. Pobednaya, d.7, kv.55',
        'State and City Haryana Panipat'
    )

