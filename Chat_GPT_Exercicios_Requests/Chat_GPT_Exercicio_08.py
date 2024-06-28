'''
Tratando códigos de status:

Faça uma requisição GET para e verifique se a resposta indica um erro 404.
'''

import requests

# Faça uma requisição GET para uma URL que retorna um erro 404
response = requests.get("https://projetoexemplo-db75d-default-rtdb.firebaseio.com/status/404.json")

# Verifique o código de status da resposta
if response.status_code == 404:
    print("Erro 404: Página não encontrada.")
else:
    print(f"Código de status: {response.status_code}")

# Opcionalmente, você pode querer levantar uma exceção se o código de status não for bem-sucedido
try:
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"Erro HTTP: {err}")
