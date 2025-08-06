import requests

API_URL = "https://reqres.in/api/users"
API_KEY = "reqres-free-v1"
HEADERS = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}

def agregar_dispositivo(data):
    return requests.post(API_URL, headers=HEADERS, json=data)

def listar_dispositivos():
    return requests.get(API_URL, headers=HEADERS)

def actualizar_dispositivo(user_id, data):
    url = f"{API_URL}/{user_id}"
    return requests.put(url, headers=HEADERS, json=data)

def eliminar_dispositivo(user_id):
    url = f"{API_URL}/{user_id}"
    return requests.delete(url, headers=HEADERS)

def mostrar_dispositivos():
    response = listar_dispositivos()
    if response.status_code == 200:
        data = response.json()
        print("Total de páginas:", data['total_pages'])
        print("Usuarios:")
        for user in data['data']:
            print(f"- {user['id']} | {user['first_name']} {user['last_name']}")
    else:
        print("Error al obtener los usuarios:", response.status_code)

if __name__ == "__main__":
    mostrar_dispositivos()

