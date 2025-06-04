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
}
