
import http.server
import socket
import socketserver
import webbrowser
from pyqrcode import QRCode
import png
import os
import pyqrcode

port = 8010
os.environ['USERPROFILE']

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']),'OneDrive')
os.chdir(desktop)


handler = http.server.SimpleHTTPRequestHandler
hostname = socket.gethostname()


s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(("8.8.8.8",80))
IP = "http://" + s.getsockname()[0] + ":" + str(port)
link = IP


url = pyqrcode.create(link)
url.svg("myqr.svg",scale = 8)
webbrowser.open('myqr.svg')


with socketserver.TCPServer(("",port),handler) as httpd:
    print("serving at port",port)
    print("Type this in your browser",IP)
    print("or Use thw QRCode")
    httpd.serve_forever()