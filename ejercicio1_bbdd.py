import requests 

# Haré una solicitud GET a la ruta '/'
url = "http://192.168.60.211:3030/"  # Defino el URL del servidor
response = requests.get(url)  # Hago la petición GET y guardo la respuesta

print(response.text)  # Imprimo la respuesta en la terminal

