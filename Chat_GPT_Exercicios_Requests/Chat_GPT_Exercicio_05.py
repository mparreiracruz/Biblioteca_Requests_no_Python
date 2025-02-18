'''
05. Passando parâmetros na URL:

Faça uma requisição GET passando um parâmetro name com valor John.
'''

# import requests
#
# # Parâmetros que serão passados na URL
# params = '{"name": "John"}'
#
# # Fazendo a requisição GET com os parâmetros
# requisicao = requests.get('https://projetoexemplo-db75d-default-rtdb.firebaseio.com/Semestre1.json', params=params)
#
# # Imprimindo o conteúdo da resposta
# print(requisicao.text)
# print(requisicao)
# print(requisicao.json())

import requests

# URL para a qual a requisição será feita
url = 'https://projetoexemplo-db75d-default-rtdb.firebaseio.com/.json'

# Dados que serão passados no corpo da requisição
data = {'name': 'John'}

# Fazendo a requisição POST com os dados
response = requests.post(url, json=data)

# Imprimindo o conteúdo da resposta
print(response.json())


