# swagger_client.DefaultApi

All URIs are relative to *https://mobile-api.senscritique.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_product_id_rate_post**](DefaultApi.md#products_product_id_rate_post) | **POST** /products/{product_id}/rate | Rate a product


# **products_product_id_rate_post**
> SuccessStatusResponse products_product_id_rate_post(product_id, body)

Rate a product

Send a rating for a product

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
product_id = 56 # int | The id of the product to rate
body = swagger_client.RatingRequest() # RatingRequest | Rating request body

try: 
    # Rate a product
    api_response = api_instance.products_product_id_rate_post(product_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->products_product_id_rate_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| The id of the product to rate | 
 **body** | [**RatingRequest**](RatingRequest.md)| Rating request body | 

### Return type

[**SuccessStatusResponse**](SuccessStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

