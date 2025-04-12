import os
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
    print("❌ Erreur : BOT_TOKEN ou CHAT_ID manquant dans .env")

def send_alert(token_data, score):
    name = token_data.get("name", "Unknown")
    message = f"🚨 STRONG BUY DETECTED\nToken: {name}\nScore: {score}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        response = requests.post(url, data=payload)
        print("——— DEBUG TELEGRAM ———")
        print("URL:", url)
        print("Payload:", payload)
        print("Status Code:", response.status_code)
        print("Response:", response.text)
    except Exception as e:
        print("❌ Exception lors de l’envoi Telegram :", e)
