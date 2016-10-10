# Author: Marshall Richards
# Description:
# Chop video and send most recent increment after triggering of accelerometer

import sys
import os
import subprocess
import math
import threading
import time
import pysftp

def f():
	i = 1
	file_name = 'tester'
	accel = 4
	while True:
		file_complete = file_name + str(i) + '.mp4'
		subprocess.call('ffmpeg -i '+ 'http://10.5.23.152/hls/561746771/hls.m3u8 -map 0:0 -t 30 ' + file_complete, shell=True)
		print(file_complete)
		#time.sleep(10)
		i = i + 1
		if accel == 1:
			integer = i - 1
			file_to_send = file_name + str(integer) + '.mp4'
			current_file_to_send = file_name + str(i) + '.mp4'
			#with pysftp.Connection('52.183.41.31', username='carhack', password='Carhack2000Carhack2000') as sftp:
    		#	with sftp.cd('/home/carhack/video'):             # temporarily chdir to public
        	#		sftp.put('video1.mp4')  # upload file to public/ on remote

	test = "video_8.mp4"
	#sleep(10)
	#file_complete = file_name + str(i) + '.mp4'
	#i = i + i
	#subprocess.call('ffmpeg -i '+ 'http://10.5.23.152/hls/513611809/hls.m3u8 -map 0:0 -t 10 ' + test, shell=True)
	#print("hello")
	#threading.Timer(1, f).start()
f()

#when accelerometer i - 1 send to server 