import socket
import multiprocessing
import select
import re

class HNWebServer(object):
    """
    HNweb服务器，采用Epoll实现
    多进程处理浏览器请求
    支持HTTP1.1 长连接
    """
    def __init__(self,port):
        #创建套接字
        self.tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        #绑定套接字ip地址端口号
        self.tcp_socket.bind(("",port))
        #设置套接字为监听状态
        self.tcp_socket.listen(128)
        #设置套接字为非阻塞状态
        self.tcp_socket.setblocking(False)
        #创建一个epoll对象
        self.epl = select.epoll()
        #将监听套接字对应的fd注册epoll中
        self.epl.register(self.tcp_socket.fileno(),select.EPOLLIN)
        #创建一个文件描述符对应的套接字字典
        self.client_sock_dict = {}

    def service_client(self,new_socket,data):
        response = ""
        request_lines = data.splitlines()
        #处理请求看浏览器请求的内容
        ret = re.match(r"[^/]+(/[^ ]*)",request_lines[0])
        if ret:
            filename = ret.group(1)
            if filename == "/":
                filename = "/index.html"
                response = self.deal_with_static_request(filename)
            elif filename.endswith(".py"):
                response = self.deal_with_dynaminc_request(filename)
            else:
                response = self.deal_with_static_request(filename)
            new_socket.send(response)
        new_socket.close()
    

    def deal_with_static_request(self,filename):
        #处理静态页面请求
        headers = "HTTP/1.1 200 OK\r\n"
        try:
            f = open("./html"+filename,"rb")
        except:
            return self.deal_with_404()
        else:
            html_content = f.read()
            headers += "Content-Length:%d\r\n"%len(html_content)
            headers +="\r\n"
            return (headers.encode("utf-8")+html_content)

    def deal_with_dynamic_request(self,request):
        #处理动态请求
        pass

    def deal_with_404(self):
        headers = "HTTP/1.1 404 NOT FOUND\r\n"
        headers +="\r\n"
        body = "-----file not found------"
        return (headers+body).encode("utf-8")

    def run_forever(self):
        while True:
            fd_event_list = self.epl.poll()  #默认阻塞，直到有事件到来,返回一个文件描述符列表
            for fd,event in fd_event_list:
                if fd == self.tcp_socket.fileno():
                    #如果是监听套接字有时间，那么说明有客户端连接
                    new_socket,client_addr = self.tcp_socket.accept()
                    self.client_sock_dict[new_socket.fileno()] = new_socket
                    self.epl.register(new_socket.fileno(),select.EPOLLIN) 
                elif event == select.EPOLLIN:
                    #收到浏览器发来的数据并解码
                    recv_data = self.client_sock_dict[fd].recv(1024).decode("utf-8")
                    if recv_data:
                        #如果收到的数据不为空，则说明浏览器发来请求，调用函数处理
                        p = multiprocessing.Process(target=self.service_client,args=(self.client_sock_dict[fd],recv_data,))
                        p.start()
                    else:
                        #如果收到的数据为空，则说明浏览器数据请求完毕，主动断开连接，关闭套接字并从字典中移除套接字
                        self.client_sock_dict[fd].close()
                        self.epl.unregister(fd)
                        del self.client_sock_dict[fd]

if __name__ == "__main__":
    webserver = HNWebServer(8080)
    webserver.run_forever()
