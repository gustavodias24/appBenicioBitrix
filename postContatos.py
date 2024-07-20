import requests
import json

token = "37f78666006f3bc1005d93df00000185a0ab07a18ea5fa1c973117ceaa0256410a4983"

# URL da sua instância Bitrix24
url = f'https://dohkotechnology.bitrix24.com.br/rest/1/token/crm.contact.add?auth={token}'

# Dados do novo contato a ser adicionado
contact_data = {
    "fields": {
        "NAME": "TESTE BENICIO API",
        "EMAIL": [{"VALUE": "GustavoTesteApi@gmail.com", "VALUE_TYPE": "WORK"}],
        "WEB": "/live-chat/all/5521979739793",
        "SECOND_NAME": "BENICIO",
        "LAST_NAME": "TESTE",
        "OPENED": "Y",
        "ASSIGNED_BY_ID": 1,
        "TYPE_ID": "CLIENT",
        "SOURCE_ID": "SELF",
        "PHONE": [{"VALUE": "5591984044333", "VALUE_TYPE": "WORK"}]
    },
    "params": {"REGISTER_SONET_EVENT": "Y"}
}

# Supondo que você tenha o arquivo de foto em 'photo.jpg'
# files = {'PHOTO': ('photo.jpg', open('photo.jpg', 'rb'))}

# Fazendo a chamada para a API
response = requests.post(url, data=json.dumps(contact_data))  # , files=files)

# Processando a resposta
if response.status_code == 200:
    result = response.json()
    if 'error' in result:
        print(f"Erro: {result['error']}")
    else:
        print(f"Novo contato criado com sucesso; ID={result}")
else:
    print(f"Erro na requisição: {response.status_code}")
