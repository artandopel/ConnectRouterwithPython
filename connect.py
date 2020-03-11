import getpass
import telnetlib


HOST = input("ip: ")
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")


tn.write(b"enable\n")
tn.write(b"1234\n")
tn.write(b"config ter\n")

tn.write(b"interface loopback 1 \n")
tn.write(b"ip add 10.10.10.10 255.255.255.255\n")

print("DONE")
tn.write(b"interface loopback 2 \n")
tn.write(b" ip add 11.11.11.11 255.255.255.255\n")

print("DONE")
tn.write(b"interface loopback 3 \n")
tn.write(b" ip add 12.12.12.12 255.255.255.255\n")

print("DONE")
print(tn.read_all().decode('ascii'))