import threading
import time
import sys
import os

global queue
queue = 0
global loopcount
loopcount = 0
#More workers faster program is but more power it needs
global workers
workers = 1

def f():
	global queue
	global loopcount
	queue = queue + 1
	loopcount = loopcount + 1
	#main code goes under here:


	print("loopcount = ", str(loopcount))
	print("queue = ", str(queue))


	#Main code ends here:
	time.sleep(1)
	queue = queue - 1

if __name__ == "__main__":
	while True:
		t = threading.Thread(target=f)
		if queue >= workers:
			pass
		else:
			#change cls to clear if your on linux / mac (you dont really need it)
			#os.system('cls')
			t.start()

