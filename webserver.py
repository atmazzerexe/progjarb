import socket, sys

HOST = '' 
RECV_BUFFER = 4096
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(10)
print "Chat server started on port " + str(PORT)

while 1:
	data2 = ''
	sockfd, addr = server_socket.accept()
	print >>sys.stderr, 'Connecting From: ', addr, '\n'
	rec = sockfd.recv(RECV_BUFFER)

	if rec:
		data2 = data2 + rec
		#print data2 <--- I'm really thankful to this function m(_ _)m

		if(data2.startswith("GET /001 HTTP/1.1")):
			gambar = open("001.jpg")
			grab=gambar.read()
			gambar.close()
			sockfd.sendall("HTTP/1.1 200 OK \r\n\r\n%s"%grab)
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
        		print "Returning 404"
        		sockfd.sendall("HTTP/1.0 404 Not Found\r\n\r\n")

	sockfd.close()
