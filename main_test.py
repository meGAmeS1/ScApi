import requests
import hmac
import hashlib
import json
import settings


# A little function to pretty print JSON
def pp_json(data):
    print json.dumps(data, indent=4, sort_keys=True)


token_response = requests.get(settings.HOST + '/auth/request_token', params={'app_id': 11})

if token_response.status_code != 200:
    exit(1)

print token_response.content
token = token_response.json().get('request_token')

password_md5 = hashlib.md5(settings.PASSWORD).hexdigest()
nonce = hmac.new(str(token.get('token')), settings.LOGIN + password_md5, hashlib.md5).hexdigest()

login_response = requests.post(settings.HOST + '/auth/login', data={'nonce': nonce,
                                                                    'email': settings.LOGIN,
                                                                    'pass': settings.PASSWORD,
                                                                    'token_id': str(token.get('id'))})
if login_response.status_code != 200:
    exit(1)

login_data = login_response.json()

access_token = str(login_data.get('access_token'))
# search_response = requests.get(host + '/search', params={'access_token': access_token, 'query': 'interstellar'})
# pp_json(search_response.json())

user_response = requests.get(settings.HOST + '/users/me', params={'access_token': access_token})
pp_json(user_response.json())
