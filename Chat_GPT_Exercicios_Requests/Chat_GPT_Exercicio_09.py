'''
09. Cabeçalhos da requisição:

Faça uma requisição GET enviando um cabeçalho customizado.
'''

import requests

# URL alvo
url = 'https://projetoexemplo-db75d-default-rtdb.firebaseio.com/.json'

# Cabeçalho customizado
headers = {'X-Custom-Header': 'ValorCustomizado'}

# Fazendo a requisição GET com cabeçalhos customizados
response = requests.post(url, json=headers)

# Verificando o status da resposta
print(f'Status Code: {response.status_code}\n')

# Exibindo o conteúdo da resposta (json para melhor visualização)
print(response.json())
