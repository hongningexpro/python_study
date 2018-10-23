import gevent
import re
from gevent import monkey
import socket

monkey.patch_all()

def service_client(clientfd):
    request = clientfd.recv().decode("utf-8")

    request_lines = request.splitlines()
    ret = re.match(r"[^/]+(/[^ ]*)",request_lines[0])

    file_name = ""
    html_content = ""
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "index.html"

    response = "HTTP/1.1 200 OK\r\n"
    response +="\r\n"

    try:
        f = open("./html"+file_name,"rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response +="\r\n"
        response +="-------file not found---------"
        clientfd.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()

    clientfd.send(response.encode("utf-8"))
    clientfd.send(html_content)

def main():
    sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sockfd.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    sockfd.bind(("",8080))
    sockfd.listen(128)

    while True:
        client_fd = sockfd.accept()
        gevent.spawn(service_client,client_fd) 

    sockfd.close()


if __name__ == "__main__":
    main()
