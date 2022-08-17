#imorting socket module
import socket

def client_program():
    host=socket.gethostname() 
    port=5000 

    
    client_socket=socket.socket()
    client_socket.connect((host,port))
    msg=input("enter the msg to send to server:")

    while msg.lower().strip()!="exit":
        client_socket.send(msg.encode()) 
        data=client_socket.recv(1024).decode()
        print("received frm server: "+data) 
        msg=input("Enter msg to send to server: ")

    client_socket.close()

if __name__=="__main__":
    client_program()