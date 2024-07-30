import requests

# URL de la API
url = "https://my.imperva.com/api/integration/v1/ips"

# Realiza la solicitud GET sin autenticación
response = requests.get(url)
response.raise_for_status()  # Lanza una excepción si la respuesta no es exitosa
json_data = response.json()

# Supongamos que el JSON contiene una lista de IPs en un campo llamado "data"
ips = json_data.get("data", [])

# Convierte el JSON en una lista de IPs
ip_list = [ip['ip'] for ip in ips]  # Ajusta esto según la estructura real del JSON

# Imprime o guarda la lista
print(ip_list)
