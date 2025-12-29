from http.server import BaseHTTPRequestHandler
import json
import os
import asyncio
from aiogram import Bot
from aiogram.types import LabeledPrice

BOT_TOKEN = os.environ["BOT_TOKEN"]
bot = Bot(token=BOT_TOKEN)

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length"))
        body = self.rfile.read(length)
        data = json.loads(body)

        user_id = data["user_id"]
        amount = data["amount"]

        asyncio.run(
            bot.send_invoice(
                chat_id=user_id,
                title="AlimCase",
                description=f"Пополнение на {amount} ⭐",
                payload=f"topup_{user_id}_{amount}",
                provider_token="",
                currency="XTR",
                prices=[LabeledPrice(label="Stars", amount=amount)],
            )
        )

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'{"ok": true}')
