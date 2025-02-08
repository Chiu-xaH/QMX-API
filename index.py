from http.server import BaseHTTPRequestHandler

# 用作托管Vercel
class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write("QMX-API by python!".encode())
        return
