from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json
import requests


# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Send message back to client
        message = "Hello Gabiras! Sou dev python agora"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        post_register_data()
        return

  def do_POST(self):

        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()

        request_path = self.path

        print("\n----- Request Start ----->\n")
        print(request_path)


        if self.headers:
            request_headers = self.headers
            content_length = request_headers.get_all('content-length')
            length = int(content_length[0]) if content_length else 0

            print(request_headers)
            print(self.rfile.read(length))



        print("<----- Request End -----\n")


def run():
  print('starting server...')

  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('127.0.0.1', 8000)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()

# ID  HORA MINUTO NIVEL(0/100) BATERIA(0/100) CODE-ERROR  PH TEMPERATURA CODUTIVIDADE
def post_register_data(post_fields):
    url = 'http://192.168.15.151:3000/feeders/register_data'
    requests.post(url, json=post_fields)
    print(post_fields)

def read_file():
    keys = ["network_code",
            "hora",
            "minute",
            "food_level",
            "battery_level",
            "error_code",
            "ph",
            "temperature",
            "conductivity"]
    json_data = {}
    array_data = []
    with open("node.txt", "r") as f:
        data = f.readlines()

        for line in data:
            words = line.split()

            for index, value in enumerate(words):
                json_data[keys[index]] = value

            array_data.append(json_data)
            json_data = {}


        f.close()
    request_data = {'data':array_data}
    return request_data

post_register_data(read_file())
