# swagger_client.AuthenticationApi

All URIs are relative to *https://mobile-api.senscritique.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_login_post**](AuthenticationApi.md#auth_login_post) | **POST** /auth/login | Perform user authentication
[**auth_request_token_get**](AuthenticationApi.md#auth_request_token_get) | **GET** /auth/request_token | Request API token


# **auth_login_post**
> AccessToken auth_login_post(body)

Perform user authentication

Authenticate a request_token with a username/password couple

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
body = swagger_client.AuthenticationRequest() # AuthenticationRequest | Authentication request parameters

try: 
    # Perform user authentication
    api_response = api_instance.auth_login_post(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthenticationApi->auth_login_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthenticationRequest**](AuthenticationRequest.md)| Authentication request parameters | 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_request_token_get**
> RequestToken auth_request_token_get(app_id)

Request API token

Get an API token, which needs to be authenticated in a further step

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
app_id = 56 # int | Should be set to 11

try: 
    # Request API token
    api_response = api_instance.auth_request_token_get(app_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthenticationApi->auth_request_token_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**| Should be set to 11 | 

### Return type

[**RequestToken**](RequestToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

