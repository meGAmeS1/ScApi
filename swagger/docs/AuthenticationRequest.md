# AuthenticationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nonce** | **str** | # How to generate nonce: password_md5 &#x3D; md5(user_password) # Use token as hashing key nonce &#x3D; md5(user_email + password_md5, token)  | [optional] 
**email** | **str** | The user email used to login | [optional] 
**password** | **str** | The user passord used to login | [optional] 
**token_id** | **str** | The id of the request_token to authenticate | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


