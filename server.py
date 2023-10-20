# server.py
import socket

# Create a socket instance and pass it two parameters
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print("socket creation failed with error %s" % (err))

host = socket.gethostname()  # get the local hostname
port = 60001  # initiate port
s.bind((host, port))  # bind host address and port together
s.listen(2) # configure how many client the server can listen simultaneously
print('Server listening....')

while True:
    conn, addr = s.accept()  # accept new connection
    print('Got connection from', addr)
    data = conn.recv(1024).decode()   # Receive the filename from the client
    fileName = repr(data)
    print('Server received the file name', fileName)
    fileNameS = fileName.strip('\'')
    f = open(fileNameS, 'rb')  # open file
    l = f.read(1024)
    print('Start sending file')
    # send data
    while l:
        conn.send(l)
        # print('Sent ', repr(l))
        l = f.read(1024)
    f.close()  # close file

    print('Done sending')
    conn.send('Thank you for connecting'.encode())
    conn.close()  #close connection


