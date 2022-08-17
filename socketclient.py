#imorting socket module
import socket

def client_program():
    host=socket.gethostname() #getting ip of host
    port=5000 #port no where server is listening

    #create inst of socket
    client_socket=socket.socket()

    #instead of binding in client we r connecting to server
    client_socket.connect((host,port))

    #getting msg to send to server
    msg=input("enter the msg to send to server:")

    while msg.lower().strip()!="exit":
        client_socket.send(msg.encode()) #if client not "exit",encode and send to server
        data=client_socket.recv(1024).decode() #receive any reply
        print("received frm server: "+data) #print received data as text
        msg=input("Enter msg to send to server: ")

    client_socket.close()

if __name__=="__main__":
    client_program()



