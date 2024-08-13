import socket as sk

s = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
# ip_address = "192.168.244.85"
ip_address = "127.0.0.1"
port_no = 2525
address = (ip_address,port_no)
s.bind(address)  #regester 

while True:
    data = s.recvfrom(100)  # 100 is buffer size
    message = data[0]
    ip_address = data[1][0]
    message = data.decode('ascii')
    print(ip_address,'>>>>>',message) 
    
    if True:
        file = open('ip','w')
        file.write(ip_address,message)
        file.close()