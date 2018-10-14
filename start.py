import os
import datetime
import time
import cv2
import glob

cap = cv2.VideoCapture(0) 

t = 0
prevTimeCurrent = 0
prevTimeLog = 0

# while(t<30):
while(true):
	# getting current time
	now = datetime.datetime.utcnow()

	# capturing frame
	ret,frame = cap.read()

	# image rotation
	# (h, w) = frame.shape[:2]
	# center = (w / 2, h / 2)
	# M = cv2.getRotationMatrix2D(center, 180, 1.0)
	# frame = cv2.warpAffine(frame, M, (w, h))

	# https://docs.python.org/2/library/datetime.html
	# print now.strftime('%a %b %d %H:%M:%S %Y')
	
	# saving current image every 3 seconds
	if abs( prevTimeCurrent - int(time.mktime(now.timetuple())) )>=3 :
		# removing previous current file
		files = glob.glob('images/current/*')
		for f in files:
			if os.path.basename(f) != "payload.txt":
				os.remove(f)
		
		currentFileName = str(int(time.mktime(now.timetuple())));
		currentFileName = 'images/current/' + currentFileName + '.png';

		# saving image
		cv2.imwrite(currentFileName, frame)

		prevTimeCurrent = int( time.mktime(now.timetuple()) )
		t = t + 1

	# saving log image every 60 seconds
	if abs( prevTimeLog - int(time.mktime(now.timetuple())) )>=60 :
		# generate folder name
		folderName = 'images/log/' + now.strftime('%Y%m%d') + '/'

		# directory creation
		if not os.path.exists(folderName):
			os.makedirs(folderName)

		folderName = folderName + now.strftime('%H') + '00/'
		if not os.path.exists(folderName):
			os.makedirs(folderName)
		
		currentFileName = folderName + now.strftime('%H%M%S') + '.png';
		
		# saving image
		cv2.imwrite(currentFileName, frame)

		prevTimeLog = int( time.mktime(now.timetuple()) )


	# show image in window
	# cv2.imshow('img1',frame)
	time.sleep(0.5)


cap.release()
