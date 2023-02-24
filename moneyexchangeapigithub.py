import requests
import json

web_url = "https://api.apilayer.com/exchangerates_data/latest?base="

payload = {}
headers = {
    "apikey": "your_api_key"
}
# you can get it from exchangeratesapi.io


exchangedcurrency = input("exchanging currency: ")
desiredcurrency = input("desiring currency: ")
exchangedcurrency = exchangedcurrency.upper()
desiredcurrency = desiredcurrency.upper()
exchangedamount = int(input("How much {0} do you want to exchange?".format(exchangedcurrency)))

web_url = web_url + exchangedcurrency
response = requests.request("GET", web_url, headers=headers, data = payload)
status_code = response.status_code
result = response.text

database = json.loads(result)

print("1 {0}: {1} {2}".format(exchangedcurrency,database["rates"][desiredcurrency],desiredcurrency))

obtainedamount = exchangedamount * (float(database["rates"][desiredcurrency]))

print("{0} {1} : {2} {3}".format(exchangedamount,exchangedcurrency,obtainedamount,desiredcurrency))  
       

    



