import server , client

def dec():
    inp = input("SERVER(S)/CLIENT(C): ")

    inp = inp.upper()

    if inp == 'S':
        server.start()
    elif inp == 'C':
        client.start()
    else:
        print("Invalid input..")
        exit()
dec()
