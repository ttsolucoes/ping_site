import time
import requests

url = "https://site-ttsolucoes.onrender.com/"

while True:
    try:
        response = requests.get(url)
        print(f"Pinged {url} - Status: {response.status_code}")
    except Exception as e:
        print(f"Erro: {e}")
    time.sleep(20)  # espera 20 segundos
