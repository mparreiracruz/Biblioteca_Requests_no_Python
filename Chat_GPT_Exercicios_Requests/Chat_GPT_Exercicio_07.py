'''
07. Enviando dados em uma requisição POST:

Faça uma requisição POST enviando os dados {"username": "john", "password": "1234"}.
'''

import requests

informacoes = '{"username": "John", "password": "1234"}'
requisicao = requests.post('https://projetoexemplo-db75d-default-rtdb.firebaseio.com/.json', data=informacoes)
print(requisicao)
print(requisicao.json())

'''
# Método do ChatGPT

# URL para a qual vamos enviar a requisição POST
url = "https://projetoexemplo-db75d-default-rtdb.firebaseio.com/.json"

# Dados a serem enviados no corpo da requisição
data = {
    "username": "john",
    "password": "1234"
}

# Fazendo a requisição POST
response = requests.post(url, json=data)

# Imprimindo o status da resposta e o conteúdo
print("Status Code:", response.status_code)
print("Response Body:", response.text)
'''