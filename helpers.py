import requests
import random
import string
import allure

from data import const


russian_letters = ''.join([chr(i) for i in range(1040, 1104)])

class RequestTools:

    @staticmethod
    @allure.step("Отправляем запрос на ручку")
    def send_request(handler, headers = None, params = None, data = None, tail=None):
        method, endpoint = handler
        if tail:
            response = getattr(requests, method)(endpoint + str(tail), headers=headers, params=params, data=data)
        else:
            response = getattr(requests, method)(endpoint, headers=headers, params=params, data=data)
        return response

    @staticmethod
    @allure.step("Пытаемся зарегистрировать пользователя")
    def try_to_register_new_user(user):
        response = RequestTools.send_request(handler=const['HANDLER_REGISTRATION_USER'], data=user)
        return response

    @staticmethod
    @allure.step("Проверяем ответ на соответствие ожидаемому значению: {results}")
    def check_response(actually_value, results):
        expected_value_code, expected_value_text = results
        assert actually_value.status_code == expected_value_code, f'\nОжидаемое значение:\n"{expected_value_code}"\nФактическое значение:\n"{actually_value.status_code}"'
        assert actually_value.text == expected_value_text, f'\nОжидаемое значение:\n"{expected_value_text}"\nФактическое значение:\n"{actually_value.text}"'

    @staticmethod
    @allure.step("Проверяем ответ на соответствие ожидаемому значению: {results}")
    def check_response_have_content(actually_value, results):
        expected_value_code, expected_value_text = results
        assert actually_value.status_code == expected_value_code, f'\nОжидаемое значение:\n"{expected_value_code}"\nФактическое значение:\n"{actually_value.status_code}"'
        assert expected_value_text in actually_value.text, f'\nОжидаемое значение содержит:\n"{expected_value_text}"\nФактическое значение:\n"{actually_value.text}"'

class Generators:

    @staticmethod
    def generate_random_email():
        login_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(3, 10)))
        email_name = ''.join(random.choices(string.ascii_lowercase, k=random.randint(2, 10)))
        email_domain = ''.join(random.choices(string.ascii_lowercase, k=2))
        return f"{login_name}@{email_name}.{email_domain}"

    @staticmethod
    def generate_random_name():
        allowed_chars = string.ascii_lowercase + string.digits
        random_name = ''.join(random.choices(allowed_chars, k=random.randint(2, 10)))
        return random_name

    @staticmethod
    def generate_random_password():
        allowed_chars = string.digits
        random_password = ''.join(random.choices(allowed_chars, k=4))
        return random_password
