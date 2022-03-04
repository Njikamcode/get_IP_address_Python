# pip install socket
import socket

hostname = socket.gethostname()
ipAddress = socket.gethostbyname(hostname)

print('My IP Adress is: ' + ipAddress)