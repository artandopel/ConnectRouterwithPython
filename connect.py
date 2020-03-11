import getpass
import telnetlib        


HOST = input("ip: ")     # ip interface on router
user = input("Enter your remote account: ")  # username on router
password = getpass.getpass()                 # password on router 

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")


tn.write(b"enable\n")
tn.write(b"1234\n")         #password after enable  
tn.write(b"config ter\n")

tn.write(b"interface loopback 1 \n")              #ip interface loopback 1 
tn.write(b"ip add 10.10.10.10 255.255.255.255\n") #set ip address in loopback 1

print("DONE")
tn.write(b"interface loopback 2 \n")              #ip interface loopback 2
tn.write(b" ip add 11.11.11.11 255.255.255.255\n") #set ip address in loopback 2

print("DONE")
tn.write(b"interface loopback 3 \n")              #ip interface loopback 3
tn.write(b" ip add 12.12.12.12 255.255.255.255\n") #set interface loopback 3

print("DONE")
print(tn.read_all().decode('ascii'))
