import socket  
HOST = '127.0.0.1'  # The server's hostname or IP address 
PORT = 65432        # The port used by the server  
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.connect((HOST, PORT)) 
    while True: 
        text = input("Enter data from Client from Server") 
        s.sendall(bytes(text,'utf-8')) 
        data = s.recv(1024) 
        print("Server : ",data) 
#print('Received', repr(data))   
