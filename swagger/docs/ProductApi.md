# swagger_client.ProductApi

All URIs are relative to *https://mobile-api.senscritique.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_product_id_rate_post**](ProductApi.md#products_product_id_rate_post) | **POST** /products/{product_id}/rate | Rate a product
[**users_user_id_products_wish_get**](ProductApi.md#users_user_id_products_wish_get) | **GET** /users/{user_id}/products/wish | User wishes


# **products_product_id_rate_post**
> SuccessStatusResponse products_product_id_rate_post(access_token, product_id, body)

Rate a product

Send a rating for a product

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductApi()
access_token = 'access_token_example' # str | Authenticated token
product_id = 56 # int | The id of a product
body = swagger_client.RatingRequest() # RatingRequest | Rating request body

try: 
    # Rate a product
    api_response = api_instance.products_product_id_rate_post(access_token, product_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProductApi->products_product_id_rate_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Authenticated token | 
 **product_id** | **int**| The id of a product | 
 **body** | [**RatingRequest**](RatingRequest.md)| Rating request body | 

### Return type

[**SuccessStatusResponse**](SuccessStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_products_wish_get**
> PaginatedProductListResponse users_user_id_products_wish_get(user_id, access_token)

User wishes

Returns the list of the wishes for a given user

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductApi()
user_id = 'user_id_example' # str | User id (use 'me' for logged in user)
access_token = 'access_token_example' # str | Authenticated token

try: 
    # User wishes
    api_response = api_instance.users_user_id_products_wish_get(user_id, access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ProductApi->users_user_id_products_wish_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User id (use &#39;me&#39; for logged in user) | 
 **access_token** | **str**| Authenticated token | 

### Return type

[**PaginatedProductListResponse**](PaginatedProductListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

