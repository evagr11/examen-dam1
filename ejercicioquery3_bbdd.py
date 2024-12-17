import requests

# Defino la URL del servidor y el endpoint /shared_data
url = "http://192.168.60.211:3030/shared_data"

# Los datos que vamos a enviar en la URL como parámetros de consulta
params = {
    "nombre": "ejemplo",
    "valor": "123"
}

# Hago la solicitud POST enviando los datos como parámetros en la URL
response = requests.post(url, params=params)

# Imprimo la respuesta en la terminal
print(response.text)  # Esto debería mostrar las banderas si todo sale bien
