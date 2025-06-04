import allure

from data import WEBPAGE, const, results
from helpers import RequestTools


class TestSuit1:

    @allure.title('№ 1-1 Проверка возможности произвести регистрацию нового пользователя с валидными данными')
    @allure.description('Отправляем запрос с валидными значениями  на ручку (POST api/auth/register) регистрации пользователя, проверяем код и тело ответа')
    @allure.story("Тестовый сценарий № 1")
    @allure.link(WEBPAGE, name='Учебный сервис «Stellar Burgers» (стенд)')
    def test_allowed_registration_new_user_with_valid_values(self, random_user):
        print(random_user)
        response = RequestTools.try_to_register_new_user(user=random_user)
        print(response.text)
        RequestTools.check_response_have_content(actually_value=response,results=results['ALLOWED_REGISTRATION_NEW_USER_WITH_VALID_VALUES'])
