import socket

def main():
	udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	udp_socket.bind(("",3344))
	recv_data = udp_socket.recvfrom(1024)
	msg_data = recv_data[0].decode("utf-8")
	peer_addr = recv_data[1]
	print("recieve msg:[%s] from [%s]"%(msg_data,peer_addr))
	udp_socket.close()

if __name__ == "__main__":
	main()
