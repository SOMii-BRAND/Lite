import os,sys, platform,time
try:
   import requests
except:
   os.system('pip2 install requests')
from time import sleep
import requests
def XXX(xxx):
	for xx in xxx + "\n":
		sys.stdout.write(xx);sys.stdout.flush();time.sleep(0.03)
bit = platform.architecture()[0]
if bit == '64bit':
    from li import _site_view_
    XXX("\n \033[38;2;255;127;0;1mSystem Loading _________033[1;0m\n")
    print("\n Congratulations! Your device supported!\n")
    time.sleep(3)
    _site_view_()
elif bit == '32bit':
    from f32 import _site_view_
    print("\n Congratulations! Your device supported!\n")
    time.sleep(3)
    _site_view_()
 
 
