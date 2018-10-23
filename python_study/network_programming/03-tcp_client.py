import socket

def main():
	tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	tcp_socket.connect(("127.0.0.1",3344))

	send_data = input("请输入你转换的字母:")

	tcp_socket.send(send_data.encode("utf-8"))
	recv_data = tcp_socket.recv(1024)

	msg = recv_data.decode("utf-8")
	
	print("收到[%s]"%(msg))

	tcp_socket.close()

if __name__ == "__main__":
	main()
