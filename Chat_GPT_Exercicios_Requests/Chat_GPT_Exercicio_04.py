'''
04. Acessando cabeçalhos da resposta:

Faça uma requisição GET e imprima os cabeçalhos da resposta.
'''
import requests


# Fazendo a requisição GET
requisicao = requests.get('https://projetoexemplo-db75d-default-rtdb.firebaseio.com/.json')

# Acessando os cabeçalhos da resposta
headers = requisicao.headers

# Imprimindo os cabeçalhos
print("Cabeçalhos da resposta:")
for key, value in headers.items():
    print(f"{key}: {value}")
