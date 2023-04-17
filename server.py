import http.server
from urllib.parse import urlparse, parse_qs
from io import BytesIO
import socketserver

from SegmentationAI import Decider
from PIL import Image

# Define the port number for the server
PORT = 8080
decider = Decider()


# Define the handler to use for incoming requests
class MarioHandler(http.server.SimpleHTTPRequestHandler):
    image_counter = 0

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self): 
        movement = decide_movement_segmentation("buff.png")
        print(movement)

        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(bytes(movement, 'utf-8'))


def decide_movement_segmentation(img):
    # Preprocess image
    image = Image.open(img)
    width, height = image.size
    cropped_image = image.crop((0, 0, width, height//2))
    cropped_image.save(img)
    
    actionPair, angle = decider.direction_to_move(img)
    action, move = actionPair

    return move


# Create a TCP socket and bind it to the localhost and port number
with socketserver.TCPServer(('localhost', PORT), MarioHandler) as httpd:
    # Print a message indicating that the server is running
    print(f'Server is running on port {PORT}')

    # Start serving requests until the server is stopped
    httpd.serve_forever()