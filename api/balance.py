from http.server import BaseHTTPRequestHandler
import json

USERS = {}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = self.path.split("?")[-1]
        params = dict(p.split("=") for p in query.split("&") if "=" in p)
        user_id = params.get("user_id")

        balance = USERS.get(user_id, 0)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps({
            "balance": balance
        }).encode())
