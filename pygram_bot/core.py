import requests
from .exceptions import BotError

class Bot:
    def __init__(self, token: str):
        if not token:
            raise BotError("Token bo‘sh bo‘lishi mumkin emas.")
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}"

    def send_message(self, chat_id: int, text: str):
        url = f"{self.base_url}/sendMessage"
        resp = requests.post(url, data={"chat_id": chat_id, "text": text})
        if resp.status_code != 200:
            raise BotError(f"Xatolik: {resp.text}")
        return resp.json()
