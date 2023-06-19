import socket
# import network


f = open('html/index.html', 'r')
html = f.read()
f.close


# Example Code for testing on a PC SOURCE:https://pythonbasics.org/webserver/
if __name__ == "__main__":
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import time

    hostname = "localhost"
    serverport = 8080

    class MyServer(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write(bytes(html, "utf-8"))

    webServer = HTTPServer((hostname, serverport), MyServer)
    print("Server started http://%s:%s" % (hostname, serverport))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")





