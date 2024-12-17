import requests

# Defino la URL del servidor y el endpoint /shared_data
url = "http://192.168.60.211:3030/shared_data"

# Los datos que vamos a enviar en el body, en este caso puedes enviar cualquier cosa
data = {
    "nombre": "ejemplo",
    "valor": "123"
}

# Hago la solicitud POST enviando los datos en formato JSON en el body
response = requests.post(url, json=data)

# Imprimo la respuesta en la terminal
print(response.text)  # Esto debería mostrar las banderas si todo sale bien

