import requests
import random
import string
import allure
import copy

from data import const


russian_letters = ''.join([chr(i) for i in range(1040, 1104)])

class Tools:

    @staticmethod
    def make_clone(test_data):
        return copy.deepcopy(test_data)

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
    @allure.step("Пытаемся авторизоваться под пользователем")
    def try_user_authorization(user):
        response = RequestTools.send_request(handler=const['HANDLER_AUTHORIZATION_USER'], data=user)
        allure.attach(  body=f"Код ответа: {response.status_code}\nТело ответа:\n{response.text}".encode(),
                        name="Ответ на попытку авторизоваться под пользователем",
                        attachment_type=allure.attachment_type.TEXT, extension=".txt")
        return response

    @staticmethod
    @allure.step("Пытаемся получить токен авторизации пользователя")
    def try_to_get_user_tokens(user):
        response = RequestTools.try_user_authorization(user=user)
        access_token = response.json()[const['USER_ACCESS_TOKEN_PARAMETER_NAME']]
        refresh_token = response.json()[const['USER_REFRESH_TOKEN_PARAMETER_NAME']]
        return [{const['USER_AUTHORIZATION_PARAMETER_NAME']: access_token}, {const['USER_TOKEN_PARAMETER_NAME']: refresh_token}]

    @staticmethod
    @allure.step("Пытаемся удалить пользователя")
    def try_to_delete_user(user_access_token):
        response = RequestTools.send_request(handler=const['HANDLER_DELETE_USER'], headers=user_access_token)
        allure.attach(  body=f"Код ответа: {response.status_code}\nТело ответа:\n{response.text}".encode(),
                        name="Ответ на попытку удалить пользователя",
                        attachment_type=allure.attachment_type.TEXT, extension=".txt")
        return response

    @staticmethod
    @allure.step("Пытаемся изменить данные пользователя")
    def try_to_change_data_of_user(user_access_token, new_data):
        response = RequestTools.send_request(handler=const['HANDLER_CHANGE_DATA_OF_USER'], headers=user_access_token, data=new_data)
        allure.attach(  body=f"Код ответа: {response.status_code}\nТело ответа:\n{response.text}".encode(),
                        name="Ответ на попытку изменить данные пользователя",
                        attachment_type=allure.attachment_type.TEXT, extension=".txt")
        return response

    @staticmethod
    @allure.step("Пытаемся выйти из сессии пользователя")
    def try_to_logout_user(refresh_token):
        response = RequestTools.send_request(handler=const['HANDLER_LOGOUT_USER'], data=refresh_token)
        allure.attach(  body=f"Код ответа: {response.status_code}\nТело ответа:\n{response.text}".encode(),
                        name="Ответ на попытку выйти из сессии пользователя",
                        attachment_type=allure.attachment_type.TEXT, extension=".txt")
        return response

    @staticmethod
    @allure.step("Пытаемся получить список ингредиентов")
    def try_to_get_ingredients():
        response = RequestTools.send_request(handler=const['HANDLER_GET_INGREDIENTS'])
        allure.attach(  body=f"Код ответа: {response.status_code}\nТело ответа:\n{response.text}".encode(),
                        name="Ответ на попытку получить список ингредиентов",
                        attachment_type=allure.attachment_type.TEXT, extension=".txt")
        return response

    @staticmethod
    @allure.step("Пытаемся создать заказ")
    def try_to_make_order(ingredients):
        response = RequestTools.send_request(handler=const['HANDLER_MAKE_ORDER'], data=ingredients)
        allure.attach(  body=f"Код ответа: {response.status_code}\nТело ответа:\n{response.text}".encode(),
                        name="Ответ на попытку создать заказ",
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
            RequestTools.try_to_delete_user(user_access_token={const['USER_AUTHORIZATION_PARAMETER_NAME']: token})
            allure.attach(  body=f"Удален пользователь с именем {user[const['USER_NAME_PARAMETER_NAME']]} (email: {user[const['USER_EMAIL_PARAMETER_NAME']]})".encode(),
                            name="Успешное удаление созданного пользователя",
                            attachment_type=allure.attachment_type.TEXT, extension=".txt")
        else:
            allure.attach(  body=f"Авторизоваться под пользователем не удалось".encode(),
                            name="Ошибка удаления пользователя",
                            attachment_type=allure.attachment_type.TEXT, extension=".txt")

class Generators:

    @staticmethod
    def generate_random_email():
        login_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(3, 10)))
        email_name = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        email_domain = ''.join(random.choices(string.ascii_lowercase, k=2))
        return f"{login_name}@{email_name}.{email_domain}"

    @staticmethod
    def generate_random_name():
        allowed_chars = string.ascii_lowercase + string.digits
        random_name = ''.join(random.choices(allowed_chars, k=random.randint(3, 10)))
        return random_name

    @staticmethod
    def generate_random_password():
        allowed_chars = string.digits
        random_password = ''.join(random.choices(allowed_chars, k=4))
        return random_password

    @staticmethod
    def change_last_two_chars(input_string):
        allowed_chars = string.ascii_lowercase
        modified_string = input_string[:-2] + ''.join(random.choices(allowed_chars, k=2))
        return modified_string

    @staticmethod
    def generate_random_burger(number_of_main=None, number_of_sauce=None):
        print()
        response = RequestTools.try_to_get_ingredients().json()["data"]
        list_of_bun = []
        list_of_main = []
        list_of_sauce = []
        for element in response:
            match element['type']:
                case "bun": list_of_bun.append(element["_id"])
                case "main": list_of_main.append(element["_id"])
                case "sauce": list_of_sauce.append(element["_id"])
        random_bun = random.choice(list_of_bun)

        if number_of_main: random_main = random.sample(population=list_of_main, k=number_of_main)
        else: random_main = None

        if number_of_sauce: random_sauce = random.sample(population=list_of_sauce, k=number_of_sauce)
        else: random_sauce = None

        print(f"Случайный bun: {random_bun}")
        print(f"Случайные main: {random_main}")
        print(f"Случайные sauce: {random_sauce}")

        return random_bun, random_main, random_sauce