import allure
import pytest

from data import WEBPAGE, results, user_change_data_test_parameters
from helpers import RequestTools, Generators, Tools


class TestSuit3:

    @pytest.mark.parametrize('parameter', user_change_data_test_parameters)
    @allure.title('№ 3-1 Проверка возможности изменить значение параметра "{parameter}" авторизованного пользователя')
    @allure.description('Создаем нового пользователя, авторизуемся за созданного пользователя, отправляем запрос на изменение значения параметра созданного пользователя на ручку (PATCH api/auth/user) изменения значений параметров пользователя, проверяем код и тело ответа')
    @allure.story("Тестовый сценарий № 3")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_allowed_change_data_of_authorized_user(self, random_user, parameter):
        RequestTools.try_to_register_new_user(user=random_user)
        authorization_token = RequestTools.try_to_get_user_tokens(user=random_user)[0]
        random_user[parameter] = Generators.change_last_two_chars(random_user[parameter])
        response = RequestTools.try_to_change_data_of_user(user_access_token=authorization_token,new_data=random_user)
        RequestTools.check_response_have_content(actually_value=response,results=results['ALLOWED_CHANGE_DATA_OF_AUTHORIZED_USER'])

    @allure.title('№ 3-2 Проверка изменения значения параметра "password" авторизованного пользователя')
    @allure.description('Создаем нового пользователя, авторизуемся за созданного пользователя, изменяем значения параметра "password" созданного пользователя, отправляем запрос на ручку (POST api/auth/login) авторизации пользователя, проверяем код и тело ответа')
    @allure.story("Тестовый сценарий № 3")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_check_of_changing_password_of_authorized_user(self, random_user):
        RequestTools.try_to_register_new_user(user=random_user)
        authorization_token = RequestTools.try_to_get_user_tokens(user=random_user)[0]
        random_user[user_change_data_test_parameters[1]] = Generators.change_last_two_chars(random_user[user_change_data_test_parameters[1]])
        RequestTools.try_to_change_data_of_user(user_access_token=authorization_token, new_data=random_user)
        response = RequestTools.try_user_authorization(user=random_user)
        RequestTools.check_response_have_content(actually_value=response, results=results['ALLOWED_AUTHORIZATION_USER_WITH_VALID_VALUES'])

    @allure.title('№ 3-3 Проверка изменения значения параметра "email" авторизованного пользователя')
    @allure.description('Создаем нового пользователя, авторизуемся за созданного пользователя, изменяем значения параметра "email" созданного пользователя, отправляем запрос на ручку (POST api/auth/login) авторизации пользователя, проверяем код и тело ответа')
    @allure.story("Тестовый сценарий № 3")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_check_of_changing_email_of_authorized_user(self, random_user):
        RequestTools.try_to_register_new_user(user=random_user)
        authorization_token = RequestTools.try_to_get_user_tokens(user=random_user)[0]
        random_user[user_change_data_test_parameters[0]] = Generators.change_last_two_chars(random_user[user_change_data_test_parameters[0]])
        RequestTools.try_to_change_data_of_user(user_access_token=authorization_token, new_data=random_user)
        response = RequestTools.try_user_authorization(user=random_user)
        RequestTools.check_response_have_content(actually_value=response,results=(results['ALLOWED_AUTHORIZATION_USER_WITH_VALID_VALUES'][0], random_user[user_change_data_test_parameters[0]]))

    @allure.title('№ 3-4 Проверка изменения значения параметра "name" авторизованного пользователя')
    @allure.description('Создаем нового пользователя, авторизуемся за созданного пользователя, изменяем значения параметра "name" созданного пользователя, отправляем запрос на ручку (POST api/auth/login) авторизации пользователя, проверяем код и тело ответа')
    @allure.story("Тестовый сценарий № 3")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_check_of_changing_name_of_authorized_user(self, random_user):
        RequestTools.try_to_register_new_user(user=random_user)
        authorization_token = RequestTools.try_to_get_user_tokens(user=random_user)[0]
        random_user[user_change_data_test_parameters[2]] = Generators.change_last_two_chars(random_user[user_change_data_test_parameters[2]])
        RequestTools.try_to_change_data_of_user(user_access_token=authorization_token, new_data=random_user)
        response = RequestTools.try_user_authorization(user=random_user)
        RequestTools.check_response_have_content(actually_value=response, results=(results['ALLOWED_AUTHORIZATION_USER_WITH_VALID_VALUES'][0], random_user[user_change_data_test_parameters[2]]))

    @allure.title('№ 3-5 Проверка не возможности изменить значение параметра "{parameter}" не авторизованного пользователя')
    @allure.description('Создаем нового пользователя, отправляем запрос на изменение значения параметра созданного пользователя без токена авторизации на ручку (PATCH api/auth/user) изменения значений параметров пользователя, проверяем код и тело ответа')
    @allure.story("Тестовый сценарий № 3")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_not_allowed_change_data_of_not_authorized_user(self, random_user):
        RequestTools.try_to_register_new_user(user=random_user)
        response = RequestTools.try_to_change_data_of_user(user_access_token=None,new_data=random_user)
        RequestTools.check_response_have_content(actually_value=response,results=results['NOT_ALLOWED_CHANGE_DATA_OF_NOT_AUTHORIZED_USER'])

    @pytest.mark.parametrize('parameter', user_change_data_test_parameters)
    @allure.title('№ 3-6 Проверка возможности изменить значение параметра "{parameter}" пользователя после выхода из сессии')
    @allure.description('Создаем нового пользователя, авторизуемся за созданного пользователя, осуществляем выход из сессии созданным пользователем, отправляем запрос на изменение значения параметра созданного пользователя на ручку (PATCH api/auth/user) изменения значений параметров пользователя, проверяем код и тело ответа')
    @allure.story("Тестовый сценарий № 3")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_allowed_change_data_after_user_quit(self, random_user, parameter):
        RequestTools.try_to_register_new_user(user=random_user)
        another_user = Tools.make_clone(random_user)
        tokens = RequestTools.try_to_get_user_tokens(user=another_user)
        RequestTools.try_to_logout_user(refresh_token=tokens[1])
        another_user[parameter] = Generators.change_last_two_chars(another_user[parameter])
        response = RequestTools.try_to_change_data_of_user(user_access_token=tokens[0],new_data=another_user)
        RequestTools.check_response_have_content(actually_value=response,results=results['ALLOWED_CHANGE_DATA_OF_AUTHORIZED_USER'])


