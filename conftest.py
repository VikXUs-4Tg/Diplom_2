import pytest

from data import const
from helpers import RequestTools, Generators


@pytest.fixture(scope='function')
def random_user():
    random_user = {
        const['USER_EMAIL_PARAMETER_NAME']: Generators.generate_random_email(),
        const['USER_PASSWORD_PARAMETER_NAME']: Generators.generate_random_password(),
        const['USER_NAME_PARAMETER_NAME']: Generators.generate_random_name()
    }
    yield random_user
    RequestTools.delete_user_after_test(random_user)
