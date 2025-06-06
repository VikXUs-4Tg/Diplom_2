import allure

from data import WEBPAGE, results, const
from helpers import RequestTools, Generators


class TestSuit4:

    @allure.title('№ 4-1 Проверка возможности сделать валидный заказ не авторизованным пользователем')
    @allure.description('Создаем случайный бургер из случайного количества валидных ингредиентов, отправляем запрос на ручку (POST api/orders) создания заказов, проверяем код и тело ответа')
    @allure.story("Тестовый сценарий № 4")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_allowed_make_order_with_out_authorization(self):
        random_burger = Generators.generate_random_burger()
        response = RequestTools.try_to_make_order(user_access_token=None,list_of_ingredients=random_burger)
        RequestTools.check_response_have_content(actually_value=response,results=results['ALLOWED_MAKE_ORDER_WITH_OUT_AUTHORIZATION'])

    @allure.title('№ 4-2 Проверка возможности сделать валидный заказ авторизованным пользователем')
    @allure.description('Регистрируем нового пользователя и авторизуемся им, создаем случайный бургер из случайного количества валидных ингредиентов, отправляем запрос на ручку (POST api/orders) создания заказов с указанием токена доступа созданного пользователя, проверяем код и тело ответа')
    @allure.story("Тестовый сценарий № 4")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_allowed_make_order_by_authorized_user(self, random_user):
        RequestTools.try_to_register_new_user(user=random_user)
        access_token = RequestTools.try_to_get_user_tokens(user=random_user)[0]
        random_burger = Generators.generate_random_burger()
        response = RequestTools.try_to_make_order(user_access_token=access_token,list_of_ingredients=random_burger)
        RequestTools.check_response_have_content(actually_value=response,results=results['ALLOWED_MAKE_ORDER_BY_AUTHORIZED_USER'])

    @allure.title('№ 4-3 Проверка верного указания в теле заказа параметра "name" авторизованного пользователя, создавшего заказ')
    @allure.description('Регистрируем нового пользователя и авторизуемся им, создаем случайный бургер из случайного количества валидных ингредиентов, отправляем запрос на ручку (POST api/orders) создания заказов с указанием токена доступа созданного пользователя, проверяем код и тело ответа на соответствие параметра "owner - name"')
    @allure.story("Тестовый сценарий № 4")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_check_user_name_of_created_order_with_authorization(self, random_user):
        RequestTools.try_to_register_new_user(user=random_user)
        access_token = RequestTools.try_to_get_user_tokens(user=random_user)[0]
        random_burger = Generators.generate_random_burger()
        response = RequestTools.try_to_make_order(user_access_token=access_token, list_of_ingredients=random_burger)
        RequestTools.check_response_have_content(actually_value=response, results=(results['ALLOWED_MAKE_ORDER_BY_AUTHORIZED_USER'][0],random_user[const['USER_NAME_PARAMETER_NAME']]))

    @allure.title('№ 4-4 Проверка верного указания в теле заказа параметра "email" авторизованного пользователя, создавшего заказ')
    @allure.description('Регистрируем нового пользователя и авторизуемся им, создаем случайный бургер из случайного количества валидных ингредиентов, отправляем запрос на ручку (POST api/orders) создания заказов с указанием токена доступа созданного пользователя, проверяем код и тело ответа на соответствие параметра "owner - email"')
    @allure.story("Тестовый сценарий № 4")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_check_user_email_of_created_order_with_authorization(self, random_user):
        RequestTools.try_to_register_new_user(user=random_user)
        access_token = RequestTools.try_to_get_user_tokens(user=random_user)[0]
        random_burger = Generators.generate_random_burger()
        response = RequestTools.try_to_make_order(user_access_token=access_token, list_of_ingredients=random_burger)
        RequestTools.check_response_have_content(actually_value=response, results=(results['ALLOWED_MAKE_ORDER_BY_AUTHORIZED_USER'][0], random_user[const['USER_EMAIL_PARAMETER_NAME']]))

    @allure.title('№ 4-5 Проверка не возможности сделать заказ без указания списка ингредиентов в теле запроса не авторизованным пользователем')
    @allure.description('Отправляем запрос без указания ингредиентов в теле запроса на ручку (POST api/orders) создания заказов, проверяем код и тело ответа')
    @allure.story("Тестовый сценарий № 4")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_not_allowed_make_order_with_out_list_of_ingredients(self):
        response = RequestTools.try_to_make_order(user_access_token=None, list_of_ingredients=None)
        RequestTools.check_response(actually_value=response, results=results['NOT_ALLOWED_MAKE_ORDER_WITH_OUT_OR_EMPTY_LIST_OF_INGREDIENTS'])

    @allure.title('№ 4-6 Проверка не возможности сделать заказ указав пустой список ингредиентов в теле запроса не авторизованным пользователем')
    @allure.description('Отправляем запрос указав пустой список ингредиентов в теле запроса на ручку (POST api/orders) создания заказов, проверяем код и тело ответа')
    @allure.story("Тестовый сценарий № 4")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_not_allowed_make_order_with_empty_list_of_ingredients(self):
        empty_list_of_ingredients = {const['ORDER_INGREDIENTS_PARAMETER_NAME']: []}
        response = RequestTools.try_to_make_order(user_access_token=None, list_of_ingredients=empty_list_of_ingredients)
        RequestTools.check_response(actually_value=response, results=results['NOT_ALLOWED_MAKE_ORDER_WITH_OUT_OR_EMPTY_LIST_OF_INGREDIENTS'])

    @allure.title('№ 4-7 Проверка не возможности сделать заказ указав неверный хеш ингредиента не авторизованным пользователем')
    @allure.description('Отправляем запрос без указания ингредиентов в теле на ручку (POST api/orders) создания заказов, проверяем код и тело ответа')
    @allure.story("Тестовый сценарий № 4")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_not_allowed_make_order_with_bad_ingredient_hash(self):
        empty_list_of_ingredients = {const['ORDER_INGREDIENTS_PARAMETER_NAME']: ['0']}
        response = RequestTools.try_to_make_order(user_access_token=None, list_of_ingredients=empty_list_of_ingredients)
        RequestTools.check_response_have_content(actually_value=response, results=results['NOT_ALLOWED_MAKE_ORDER_WITH_BAD_INGREDIENT_HASH'])
