import socket
# AF_NET == ipv4
# SOCK_STREAM == TCP

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = input('Where to scan?: ')
targetIP = socket.gethostbyname(target)

print("Now scanning", targetIP)

# low port range for the sake of time, will increase when we add threading
for port in range(78,82):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # we needed to change connect to connect_ex
    c = s.connect_ex((targetIP,port))
    if c == 0:
        print('Port',port,'is open!')
        s.close()
   # else:
    #    print('Port',x,'is closed')

