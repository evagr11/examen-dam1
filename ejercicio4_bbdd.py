import requests

# Definir la URL para obtener todos los usuarios
url = "http://192.168.60.211:3030/usuarios"  # Asegúrate de que esta URL sea la correcta

# Realizar la solicitud GET
response = requests.get(url)

# Verificamos el código de estado de la respuesta
if response.status_code == 200:
    usuarios = response.json()  # Parseamos la respuesta JSON

    # Buscar el usuario 'hiddenoter'
    hiddenoter = None
    for usuario in usuarios:
        if usuario['nombre'] == 'hiddenoter':
            hiddenoter = usuario
            break

    if hiddenoter:
        print(f"Usuario encontrado: {hiddenoter}")
        # Obtener el id del usuario
        user_id = hiddenoter['id']
        print(f"ID del usuario 'hiddenoter': {user_id}")

    else:
        print("Usuario 'hiddenoter' no encontrado.")
else:
    print("No se pudo obtener la lista de usuarios. Código de estado:", response.status_code)
