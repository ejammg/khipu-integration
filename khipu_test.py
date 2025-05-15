import requests

# Reemplaza con tu API Key proporcionada por Khipu
api_key = "d64172b1-88c8-4167-8b54-0842bbddbe85"

# URL del endpoint para crear pagos
url = "https://payment-api.khipu.com/v3/payments"

# Encabezados requeridos por la API
headers = {
    "x-api-key": api_key,
    "Content-Type": "application/json"
}

# Datos del pago
data = {
    "amount": 5000.0,  # Monto del pago en la moneda especificada
    "currency": "CLP",  # Código de moneda en formato ISO 4217
    "subject": "Cobro de prueba",  # Asunto o descripción breve del pago
    "transaction_id": "orden-1234",  # Identificador único de la transacción
    "return_url": "https://tusitio.com/retorno",  # URL de retorno después del pago
    "cancel_url": "https://tusitio.com/cancelado",  # URL si el usuario cancela el pago
    "notify_url": "https://tusitio.com/webhook",  # URL para recibir notificaciones de Khipu
    "notify_api_version": "3.0"  # Versión de la API de notificaciones
}

# Realizar la solicitud POST para crear el pago
response = requests.post(url, headers=headers, json=data)

# Manejo de la respuesta
if response.status_code == 200:
    payment_info = response.json()
    print("Pago creado exitosamente.")
    print(f"ID del pago: {payment_info['payment_id']}")
    print(f"URL de pago: {payment_info['payment_url']}")
else:
    print(f"Error al crear el pago. Código HTTP: {response.status_code}")
    print(f"Respuesta: {response.text}")

