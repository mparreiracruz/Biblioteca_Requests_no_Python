import requests

requisicao = requests.get('https://projetoexemplo-db75d-default-rtdb.firebaseio.com/.json')
print(requisicao)
print(requisicao.text)
print(requisicao.json())


# informacoes = '{"Nome": "Candiotto"}'
# requisicao = requests.post('https://projetoexemplo-db75d-default-rtdb.firebaseio.com/.json', data=informacoes)
# print(requisicao)
# print(requisicao.json())

# informacoes = '{"Nome": "Amanda", "Sobrenome": "Ferreira", "Idade": "37"}'
# requisicao = requests.patch('https://projetoexemplo-db75d-default-rtdb.firebaseio.com/-O0PvoAZYsbMGLGs9Scm.json', data=informacoes)
# print(requisicao)
# print(requisicao.json())

# requisicao = requests.delete('https://projetoexemplo-db75d-default-rtdb.firebaseio.com/-O0PvoAZYsbMGLGs9Scm.json')
# print(requisicao)
# print(requisicao.json())
