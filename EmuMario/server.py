import http.server
from urllib.parse import urlparse, parse_qs
from io import BytesIO
import socketserver

# Define the port number for the server
PORT = 8080

# Define the handler to use for incoming requests
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self): 
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        with open("img.png", mode='wb') as f: 
            f.write(post_data)

        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Right')


# Create a TCP socket and bind it to the localhost and port number
with socketserver.TCPServer(('localhost', PORT), MyHandler) as httpd:
    # Print a message indicating that the server is running
    print(f'Server is running on port {PORT}')

    # Start serving requests until the server is stopped
    httpd.serve_forever()