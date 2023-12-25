# Import socket module
import socket,time	
def start():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = int(input("Enter the port in which you want to communicate: "))	
    
    ip = str(input("Enter the ip4 addr of the server: "))
    s.connect((ip, port))
    fn = input("Enter the name of the file: ")
    
    cont = []
    n = s.recv(10).decode('utf-16')
    ext = s.recv(1024).decode('utf-8' , 'ignore')
    fn += ext
    n = int(n)
    print(n , 'recved')
    f = open(fn , 'wb')
    f.close()
    for i in range(n):
        x = s.recv(100000)
        if n%10 == 0:
            time.sleep(2)
        else:
            pass
        with open(fn , 'ab') as f:
            f.write(x)
        #cont.append(x)
        print(i+1 , 'recving')
    print("Done")
