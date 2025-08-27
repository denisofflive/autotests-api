from http import HTTPStatus

import pytest
from tools.fakers import fake
from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from fixtures.users import UserFixture  # Заменяем импорт
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_get_user_response

domains = {
    'mail.ru': 'User with mail in the domain Mail.ru',
    'gmail.com': 'User with mail in the domain Gmail.com',
    'example.com': 'User with mail in the domain Example.com',
}

@pytest.mark.users
@pytest.mark.regression
@pytest.mark.parametrize('domain', domains.keys(),
                         ids=lambda domain: f"{domain}: {domains[domain]}")
def test_create_user(domain: str, public_users_client: PublicUsersClient):
    # public_users_client = get_public_users_client()
    user_email = fake.email(domain=domain)

    request = CreateUserRequestSchema(email=user_email)
    # print(request.email)
    response = public_users_client.create_user_api(request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)


@pytest.mark.users
@pytest.mark.regression
def test_get_user_me(function_user: UserFixture, private_users_client: PrivateUsersClient):
    response = private_users_client.get_user_me_api()
    response_data = GetUserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_get_user_response(response_data, function_user.response)

    validate_json_schema(response.json(), response_data.model_json_schema())
