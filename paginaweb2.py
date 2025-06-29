from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write('<h1>Alô, mundo!</h1>'.encode('utf-8'))

server = HTTPServer(('localhost', 8080), HelloHandler)
print("Servidor rodando em http://localhost:8080")
server.serve_forever()
