import http.server
import socketserver
import os
import threading
from numba import jit
import LICENSE_text

is_running = True
PORT = 8000
WEB_DIR = "."
httpd = None

@jit(nopython=True)
def process_data(data):
    result = 0
    for i in range(len(data)):
        result += data[i] ** 2
    return result

def start_server():
    global httpd
    os.chdir(WEB_DIR)
    print(f"Serving files from: {os.getcwd}")

    Handler = http.server.SimpleHTTPRequestHandler
    
    httpd = socketserver.TCPServer(("", PORT), Handler)
    print(f"Serving at port: {PORT}")
    print(f"Access your server at: http://localhost:{PORT}")


    while is_running:
        try:
            httpd.handle_request()
        except Exception as e:
            print(f"Error: {e}")

    httpd.server_close()
    print("Server stoped")

server_thread = threading.Thread(target=start_server)
server_thread.start()

server_thread.join()