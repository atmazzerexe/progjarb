import sys
import socket
import select

HOST = '' 
SOCKET_LIST = []
RECV_BUFFER = 4096 
PORT = 9999
daftar = []
username = []
list = []
index = 0


def chat_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)
    
    # add server socket object to the list of readable connections
    SOCKET_LIST.append(server_socket)
 
    print "Chat server started on port " + str(PORT)
 
    while 1:
        # get the list sockets which are ready to be read through select
        # 4th arg, time_out  = 0 : poll and never block
        ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)
        
        for sock in ready_to_read:
        # a new connection request recieved
            if sock == server_socket: 
                sockfd, addr = server_socket.accept()
                SOCKET_LIST.append(sockfd)
                daftar.append(addr)
                #print"List :", daftar[]
                print "Client (%s, %s) connected" % addr
                #print "Isi : ", sockfd
                #broadcast(server_socket, sockfd, "[%s:%s] entered our chatting room\n" % addr)
             

            else:

                try:

                    #data = sock.recv(RECV_BUFFER)
                    #if data:
                        data2 = sock.recv(6)
                      	if data2 =='login ' :
				data1 =sock.recv(6)
#				a=sock.getpeername()
			  	if username.count(data1) == 0 :
					username.append(data1)
			  		list.append(sock)
					user=username[daftar.index(addr)]
	                  		broadcast(server_socket, sockfd, "["+user+"] telah memasuki ruang chat\n")
					sock.send("Login berhasil\n")
				else :
					sock.send("Username sudah ada\n")
				
 				
			if data2 =='send ' :
 			  data3=sock.recv(6)
 			  if username.count(data3) == 0 :
 			  	sock.send("User tidak ada, silahkan cek lagi lewat command 'active'\n")
 			  else :  
 				target = list[username.index(data3)]
 				data4=sock.recv(RECV_BUFFER)
   			  	useractive=daftar.index(sock.getpeername())
   		          	target.send("\r" + '['+ str(username[useractive]) +'] : ' + data4) 
   		          	
                            if data2 =='active\n' :
                            		sock.send("\rDaftar Pengguna aktif :\n")
 			                for index in range(len(username)) :
 			                    sock.send("\r"+username[index]+ "\n")
			                    
			                if data2 =='broad ' :
 			                    data4=sock.recv(RECV_BUFFER)
 			                    useractive = daftar.index(sock.getpeername())
 			                    broadcast(server_socket, sock,"\r" + '['+ str(username[useractive]) +'] ' + data4) 
                            #else:
                     
                                #if sock in SOCKET_LIST:
                                #SOCKET_LIST.remove(sock)

                                #broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr) 

      
                                except:
                                    broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr)
                                    continue

                                    server_socket.close()
    
# broadcast chat messages to all connected clients
def broadcast (server_socket, sock, message):
    for socket in SOCKET_LIST:
        # send the message only to peer
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except :
                # broken socket connection
                socket.close()
                # broken socket, remove it
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)
 
if __name__ == "__main__":

    sys.exit(chat_server())
