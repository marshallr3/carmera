import sys
import os
import subprocess
import time
import math
import pysftp

def f():
	i = 1
	file_name = 'eatt'
	while True:
		file_complete = file_name + str(i) + '.mp4'
		subprocess.call('ffmpeg -i '+ 'http://10.5.23.152/hls/275230439/hls.m3u8 -map 0:0 -t 30 -y ' + file_complete, shell=True)
		print(file_complete)
		#time.sleep(10)
		i = i + 1
		accel = eval(input("what is accel: "))
		if accel == 1:
			integer = i - 1
			file_to_send = file_name + str(integer) + '.mp4'
			current_file_to_send = file_name + str(i) + '.mp4'
			with pysftp.Connection('52.183.41.31', username='carhack', password='Carhack2000Carhack2000') as sftp:
				with sftp.cd('/home/carhack/video/'):
					sftp.put(file_to_send)  # upload file to public/ on remote
		else:
			pass
f()