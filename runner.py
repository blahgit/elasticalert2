import os
if __name__=="__main__":
	count=os.system("ps -ef |grep -v 'grep' | grep -c 'ESAlerter'")
	print count
	if count:
		os.system("python /uhome/kvenkatswammy/elasticalert/elastalert_ui/ESAlerter.py")
	count=os.system("ps -ef |grep -v 'grep' | grep -c 'elastalert.elastalert'")
        print count
	if count:
                os.system("cd /uhome/kvenkatswammy/elasticalert/elastalert; python -m elastalert.elastalert --verbose")

	print "Done."

