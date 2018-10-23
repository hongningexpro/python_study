import multiprocessing
import time

def put_2_queue(q):
    for num in range(100):
        q.put(num)
        time.sleep(3)
    print("数据存放完毕!")

def get_from_queue(q):
    recv_list = list()
    while True:
        recv_list.append(q.get())
        print(recv_list)
        time.sleep(1)

def main():
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=put_2_queue,args=(q,)) 
    p2 = multiprocessing.Process(target=get_from_queue,args=(q,)) 

    p1.start()
    p2.start()

if __name__ == "__main__":
    main()
