import sys
import socket
import select
 
#def chat_client():
    #if(len(sys.argv) < 3) :
        #print 'Usage : python chat_client.py hostname port'
        #sys.exit()
    
    host = 'localhost'
    port = '9999'
    #host = sys.argv[1]
    #port = int(sys.argv[2])
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    #menghubungkan diri dengan remote host
    try :
        s.connect((host, port))
    except :
        print 'Tidak dapat terhubung'
        sys.exit()
     
    print 'Anda telah berhasil terhubung...'
    sys.stdout.write('[Me] '); sys.stdout.flush()
     
    while 1:
        socket_list = [sys.stdin, s]
         
        # mencari daftar socket yang dapat dipakai
        ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
         
        for sock in ready_to_read:             
            if sock == s:
                #pesan masuk dari remote server (s)
                data = sock.recv(4096)
                if not data :
                    print '\nDisconnected from chat server'
                    sys.exit()
                else :
                    #print data
                    sys.stdout.write(data)
                    sys.stdout.write('[Me] '); sys.stdout.flush()     
            
            else :
                #user mengirimkan pesan
                msg = sys.stdin.readline()
                s.send(msg)
                sys.stdout.write('[Me] '); sys.stdout.flush() 

if __name__ == "__main__":

    sys.exit(chat_client())

