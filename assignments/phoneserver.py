#imorting socket module
import socket

def server_program():
    host=socket.gethostname() #getting ip of host
    port=5000

    server_socket=socket.socket()
    server_socket.bind((host,port))
    server_socket.listen(2)

    conn,address=server_socket.accept()
    print("Connection accepted from "+str(address))

    while True: 
        data=conn.recv(1024).decode() 
        if not data: 
            break
        print("message frm client "+str(address)+" : "+str(data))
        data=input("Type reply here: ")
        conn.send(data.encode())
    
    conn.close()

if __name__=="__main__":
    server_program()



