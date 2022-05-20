import socket,time,os,sys,subprocess
# UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# myaddress without network connection
target_address = ("127.0.0.0", 5555)  # target system IP address
# lets introduce ourselves
user = input("Enter your name: ")
os.system('clear') # clear screen
print("Hello " + user + "!\n")
print("checking for target system...")
wait_os="tell me your os name"
s.sendto(wait_os.encode('ascii'), target_address)
oscheck = s.recvfrom(10)
print(oscheck)
if oscheck[0].decode('ascii') == 'Linux':
    print("Target system is Linux")
    time.sleep(1)
    print("Now only send controll or command related to Linux")

elif oscheck[0].decode('ascii') == 'darwin':
    print("Target system is MAC")
    time.sleep(1)
    print("Now only send controll or command related to MAC")

elif oscheck[0].decode('ascii') == 'win32':
    print("Target system is windows")
    time.sleep(1)
    print("Now only send controll or command related to windows")

while True:
        cmd=input("Enter command: ")
        if cmd == 'exit' or cmd == 'quit':
            print("Goodbye")
            exit()
        else:
            s.sendto(cmd.encode('ascii'), target_address)
            print("instruction sent..")
            time.sleep(1)
            print("waiting for response..")
            response = s.recvfrom(100)
            print(response[0].decode())

s.close()
        