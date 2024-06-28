'''
Requisição com tempo limite (timeout):

Faça uma requisição GET com um tempo limite de 3 segundos e trate a exceção gerada.
'''

import requests
from requests.exceptions import Timeout

url = "https://projetoexemplo-db75d-default-rtdb.firebaseio.com/..json"
timeout_seconds = 3


try:
    response = requests.get(url, timeout=timeout_seconds)
    response.raise_for_status()  # Lança uma exceção para erros HTTP
    print("Requisição bem-sucedida!")
    print("Conteúdo da resposta:", response.text)
except Timeout:
    print(f"Timeout ocorreu após {timeout_seconds} segundos.")
except requests.exceptions.RequestException as e:
    print("Erro durante a requisição:", e)
