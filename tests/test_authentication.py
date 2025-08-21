
from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from http import HTTPStatus

from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code, assert_is_true
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response


def test_login():
    public_users_client = get_public_users_client()
    authentication_client = get_authentication_client()

    create_user_request = CreateUserRequestSchema()
    create_user_response = public_users_client.create_user_api(create_user_request)

    assert_status_code(create_user_response.status_code, HTTPStatus.OK)

    authentication_user = AuthenticationUserSchema(
        email=create_user_request.email,
        password=create_user_request.password
    )
    login_response = authentication_client.login_api(request=authentication_user)
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    assert_status_code(login_response.status_code, HTTPStatus.OK)
    assert_login_response(login_response_data)

    validate_json_schema(login_response.json(), login_response_data.model_json_schema())
