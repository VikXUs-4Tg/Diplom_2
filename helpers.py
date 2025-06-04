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
        allure.attach(  body=f"Код ответа: {response.status_code}\nТело ответа:\n{response.text}".encode(),
                        name="Ответ на попытку регистрации пользователя",
                        attachment_type=allure.attachment_type.TEXT, extension=".txt")
        return response

    @staticmethod
    @allure.step("Пытаемся авторизироваться под пользователем")
    def try_user_authorization(user):
        response = RequestTools.send_request(handler=const['HANDLER_AUTHORIZATION_USER'], data=user)
        allure.attach(  body=f"Код ответа: {response.status_code}\nТело ответа:\n{response.text}".encode(),
                        name="Ответ на попытку авторизироваться под пользователем",
                        attachment_type=allure.attachment_type.TEXT, extension=".txt")
        return response

    @staticmethod
    @allure.step("Пытаемся удалить пользователя")
    def try_to_delete_user(user_access_token):
        response = RequestTools.send_request(handler=const['HANDLER_DELETE_USER'], headers=user_access_token)
        allure.attach(  body=f"Код ответа: {response.status_code}\nТело ответа:\n{response.text}".encode(),
                        name="Ответ на попытку удалить пользователя",
                        attachment_type=allure.attachment_type.TEXT, extension=".txt")
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

    @staticmethod
    @allure.step("Удаляем пользователя после теста")
    def delete_user_after_test(user):
        response = RequestTools.try_user_authorization(user)
        if response.status_code == 200:
            token = response.json()[const['USER_ACCESS_TOKEN_PARAMETER_NAME']]
            RequestTools.try_to_delete_user({const['USER_AUTHORIZATION_PARAMETER_NAME']: token})
            allure.attach(  body=f"Удален пользователь с именем {user[const['USER_NAME_PARAMETER_NAME']]} (email: {user[const['USER_EMAIL_PARAMETER_NAME']]})".encode(),
                            name="Успешное удаление созданного курьера",
                            attachment_type=allure.attachment_type.TEXT, extension=".txt")
        else:
            allure.attach(  body=f"Авторизоваться под пользователем не удалось".encode(),
                            name="Ошибка удаления пользователя",
                            attachment_type=allure.attachment_type.TEXT, extension=".txt")

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
