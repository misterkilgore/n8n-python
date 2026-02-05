import requests
from datetime import datetime

# URL del tuo endpoint n8n (modifica con il tuo URL)
n8n_url = "https://misterkilgore.app.n8n.cloud/webhook-test/simple-reponse"

# --- Esempio di richiesta GET ---
def get_request():
    try:
        response = requests.get(n8n_url)
        print("GET Status Code:", response.status_code)
        print("GET Response Body:", response.text)
    except Exception as e:
        print("Errore nella GET:", e)

# --- Esempio di richiesta POST ---
def post_request(data):
    # Dati da inviare nel POST (modifica secondo necessità)
    try:
        response = requests.post(n8n_url, json=data)
        print("POST Status Code:", response.status_code)
        return response.text
    except Exception as e:
        print("Errore nella POST:", e)

data = {
        "date": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
        "message": "Messaggio XYZ"
    }

response = post_request(data)
print(f"POST Response: {response}")