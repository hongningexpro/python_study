import threading
import time

g_num = 0

def test1(num):
    global g_num
    for i in range(num):
       g_num +=1 
    print("g_num=%d"%g_num)

def test2(num):
    global g_num
    for i in range(num):
       g_num +=1 
    print("g_num=%d"%g_num)

def main():
    th1 = threading.Thread(target=test1,args=(1000000,))
    th2 = threading.Thread(target=test2,args=(1000000,))

    th1.start()
    th2.start()
    time.sleep(5)
    print("main:g_num=%d"%g_num)

if __name__ == "__main__":
    main()
