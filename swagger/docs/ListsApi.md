# swagger_client.ListsApi

All URIs are relative to *https://mobile-api.senscritique.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lists_list_id_get**](ListsApi.md#lists_list_id_get) | **GET** /lists/{list_id} | Describe a list information (name, ...)
[**lists_list_id_get_0**](ListsApi.md#lists_list_id_get_0) | **GET** /lists/{list_id}/ | Get all the products of a list
[**lists_list_id_products_get**](ListsApi.md#lists_list_id_products_get) | **GET** /lists/{list_id}/products | Get the products of a list
[**lists_list_id_products_product_id_delete**](ListsApi.md#lists_list_id_products_product_id_delete) | **DELETE** /lists/{list_id}/products/{product_id}/ | Remove a product from a list
[**lists_list_id_products_product_id_post**](ListsApi.md#lists_list_id_products_product_id_post) | **POST** /lists/{list_id}/products/{product_id} | Add product to list
[**lists_list_id_products_product_id_post_0**](ListsApi.md#lists_list_id_products_product_id_post_0) | **POST** /lists/{list_id}/products/{product_id}/ | Add a product in a list
[**users_me_lists_post**](ListsApi.md#users_me_lists_post) | **POST** /users/me/lists | Create a list for the given user


# **lists_list_id_get**
> ListDescriptionResponse lists_list_id_get(access_token, list_id)

Describe a list information (name, ...)

Describe a list information (name, ...)

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ListsApi()
access_token = 'access_token_example' # str | Authenticated token
list_id = 56 # int | The id of a list

try: 
    # Describe a list information (name, ...)
    api_response = api_instance.lists_list_id_get(access_token, list_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ListsApi->lists_list_id_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Authenticated token | 
 **list_id** | **int**| The id of a list | 

### Return type

[**ListDescriptionResponse**](ListDescriptionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_list_id_get_0**
> PaginatedProductListResponse lists_list_id_get_0(access_token, list_id)

Get all the products of a list

Get all the products of a list

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ListsApi()
access_token = 'access_token_example' # str | Authenticated token
list_id = 56 # int | The id of a list

try: 
    # Get all the products of a list
    api_response = api_instance.lists_list_id_get_0(access_token, list_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ListsApi->lists_list_id_get_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Authenticated token | 
 **list_id** | **int**| The id of a list | 

### Return type

[**PaginatedProductListResponse**](PaginatedProductListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_list_id_products_get**
> PaginatedProductListResponse lists_list_id_products_get(access_token, list_id, limit=limit, offset=offset)

Get the products of a list

Get all th product in a list. This method uses a limit/offset system to limit the results returned by the request.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ListsApi()
access_token = 'access_token_example' # str | Authenticated token
list_id = 56 # int | The id of a list
limit = 56 # int | The maximum number of product to return. Default to 20. (optional)
offset = 56 # int | The offset of the beginning of the list. Default to 0. (optional)

try: 
    # Get the products of a list
    api_response = api_instance.lists_list_id_products_get(access_token, list_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ListsApi->lists_list_id_products_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Authenticated token | 
 **list_id** | **int**| The id of a list | 
 **limit** | **int**| The maximum number of product to return. Default to 20. | [optional] 
 **offset** | **int**| The offset of the beginning of the list. Default to 0. | [optional] 

### Return type

[**PaginatedProductListResponse**](PaginatedProductListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_list_id_products_product_id_delete**
> SuccessStatusResponse lists_list_id_products_product_id_delete(list_id, product_id)

Remove a product from a list

Remove the designated product in the list.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ListsApi()
list_id = 56 # int | The id of a list
product_id = 56 # int | The id of a product

try: 
    # Remove a product from a list
    api_response = api_instance.lists_list_id_products_product_id_delete(list_id, product_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ListsApi->lists_list_id_products_product_id_delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| The id of a list | 
 **product_id** | **int**| The id of a product | 

### Return type

[**SuccessStatusResponse**](SuccessStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_list_id_products_product_id_post**
> PaginatedProductListResponse lists_list_id_products_product_id_post(access_token, list_id, product_id)

Add product to list

Add a product (specified by productId) to the specified list (listId)

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ListsApi()
access_token = 'access_token_example' # str | Authenticated token
list_id = 56 # int | The id of a list
product_id = 56 # int | The id of a product

try: 
    # Add product to list
    api_response = api_instance.lists_list_id_products_product_id_post(access_token, list_id, product_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ListsApi->lists_list_id_products_product_id_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Authenticated token | 
 **list_id** | **int**| The id of a list | 
 **product_id** | **int**| The id of a product | 

### Return type

[**PaginatedProductListResponse**](PaginatedProductListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_list_id_products_product_id_post_0**
> SuccessStatusResponse lists_list_id_products_product_id_post_0(access_token, list_id, product_id)

Add a product in a list

Add the designated product in the list. If the list already contains the item it will not be re-add. Because the universe filtering is done client side, this method also allows to add items in a list even if their universe is different.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ListsApi()
access_token = 'access_token_example' # str | Authenticated token
list_id = 56 # int | The id of a list
product_id = 56 # int | The id of a product

try: 
    # Add a product in a list
    api_response = api_instance.lists_list_id_products_product_id_post_0(access_token, list_id, product_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ListsApi->lists_list_id_products_product_id_post_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Authenticated token | 
 **list_id** | **int**| The id of a list | 
 **product_id** | **int**| The id of a product | 

### Return type

[**SuccessStatusResponse**](SuccessStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_me_lists_post**
> ListCreationResponse users_me_lists_post(label, sub_universe, access_token)

Create a list for the given user

Create a list for a specific user, with a Sub-Universe type (album, ...)

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ListsApi()
label = 'label_example' # str | The name of the list
sub_universe = 56 # int | The id of the sub universe attached to the list
access_token = 'access_token_example' # str | Authenticated token

try: 
    # Create a list for the given user
    api_response = api_instance.users_me_lists_post(label, sub_universe, access_token)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ListsApi->users_me_lists_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| The name of the list | 
 **sub_universe** | **int**| The id of the sub universe attached to the list | 
 **access_token** | **str**| Authenticated token | 

### Return type

[**ListCreationResponse**](ListCreationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

