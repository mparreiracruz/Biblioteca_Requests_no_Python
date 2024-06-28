'''
06. Requisição POST simples:

Faça uma requisição POST enviando um dado no corpo da requisição.

'''
import requests

'''
# Método do ChatGPT
# URL de destino
url = "https://projetoexemplo-db75d-default-rtdb.firebaseio.com/.json"

# Dados a serem enviados no corpo da requisição
data = {"key": "value"}

# Fazendo a requisição POST
response = requests.post(url, json=data)

# Imprimindo a resposta
print(response.text)
'''

informacoes = '{"key": "value"}'
requisicao = requests.post('https://projetoexemplo-db75d-default-rtdb.firebaseio.com/.json', data=informacoes)
print(requisicao)
print(requisicao.json())