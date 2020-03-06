"""
Hands on exercise Python 

1. Write a method to connect to following endpoint (Use POST and GET methods)

Documentation on post/get methods: https://www.w3schools.com/tags/ref_httpmethods.asp

# Endpoint URL
endpoint = r"https://zsbttrackmeeting.cognitiveservices.azure.com/"
apim_key = "a527f116932642ae9cc5b2940a61cedb"
post_url = endpoint + "/formrecognizer/v2.0-preview/prebuilt/receipt/analyze"
source = r"https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/contoso-allinone.jpg"

2. Use json, requests & urllib libraries to read the jpg file from the URL. 

3. Write a short method to validate/check for the response codes (return "Process executed succesfully for response code 202, "Process Failed", otherwise)


"""
