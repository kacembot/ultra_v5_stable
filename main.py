import requests
import json
import time

# === CONFIGURATION ===
USE_FAKE_DATA = False  # Mode réel activé
WEBHOOK_URL = "https://n8n-production-fa5c.up.railway.app/webhook/strongbuy"
INTERVAL = 10  # secondes entre chaque scan

# === FUNCTION TO FETCH REAL TOKENS ===
def get_real_token_data():
    # ⚠️ Placeholder à remplacer par intégration réelle (Axiom, PumpFun, etc.)
    # Ici on simule un token STRONG BUY détecté
    return {
        "name": "REALCOIN",
        "score": 94,
        "market_cap": "82K",
        "age": "1m21s",
        "chain": "Solana"
    }

# === ENVOI VERS LE WEBHOOK ===
def send_strongbuy_alert(token):
    payload = {
        "token": token["name"],
        "score": token["score"],
        "market_cap": token["market_cap"],
        "age": token["age"],
        "chain": token["chain"]
    }
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(WEBHOOK_URL, data=json.dumps(payload), headers=headers)
        print(f"[SENT] {token['name']} → {response.status_code} {response.text}")
    except Exception as e:
        print("[ERROR]", e)

# === LOOP PRINCIPAL ===
if __name__ == "__main__":
    print("🚀 MODE RÉEL ACTIVÉ – BOT STRONG BUY EN LIGNE")
    while True:
        token_data = get_real_token_data()
        send_strongbuy_alert(token_data)
        time.sleep(INTERVAL)
