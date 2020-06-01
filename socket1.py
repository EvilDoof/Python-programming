import socket
socobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socobj.connect(("data.pr4e.org", 80))
cmd = "GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n".encode() #converts UNICODE to byte code (UTF-8)
socobj.send(cmd)

while True:
    data = socobj.recv(512)
    if (len(data) < 1):
        break
    print(data.decode()) #converts byte code into UNICODE
socobj.close()