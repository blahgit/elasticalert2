import sys
import os
import time


if __name__=="__main__":
	print os.system("ps -ef|grep 'python script'")
	time.sleep(5)
	sys.exit(1)
