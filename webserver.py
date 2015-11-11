import socket, sys

HOST = '' 
RECV_BUFFER = 4096
PORT = 9999

#Connected using first task's way of connecting to socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(10)
print "Chat server started on port " + str(PORT)

while 1:
	#data2 for receiving the upcoming messages
	data2 = ''
	#sockfd and addr, also some variable that came from my first task
	sockfd, addr = server_socket.accept()
	print >>sys.stderr, 'Connecting From: ', addr, '\n'
	#upcoming messages come to rec first
	rec = sockfd.recv(RECV_BUFFER)

	#when browser tries to connect to localhost
	if rec:
		#data2 with additional data from incoming messages from rec
		data2 = data2 + rec
		#print data2 <--- I'm really thankful to this function m(_ _)m

		#based on what i get from print data2
		if(data2.startswith("GET /001 HTTP/1.1")):
			#opening designated file
			gambar = open("001.jpg")
			#read the whole data file
			grab=gambar.read()
			#close the opened data while keeping the already cached data file
			gambar.close()
			#Sending the 200 OK message to browser, together with the file, can be proofed using firefox network inspection tool
			sockfd.sendall("HTTP/1.1 200 OK \r\n\r\n%s"%grab)
			#For proofing at the server side
			print '1/5 page'

		elif(data2.startswith("GET /002 HTTP/1.1")):
			gambar = open("002.jpg")
			grab=gambar.read()
			gambar.close()
			sockfd.sendall("HTTP/1.1 200 OK \r\n\r\n%s"%grab)
			print '2/5 page'

		elif(data2.startswith("GET /003 HTTP/1.1")):
			gambar = open("003.jpg")
			grab=gambar.read()
			gambar.close()
			sockfd.sendall("HTTP/1.1 200 OK \r\n\r\n%s"%grab)
			print '3/5 page'

		elif(data2.startswith("GET /004 HTTP/1.1")):
			gambar = open("004.jpg")
			grab=gambar.read()
			gambar.close()
			sockfd.sendall("HTTP/1.1 200 OK \r\n\r\n%s"%grab)
			print '4/5 page'

		elif(data2.startswith("GET /005 HTTP/1.1")):
			gambar = open("005.jpg")
			grab=gambar.read()
			gambar.close()
			sockfd.sendall("HTTP/1.1 200 OK \r\n\r\n%s"%grab)
			print '5/5 page'
		
		else:
			#in case when people put the wrong number of page, returning 404 message from the server (too lazy to put other picture, so only blank page)
        		print "Returning 404"
        		#sending the 404 Not Found message to browser, can be proofed using firefox network inspection tool
        		sockfd.sendall("HTTP/1.0 404 Not Found\r\n\r\n")

	sockfd.close()
