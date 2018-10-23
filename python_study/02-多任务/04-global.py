import threading
import time

g_nums = [11,22,33]

def test1(tmp_val):
    tmp_val.append(44)

def test2(tmp_val):
    print("tmp_val=%s"%str(tmp_val))

def main():
    th1 = threading.Thread(target=test1,args=(g_nums,))
    th2 = threading.Thread(target=test2,args=(g_nums,))

    th1.start()
    time.sleep(1)
    th2.start()
    print("main:g_nums=%s"%str(g_nums))

if __name__ == "__main__":
    main()
