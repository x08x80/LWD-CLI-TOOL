import os
import http.server
import socketserver
import threading

PORT = 8000  # You can change this port if needed

def host_with_python_http_server(path):
    """
    This function starts a Python HTTP server to host the website on localhost.
    """
    os.chdir(path)  # Change the current working directory to the provided directory
    
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Serving website at http://localhost:{PORT}")
        httpd.serve_forever()

def expose_with_ngrok():
    """
    This function exposes the Python HTTP server to the internet using Ngrok.
    """
    try:
        print(f"Starting Ngrok to expose the website to the internet over port {PORT}...")
        
        os.system(f"ngrok http {PORT}")  # Expose the port the Python HTTP server is using
    except Exception as e:
        print(f"Failed to start Ngrok: {e}")
