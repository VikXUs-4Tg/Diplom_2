WEBPAGE= 'https://stellarburgers.nomoreparties.site'

const = {
'HANDLER_REGISTRATION_USER' : ('post', WEBPAGE + '/api/auth/register/'),
'USER_EMAIL_PARAMETER_NAME' : 'email',
'USER_PASSWORD_PARAMETER_NAME' : 'password',
'USER_NAME_PARAMETER_NAME' : 'name',
}

results = {
'ALLOWED_REGISTRATION_NEW_USER_WITH_VALID_VALUES' : (200,'"success":true'),
}
