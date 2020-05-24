import socket

# AF_NET == ipv4
# SOCK_STREAM == TCP

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = input('Where to scan?: ')
targetIP = socket.gethostbyname(target)

print("Now scanning", targetIP)

def pscan(port):
    try:
        # connect to the target
        s.connect((target, port))
        return True
    except:
        return False

# just scan the first 22 ports for script testing purposes
for x in range(1,23):
    if pscan(x):
        #pscan(x) is either returning True or False
        # if pscan is true, print that port x is open
        print('Port',x,'is open!')
    else:
        print('Port',x,'is closed')

