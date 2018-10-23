import socket

def main():
	tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	tcp_socket.bind(("127.0.0.1",3344))

	tcp_socket.listen(128)

	while True:
		new_socket,peer_addr = tcp_socket.accept()
		recv_data = new_socket.recv(1024)
		msg = recv_data.decode("utf-8")
		t_msg = str(msg).upper()
		new_socket.send(t_msg.encode("utf-8"))

	tcp_socket.close()

if __name__ == "__main__":
	main()


