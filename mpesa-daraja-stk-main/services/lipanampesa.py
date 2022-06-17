import json
from os import access
import base64
from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth
import keys




#print (datetime.datetime.now())
#2022-06-10 10:17:11.164659
unformatted_time = datetime.now()
formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")
#20220610102839
#print(formatted_time,"this is formatted time")

data_to_encode = str(keys.BusinessShortCode) + keys.lipa_na_mpesa_passkey + formatted_time
encoded_string = base64.b64encode(data_to_encode.encode())
#print(encoded_string) b'MjAyMjA2MTAxMDU4Mzk='

decoded_password = encoded_string.decode('utf-8')

#print (decoded_password)



consumer_key = keys.consumer_key
consumer_secret =keys.consumer_secret
api_URL = (
    "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    )
r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

#{'access_token': 'okOY9y1wkQJR2LVAPH8APJdTAti4', 'expires_in': '3599'}

# print(r.content,r.text,r.apparent_encoding)

json_response = r.json()
# print(json_response)
# player_data.get("Rivaldo")

my_access_token = json_response.get('access_token')
print(my_access_token)

def lipa_na_mpesa(my_access_token):
    
    access_token = my_access_token
    headers = {
        'Authorization': 'Bearer %s' % access_token
    }

    
    
    payload = {
       "BusinessShortCode": keys.BusinessShortCode,
       "Password": decoded_password,
       "Timestamp": formatted_time,
       "TransactionType": "CustomerPayBillOnline",
       "Amount": "1",
        "PartyA": keys.phone_number,
        "PartyB": keys.BusinessShortCode,
        "PhoneNumber":keys.phone_number,
        "CallBackURL": "https://mydomain.com/path",
        "AccountReference": "CompanyXLTD",
        "TransactionDesc": "Payment of X" 
    }


    response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, data = payload)
    print(response.text.encode('utf8'))

# lipa_na_mpesa(my_access_token)


def web(access,decoded_password,formatted_time):
    import requests

    headers = {
#   'Content-Type': 'application/json',
  'Authorization': 'Bearer %s'%access 
}

    response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, data = payload)
    print(response.text.encode('utf8'))

web(my_access_token,decoded_password,formatted_time)