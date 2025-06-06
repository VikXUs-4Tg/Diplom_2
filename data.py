WEBPAGE= 'https://stellarburgers.nomoreparties.site'

const = {
'HANDLER_REGISTRATION_USER' : ('post', WEBPAGE + '/api/auth/register/'),
'HANDLER_AUTHORIZATION_USER' : ('post', WEBPAGE + '/api/auth/login/'),
'HANDLER_DELETE_USER' : ('delete', WEBPAGE + '/api/auth/user/'),
'HANDLER_CHANGE_DATA_OF_USER' : ('patch', WEBPAGE + '/api/auth/user/'),
'HANDLER_LOGOUT_USER' : ('post', WEBPAGE + '/api/auth/logout/'),
'HANDLER_GET_INGREDIENTS' : ('get', WEBPAGE + '/api/ingredients/'),
'HANDLER_MAKE_ORDER' : ('post', WEBPAGE + '/api/orders/'),
'HANDLER_GATE_ORDER_OF_USER' : ('get', WEBPAGE + '/api/orders/'),
'USER_EMAIL_PARAMETER_NAME' : 'email',
'USER_PASSWORD_PARAMETER_NAME' : 'password',
'USER_NAME_PARAMETER_NAME' : 'name',
'USER_ACCESS_TOKEN_PARAMETER_NAME' : 'accessToken',
'USER_REFRESH_TOKEN_PARAMETER_NAME' : 'refreshToken',
'USER_AUTHORIZATION_PARAMETER_NAME' : 'authorization',
'USER_TOKEN_PARAMETER_NAME' : 'token',
'ORDER_INGREDIENTS_PARAMETER_NAME' : 'ingredients',
}

results = {
'ALLOWED_REGISTRATION_NEW_USER_WITH_VALID_VALUES' : (200,'"success":true'),
'NOT_ALLOWED_REGISTRATION_TWO_IDENTICAL_USER' : (403,'{"success":false,"message":"User already exists"}'),
'NOT_ALLOWED_REGISTRATION_USER_WITH_OUT_OR_EMPTY_ANY_NEED_PARAMETERS' : (403,'{"success":false,"message":"Email, password and name are required fields"}'),
'ALLOWED_AUTHORIZATION_USER_WITH_VALID_VALUES' : (200,'"success":true'),
'NOT_ALLOWED_AUTHORIZATION_USER_WITH_WRONG_VALUES' : (401,'{"success":false,"message":"email or password are incorrect"}'),
'ALLOWED_CHANGE_DATA_OF_AUTHORIZED_USER' : (200,'"success":true'),
'NOT_ALLOWED_CHANGE_DATA_OF_NOT_AUTHORIZED_USER' : (401 ,'{"success":false,"message":"You should be authorised"}'),
'ALLOWED_MAKE_ORDER_WITH_OUT_AUTHORIZATION' : (200,'"success":true'),
'ALLOWED_MAKE_ORDER_BY_AUTHORIZED_USER' : (200,'"success":true'),
'NOT_ALLOWED_MAKE_ORDER_WITH_OUT_OR_EMPTY_LIST_OF_INGREDIENTS' : (400,'{"success":false,"message":"Ingredient ids must be provided"}'),
'NOT_ALLOWED_MAKE_ORDER_WITH_BAD_INGREDIENT_HASH' : (500,'<!DOCTYPE html>'),
'ALLOWED_TO_GET_LIST_OF_ORDERS_BY_AUTHORIZED_USER' : (200,'"success":true'),
'NOT_ALLOWED_TO_GET_LIST_OF_ORDERS_WITH_OUT_AUTHORIZATION' : (401,'{"success":false,"message":"You should be authorised"}'),
}

user_registration_need_parameters =     [
const['USER_EMAIL_PARAMETER_NAME']      ,
const['USER_PASSWORD_PARAMETER_NAME']   ,
const['USER_NAME_PARAMETER_NAME']       ]

user_authorization_test_parameters =    [
const['USER_EMAIL_PARAMETER_NAME']      ,
const['USER_PASSWORD_PARAMETER_NAME']   ]

user_change_data_test_parameters =      [
const['USER_EMAIL_PARAMETER_NAME']      ,
const['USER_PASSWORD_PARAMETER_NAME']   ,
const['USER_NAME_PARAMETER_NAME']       ]
