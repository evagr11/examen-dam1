import requests

# Defino el URL del servidor
url = "http://192.168.60.211:3030/metodo"  # Ruta para la solicitud PATCH

# Si el servidor requiriese enviar datos en la solicitud PATCH, los agregaria aquí, pero como no...

data = {
    # Aquí van los datos que el servidor necesita para procesar la petición
    # Ejemplo: "key": "value"
}

# Hago la petición PATCH
response = requests.patch(url, json=data)  # Usando json si es necesario enviar datos en formato JSON

# Imprimo la respuesta en la terminal
print(response.text)  # Muestra la respuesta del servidor

