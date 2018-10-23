import threading
import time

g_num = 100

def test1():
    global g_num
    g_num +=1

def test2():
    print("g_num=%d"%g_num)

def main():
    th1 = threading.Thread(target=test1)
    th2 = threading.Thread(target=test2)

    th1.start()
    time.sleep(1)
    th2.start()
    print("main:g_num=%d"%g_num)

if __name__ == "__main__":
    main()
