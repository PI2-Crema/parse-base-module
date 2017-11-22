from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os.path
import simplejson


# HTTPRequestHandler class
class RequestHandler(BaseHTTPRequestHandler):

  def do_GET(self):

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello Gabiras! Sou dev python agora"
        self.wfile.write(bytes(message, "utf8"))
        return

  def do_POST(self):

        print("<----- Request Start -----\n")

        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        data = simplejson.loads(self.data_string)
        with open("nodes.txt", "w") as outfile:
            outfile.write(str(data['id']) + ' ')
            for currentObject in data["data"]:
                outfile.write(str(currentObject['hour']) + ' ')
                outfile.write(str(currentObject['minute']) + ' ')
                outfile.write(str(currentObject['quantity']) + ' ')

        print("<----- Request End -----\n")

def run():
  print('starting server...')
  server_address = ('', 8000)
  httpd = HTTPServer(server_address, RequestHandler)
  print('running server...')
  httpd.serve_forever()

def main():
    run()

if __name__ == "__main__":
    main()
