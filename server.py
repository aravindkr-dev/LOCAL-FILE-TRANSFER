import socket , reader , time
def start():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		
    print ("Socket successfully created")


    port = int(input("Enter the port in which you want to communicate: "))		

    s.bind(('', port))		
    print ("socket binded to %s" %(port))

    # put the socket into listening mode
    s.listen(1)	
    print ("socket is listening")		

    c, addr = s.accept()	
    print ('Got connection from', addr )

    fname = input(r"#enter the file path: ")
    a1 = fname.find('.')
    ext_of_file = str(fname[a1:])

    cont = reader.split_read(fname)
        
    print("Reach")
    c.send(str(len(cont)).strip().encode('utf-16'))
    #c.send('.jpg'.encode('utf-8'))
    c.send(bytes(ext_of_file , 'utf-8'))
    for i in range(len(cont)):
        c.send(cont[i])
            #time.sleep(1)
        print(i+1 , 'sending')
    print('done')
    c.close()

