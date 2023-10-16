# IoExternalSecretsGeneratorsV1alpha1PasswordSpec

PasswordSpec controls the behavior of the password generator.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_repeat** | **bool** | set AllowRepeat to true to allow repeating characters. | 
**digits** | **int** | Digits specifies the number of digits in the generated password. If omitted it defaults to 25% of the length of the password | [optional] 
**length** | **int** | Length of the password to be generated. Defaults to 24 | 
**no_upper** | **bool** | Set NoUpper to disable uppercase characters | 
**symbol_characters** | **str** | SymbolCharacters specifies the special characters that should be used in the generated password. | [optional] 
**symbols** | **int** | Symbols specifies the number of symbol characters in the generated password. If omitted it defaults to 25% of the length of the password | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


