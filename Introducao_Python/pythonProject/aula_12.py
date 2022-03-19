import requests

'''response = requests.get('https://viacep.com.br/ws/01001000/json/')
print(response.status_code)
print(response.text)
# transformar o JSON em um dicionário
dados_cep = response.json()
print(dados_cep['logradouro'])'''

response = requests.get('https://saocarlos.sp.senai.br/?fbclid=IwAR2qo7OoHSYQeaGg9zVj9JtVgzAqi-tM8nkZ9rjCKwVZV1c3jYacBQ_yPPo')
print(response.text) # retorna todo o HTML da pagina requisitada
