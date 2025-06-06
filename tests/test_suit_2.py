import allure
import pytest

from data import WEBPAGE, results, user_authorization_test_parameters
from helpers import RequestTools, Generators, Tools


class TestSuit2:

    @allure.title('№ 2-1 Проверка возможности произвести авторизацию с валидными данными существующего пользователя')
    @allure.description('Создаем нового пользователя, отправляем запрос с реквизитами доступа созданного пользователя на ручку (POST api/auth/login) авторизации пользователя, проверяем код и тело ответа')
    @allure.story("Тестовый сценарий № 2")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_allowed_authorization_user_with_valid_values(self, random_user):
        RequestTools.try_to_register_new_user(user=random_user)
        response = RequestTools.try_user_authorization(user=random_user)
        RequestTools.check_response_have_content(actually_value=response,results=results['ALLOWED_AUTHORIZATION_USER_WITH_VALID_VALUES'])

    @pytest.mark.parametrize('parameter', user_authorization_test_parameters)
    @allure.title('№ 2-2 Проверка невозможности произвести авторизацию существующего пользователя, если указать неверное значение параметра "{parameter}"')
    @allure.description('Создаем нового пользователя, отправляем запрос c неверным значением параметра созданного пользователя на ручку (POST api/auth/login) авторизации пользователя, проверяем код и тело ответа')
    @allure.story("Тестовый сценарий № 2")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_not_allowed_authorization_user_with_wrong_values(self, random_user, parameter):
        RequestTools.try_to_register_new_user(user=random_user)
        another_user = Tools.make_clone(random_user)
        another_user[parameter] = Generators.change_last_two_chars(another_user[parameter])
        response = RequestTools.try_user_authorization(user=another_user)
        RequestTools.check_response(actually_value=response,results=results['NOT_ALLOWED_AUTHORIZATION_USER_WITH_WRONG_VALUES'])

    @pytest.mark.parametrize('parameter', user_authorization_test_parameters)
    @allure.title('№ 2-3 Проверка невозможности произвести авторизацию существующего пользователя, если не указать параметр "{parameter}"')
    @allure.description('Создаем нового пользователя, отправляем запрос без указания параметра созданного пользователя на ручку (POST api/auth/login) авторизации пользователя, проверяем код и тело ответа')
    @allure.story("Тестовый сценарий № 2")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_not_allowed_authorization_user_with_empty_values(self, random_user, parameter):
        RequestTools.try_to_register_new_user(user=random_user)
        another_user = Tools.make_clone(random_user)
        del another_user[parameter]
        response = RequestTools.try_user_authorization(user=another_user)
        RequestTools.check_response(actually_value=response,results=results['NOT_ALLOWED_AUTHORIZATION_USER_WITH_WRONG_VALUES'])


