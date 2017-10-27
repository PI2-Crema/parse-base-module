from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import requests
import os.path
import time


# HTTPRequestHandler class
class RequestHandler(BaseHTTPRequestHandler):

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
  server_address = ('', 8000)
  httpd = HTTPServer(server_address, RequestHandler)
  print('running server...')
  run_observer()
  httpd.serve_forever()

def run_observer():
    try:
        while True:
            time.sleep(1)
            observer('node.txt')
    except KeyboardInterrupt:
        print("parei")

def observer(filepath):
    if os.path.isfile(filepath):
        filename = filepath.split('.')
        file = filename[0] + '.txt'
        file_copy = filename[0] + '_copy.txt'
        os.rename(
            file,
            file_copy
            )

        status_code = post_register_data(read_file(file_copy))
        if status_code == 200:
            delete_file(file_copy)

# ID  HORA MINUTO NIVEL(0/100) BATERIA(0/100) CODE-ERROR  PH TEMPERATURA CODUTIVIDADE
def post_register_data(post_fields):
    url = 'http://192.168.15.151:3000/feeders/register_data'
    post_request = requests.post(url, json=post_fields)
    print(post_fields)
    return post_request.status_code

def read_file(file_name):
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
    with open(file_name, "r") as f:
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

def delete_file(file_name):
    if os.path.isfile(file_name):
        os.remove(file_name)

def main():
    run()

if __name__ == "__main__":
    main()
