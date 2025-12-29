from http.server import BaseHTTPRequestHandler
import json

# Хранилище баланса
USERS = {}

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length"))
        data = json.loads(self.rfile.read(length))

        user_id = str(data["user_id"])
        amount = int(data["amount"])

        USERS[user_id] = USERS.get(user_id, 0) + amount

        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps({"balance": USERS[user_id]}).encode())
