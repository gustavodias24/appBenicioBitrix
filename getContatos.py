import requests
import json

url = ("https://dohkotechnology.bitrix24.com.br/rest/crm.deal.list.json?auth"
       "=81ac8e66006f3bc1005d93df00000185a0ab07139e4ec07874b6d28df50c4bd2a2f8e7")
params = {
    "order": json.dumps({"STAGE_ID": "DESC"})
}

response = requests.get(url, json=params)
result = response.json()

print(result)

# import requests
#
# # consulta = "crm.contact.list"
# consulta = "crm.status.list"
# token = "37f78666006f3bc1005d93df00000185a0ab07a18ea5fa1c973117ceaa0256410a4983"
#
# url = f"https://dohkotechnology.bitrix24.com.br/rest/{consulta}.json?auth={token}"
#
# # payload = {
# #     'order': {'ID': 'DESC'},
# #     'start': -1
# # }
#
# response = requests.post(url)  #, json=payload)
#
# json_data = response.json()
# print(json_data)
