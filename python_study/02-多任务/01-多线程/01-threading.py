import threading
import time

def sing():
	while True:
		print("sing...")
		time.sleep(1)

def dance():
	while True:
		print("dance...")
		time.sleep(1)

def main():
	th1 = threading.Thread(target = sing)
	th2 = threading.Thread(target = dance)

	th1.start()
	th2.start()

if __name__ == "__main__":
	main()
