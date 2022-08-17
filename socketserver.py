#imorting socket module
import socket

def server_program():
    #"127.0.01" or localhost
    #port can range frm 1024 to 65535
    host=socket.gethostname() #getting ip of host
    port=5000

    #create instances of socket
    server_socket=socket.socket()

    #binding host ip and port to socket inst
    #pass host and port as tuple into bind()
    server_socket.bind((host,port))

    #start listening to socket
    server_socket.listen(2)

    #accept incoming conn
    #accept() gives back conn obj and ip add of incoming conn
    conn,address=server_socket.accept()
    print("Connection accepted from "+str(address))

    #msgs can be recevied using while loop keeping conn active
    #receives msgs till there is none left or "exit" msg 
    while True: #infinite while loop to receive data stream (max size 1024 bytes)
        data=conn.recv(1024).decode() #decode received data
        if not data: #if no data received, then terminate while
            break
        print("message frm client "+str(address)+" : "+str(data))
    
        #give provision to send reply back to client
        data=input("Type reply here: ")

        #encode data and sene to client
        conn.send(data.encode())
    
    #closing conn once while loop breaks
    conn.close()

if __name__=="__main__":
    server_program()

#if python pgm is imported, it will bethere as imported code
#wont run till user calls the function
#if run directly using cmd prompt function server_program()
#automatically start

