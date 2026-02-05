import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("N8N_URL")
print("TEST VARIABILI D'AMBIENTE")
print(f"url={url}")
