
########### Python Form Recognizer Async Layout #############

"""
https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/contoso-allinone.jpg

key:a527f116932642ae9cc5b2940a61cedb
endpoint: https://zsbttrackmeeting.cognitiveservices.azure.com/

"""

import json
import time
from requests import get, post
import urllib.request

# Endpoint URL
endpoint = r"https://zsbttrackmeeting.cognitiveservices.azure.com/"
apim_key = "a527f116932642ae9cc5b2940a61cedb"
post_url = endpoint + "/formrecognizer/v2.0-preview/prebuilt/receipt/analyze"
source = r"https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/contoso-allinone.jpg"

print(source)
headers = {
    # Request headers
    'Content-Type': 'image/jpg',
    'Ocp-Apim-Subscription-Key': "a527f116932642ae9cc5b2940a61cedb",
}

print("Printing headers.......{}".format(headers))

params = {
    "includeTextDetails": True
}

with urllib.request.urlopen(source) as url:
  data_bytes=url.read()
  print(data_bytes)
#     with open('temp.jpg', 'wb') as f:
#         f.write(url.read())

# file = urllib.request.urlopen(source)
# data_bytes = file.read()
# print(data_bytes)
    

try:
    resp = post(url = post_url, data = data_bytes, headers = headers, params = params)
    print("Printing the response here.........................................................")
    print(resp.status_code)
    if resp.status_code != 202:
        print("POST analyze failed:\n%s" % resp.text)
        quit()
    print("POST analyze succeeded:\n%s" % resp.headers)
    get_url = resp.headers["operation-location"]
except Exception as e:
    print("POST analyze failed:\n%s" % str(e))
    quit()



def get_analyzed_results():  
  n_tries = 5
  n_try = 0
  wait_sec = 6
  while n_try < n_tries:
      try:
          resp = get(url = get_url, headers = {"Ocp-Apim-Subscription-Key": apim_key})
          resp_json = json.loads(resp.text)

          print(resp_json)
          if resp.status_code != 200:
              print("GET Layout results failed:\n%s" % resp_json)
              quit()
          status = resp_json["status"]
          if status == "succeeded":
              print("Layout Analysis succeeded:\n%s" % resp_json)
              quit()
          if status == "failed":
              print("Analysis failed:\n%s" % resp_json)
              quit()
          # Analysis still running. Wait and retry.
          time.sleep(wait_sec)
          n_try += 1     
      except Exception as e:
          msg = "GET analyze results failed:\n%s" % str(e)
          print(msg)
          quit()
  return 1 
