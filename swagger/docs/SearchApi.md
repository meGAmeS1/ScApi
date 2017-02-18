# swagger_client.SearchApi

All URIs are relative to *https://mobile-api.senscritique.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_get**](SearchApi.md#search_get) | **GET** /search | Search products


# **search_get**
> PaginatedProductListResponse search_get(query, access_token, filter=filter)

Search products

Search products, depending on text (title and description) and universe + sub_universe

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchApi()
query = 'query_example' # str | The text to search
access_token = 'access_token_example' # str | Authenticated token
filter = 'filter_example' # str | Limit the results to a specific universe (optional)

try: 
    # Search products
    api_response = api_instance.search_get(query, access_token, filter=filter)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SearchApi->search_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The text to search | 
 **access_token** | **str**| Authenticated token | 
 **filter** | **str**| Limit the results to a specific universe | [optional] 

### Return type

[**PaginatedProductListResponse**](PaginatedProductListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

