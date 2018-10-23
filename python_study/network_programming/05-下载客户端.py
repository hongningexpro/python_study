import socket

def main():
	tcp_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	srv_ip = input("请输入服务器ip:")
	srv_port = input("请输入服务器port:")

	tcp_sock.connect((srv_ip,int(srv_port)))
	file_name = input("请输入要下载的文件名字:")

	tcp_sock.send(file_name.encode("utf-8"))

	recv_data = tcp_sock.recv(1024)

	with open("新"+file_name,"wb") as f:
		f.write(recv_data)

	tcp_sock.close()

	


if __name__ == "__main__" :
	main()
