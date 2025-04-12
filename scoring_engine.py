import random

def evaluate_token(token_data):
    base = 50
    volume_score = min(token_data.get("volume", 0) / 1000, 20)
    sniper_score = token_data.get("snipers", 0) * 3
    age_score = max(10 - token_data.get("age", 0), 0)
    random_boost = random.randint(0, 10)
    final_score = base + volume_score + sniper_score + age_score + random_boost
    return round(final_score)
