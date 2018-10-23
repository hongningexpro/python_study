import socket
	
def main():
	#create socket
	udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	send_ip = input("please input peer ip:")	
	#send_port = input("please input peer port:")	
	send_data = input("please input your message:")	
	send_addr = (send_ip,3344)	
	udp_socket.sendto(send_data.encode("utf-8"),send_addr)	

	udp_socket.close()

if __name__ == "__main__":
	main()
