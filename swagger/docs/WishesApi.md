# swagger_client.WishesApi

All URIs are relative to *https://mobile-api.senscritique.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_user_id_products_wish_get**](WishesApi.md#users_user_id_products_wish_get) | **GET** /users/{user_id}/products/wish | User wishes


# **users_user_id_products_wish_get**
> PaginatedProductList users_user_id_products_wish_get(user_id, access_token)

User wishes

Returns the list of the wishes for a given user

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WishesApi()
user_id = 'user_id_example' # str | User id (use 'me' for logged in user)
access_token = 'access_token_example' # str | Authenticated token

try: 
    # User wishes
    api_response = api_instance.users_user_id_products_wish_get(user_id, access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WishesApi->users_user_id_products_wish_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User id (use &#39;me&#39; for logged in user) | 
 **access_token** | **str**| Authenticated token | 

### Return type

[**PaginatedProductList**](PaginatedProductList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

