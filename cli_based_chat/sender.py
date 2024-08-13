import socket as sk

s = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
target_ip = "127.0.0.1"
port_no = 2525

target_address = (target_ip,port_no)

quite = True
while quit:
    message = input("plz enter the message : ")
    encyp_message = message.encode("ascii")
    s.sendto(encyp_message,target_address)

    user_input = input("do i want to quit it press Y/y")
    if user_input == "y" or user_input == "y":
        quite = False

