from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTPRequestHandler class
class RequestHandler(BaseHTTPRequestHandler):
    
    # GET method
    def do_GET(self):
        # Send response status code
        self.send_response(200)
        
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
        
        # Send message back to client
        message = "Hello!"
        
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

# Define server port
port = 8080

# Server settings
server_address = ('', port)
httpd = HTTPServer(server_address, RequestHandler)
print(f'Starting server on port {port}')

# Run server
httpd.serve_forever()
