## Дипломный проект. Задание 2: API

<hr>

## Студент: Федоров Кирилл Сергеевич

## <h>Когорта: №19</h>

<hr>

### Автотесты для тестирования ручек API сервиса Stellar Burgers.

### Реализованные сценарии

Созданы API-тесты, покрывающие следующие ручки: <br />
POST api/auth/register - создание пользователя <br />
POST api/auth/login - логин пользователя <br />
PATCH api/auth/user - изменения данных пользователя <br />
POST api/orders - создание заказа <br />
GET api/orders - получение заказов конкретного пользователя <br />
Всего: 33 теста <br /> <br />
Создан отчет в Allure, прилагаемый к тестам

### Структура проекта

- `tests` - пакет, содержащий тесты, разделенные по наборам.
- `allure_results` - каталог, содержащий отчет в Allure.

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Сгенерировать отчеты в Allure**

> `$ pytest tests/. --alluredir=allure_results`

**Посмотреть результаты тестирования в Allure**

> `$ allure serve allure_results`

<hr>

### Ссылки:

#### Ссылка на Pull-request:

#### Тестовый стенд: https://stellarburgers.nomoreparties.site/

#### Ссылка на документацию API: https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/api-documentation.pdf?etag=3403196b527ca03259bfd0cb41163a89