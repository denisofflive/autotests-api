import httpx

login_payload = {
    "email": "denisov@google.net",
    "password": "1234567890"
}

login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload, timeout=15)
login_response_data = login_response.json()

print('Login Response:', login_response_data)
print('Status Code:', login_response.status_code)

access_token = login_response_data.get('token', 'None').get('accessToken', 'None')
headers = {"Authorization": f"Bearer {access_token}"}
response_me = httpx.get('http://localhost:8000/api/v1/users/me', headers=headers)
response_me_data = response_me.json()

print('Response Me:', response_me_data)
print('Status Code:', response_me.status_code)
