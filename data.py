WEBPAGE= 'https://stellarburgers.nomoreparties.site'

const = {
'HANDLER_REGISTRATION_USER' : ('post', WEBPAGE + '/api/auth/register/'),
'HANDLER_AUTHORIZATION_USER' : ('post', WEBPAGE + '/api/auth/login/'),
'HANDLER_DELETE_USER' : ('delete', WEBPAGE + '/api/auth/user/'),
'USER_EMAIL_PARAMETER_NAME' : 'email',
'USER_PASSWORD_PARAMETER_NAME' : 'password',
'USER_NAME_PARAMETER_NAME' : 'name',
'USER_ACCESS_TOKEN_PARAMETER_NAME' : 'accessToken',
'USER_AUTHORIZATION_PARAMETER_NAME' : 'authorization',

}

results = {
'ALLOWED_REGISTRATION_NEW_USER_WITH_VALID_VALUES' : (200,'"success":true'),
'NOT_ALLOWED_REGISTRATION_TWO_IDENTICAL_USER' : (403,'{"success":false,"message":"User already exists"}'),
'NOT_ALLOWED_REGISTRATION_USER_WITH_OUT_OR_EMPTY_ANY_NEED_PARAMETERS' : (403,'{"success":false,"message":"Email, password and name are required fields"}'),
'ALLOWED_AUTHORIZATION_USER_WITH_VALID_VALUES' : (200,'"success":true'),
'NOT_ALLOWED_AUTHORIZATION_USER_WITH_WRONG_VALUES' : (401,'{"success":false,"message":"email or password are incorrect"}'),
}

user_registration_need_parameters =     [
const['USER_EMAIL_PARAMETER_NAME']      ,
const['USER_PASSWORD_PARAMETER_NAME']   ,
const['USER_NAME_PARAMETER_NAME']       ]

user_authorization_test_parameters =    [
const['USER_EMAIL_PARAMETER_NAME']      ,
const['USER_PASSWORD_PARAMETER_NAME']   ]

