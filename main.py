import time
import os
from telegram_utils import send_alert
from scoring_engine import evaluate_token

print("Bot ULTRA V5 démarré.")
print("BOT_TOKEN =", os.getenv("BOT_TOKEN"))
print("CHAT_ID =", os.getenv("CHAT_ID"))

fake_tokens = [
    {"name": "DOGEAI", "volume": 12000, "snipers": 4, "age": 3},
    {"name": "MOONX", "volume": 5000, "snipers": 2, "age": 1},
    {"name": "XGPT", "volume": 23000, "snipers": 8, "age": 0.5},
]

index = 0
while True:
    token = fake_tokens[index % len(fake_tokens)]
    score = evaluate_token(token)
    print(f"[Loop] Token: {token['name']} | Score: {score}")
    if score >= 80:
        send_alert(token, score)
    index += 1
    time.sleep(5)
