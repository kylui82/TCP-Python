#client.py
import socket

# Create a socket instance and pass it two parameters
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()  # get the local hostname
port = 60001  # initiate port

s.connect((host, port))  # Connect to the server
s.send(b'mytext.txt')  # Send the filename to the server.

while True:
    print('receiving data..')
    data = s.recv(1024).decode()
    print(data)
    if not data:
        break

print('Successfully get the file')
s.close()  # close connection
print('connection closed')
