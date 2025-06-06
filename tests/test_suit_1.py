import allure
import pytest

from data import WEBPAGE, results, user_registration_need_parameters
from helpers import RequestTools


class TestSuit1:

    @allure.title('№ 1-1 Проверка возможности произвести регистрацию нового пользователя с валидными данными')
    @allure.description('Отправляем запрос с валидными значениями на ручку (POST api/auth/register) регистрации пользователя, проверяем код и тело ответа')
    @allure.story("Тестовый сценарий № 1")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_allowed_registration_new_user_with_valid_values(self, random_user):
        response = RequestTools.try_to_register_new_user(user=random_user)
        RequestTools.check_response_have_content(actually_value=response,results=results['ALLOWED_REGISTRATION_NEW_USER_WITH_VALID_VALUES'])

    @allure.title('№ 1-2 Проверка невозможность произвести регистрацию уже созданного пользователя повторно')
    @allure.description('Отправляем дважды последовательно запросы на регистрацию одного и того же пользователя на ручку (POST api/auth/register) регистрации пользователя, проверяем код и тело ответа')
    @allure.story("Тестовый сценарий № 1")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_not_allowed_registration_two_identical_user(self, random_user):
        RequestTools.try_to_register_new_user(user=random_user)
        response = RequestTools.try_to_register_new_user(user=random_user)
        RequestTools.check_response(actually_value=response,results=results['NOT_ALLOWED_REGISTRATION_TWO_IDENTICAL_USER'])

    @pytest.mark.parametrize('parameter', user_registration_need_parameters)
    @allure.title('№ 1-3 Проверка невозможность произвести регистрацию нового пользователя без указания обязательного параметра "{parameter}"')
    @allure.description('Отправляем запрос на ручку (POST api/auth/register) регистрации пользователя без указания обязательного параметра, проверяем код и тело ответа')
    @allure.story("Тестовый сценарий № 1")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_not_allowed_registration_with_out_any_need_parameters(self, random_user, parameter):
        del random_user[parameter]
        response = RequestTools.try_to_register_new_user(user=random_user)
        RequestTools.check_response(actually_value=response,results=results['NOT_ALLOWED_REGISTRATION_USER_WITH_OUT_OR_EMPTY_ANY_NEED_PARAMETERS'])

    @pytest.mark.parametrize('parameter', user_registration_need_parameters)
    @allure.title('№ 1-4 Проверка невозможность произвести регистрацию нового пользователя при указании пустого значения обязательного параметра "{parameter}"')
    @allure.description('Отправляем запрос на ручку (POST api/auth/register) регистрации пользователя c пустым значением обязательного параметра, проверяем код и тело ответа')
    @allure.story("Тестовый сценарий № 1")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_not_allowed_registration_with_empty_any_need_parameters(self, random_user, parameter):
        random_user[parameter] = ""
        response = RequestTools.try_to_register_new_user(user=random_user)
        RequestTools.check_response(actually_value=response,results=results['NOT_ALLOWED_REGISTRATION_USER_WITH_OUT_OR_EMPTY_ANY_NEED_PARAMETERS'])
