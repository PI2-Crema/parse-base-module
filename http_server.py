from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os.path
import simplejson


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
        return

  def do_POST(self):

        print("<----- Request Start -----\n")

        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        data = simplejson.loads(self.data_string)
        with open("data_server.txt", "w") as outfile:
            for key, value in data.items():
                outfile.write(str(value) + ' ')
                # simplejson.dump(" ".join(value), outfile)


        print("<----- Request End -----\n")

def run():
  print('starting server...')

  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('', 8000)
  httpd = HTTPServer(server_address, RequestHandler)
  print('running server...')
  httpd.serve_forever()

def main():
    run()

if __name__ == "__main__":
    main()
