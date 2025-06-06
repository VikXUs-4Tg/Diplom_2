import allure

from data import WEBPAGE, results, const
from helpers import RequestTools, Generators


class TestSuit5:

    @allure.title('№ 5-1 Проверка возможности получения списка сделанных пользователем заказов')
    @allure.description('Регистрируем нового пользователя и авторизуемся им, не делая заказов - отправляем запрос на ручку (GET api/orders) просмотра созданных заказов, проверяем код и тело ответа')
    @allure.story("Тестовый сценарий № 5")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_allowed_to_get_list_of_orders_by_authorized_user_with_out_orders(self, random_user):
        RequestTools.try_to_register_new_user(user=random_user)
        access_token = RequestTools.try_to_get_user_tokens(user=random_user)[0]
        response = RequestTools.try_to_get_orders_list(user_access_token=access_token)
        RequestTools.check_response_have_content(actually_value=response,results=results['ALLOWED_TO_GET_LIST_OF_ORDERS_BY_AUTHORIZED_USER'])

    @allure.title('№ 5-2 Проверка возможности получения в списке сделанных пользователем заказов ингредиента из сделанного ранее заказа')
    @allure.description('Регистрируем нового пользователя и авторизуемся им, делаем валидный заказ созданным пользователем, отправляем запрос на ручку (GET api/orders) просмотра созданных заказов, проверяем код и тело ответа')
    @allure.story("Тестовый сценарий № 5")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_allowed_to_get_list_of_orders_by_authorized_user_with_one_order(self, random_user):
        RequestTools.try_to_register_new_user(user=random_user)
        access_token = RequestTools.try_to_get_user_tokens(user=random_user)[0]
        random_burger = Generators.generate_random_burger()
        RequestTools.try_to_make_order(user_access_token=access_token,list_of_ingredients=random_burger)
        response = RequestTools.try_to_get_orders_list(user_access_token=access_token)
        RequestTools.check_response_have_content(actually_value=response, results=(results['ALLOWED_TO_GET_LIST_OF_ORDERS_BY_AUTHORIZED_USER'][0], random_burger[const['ORDER_INGREDIENTS_PARAMETER_NAME']][0]))

    @allure.title('№ 5-3 Проверка невозможности получения списка сделанных пользователем заказов, если пользователь не авторизован')
    @allure.description('Отправляем запрос без токена авторизации на ручку (GET api/orders) просмотра созданных заказов, проверяем код и тело ответа')
    @allure.story("Тестовый сценарий № 5")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_not_allowed_to_get_list_of_orders_with_out_authorization(self):
        response = RequestTools.try_to_get_orders_list(user_access_token=None)
        RequestTools.check_response(actually_value=response,results=results['NOT_ALLOWED_TO_GET_LIST_OF_ORDERS_WITH_OUT_AUTHORIZATION'])
