import pygame
import pygame.camera
import os
import sys
import time
import StringIO
import gzip

import zlib
import cPickle

pygame.camera.init()
webcam = pygame.camera.Camera("/dev/video0",(320,240))
webcam.start()

count = 0
while True:
	image = webcam.get_image()
	print type(image)
	
	#data = StringIO.StringIO()
	#pygame.image.save(image,x)
	
	data = pygame.image.tostring(image,"RGB")
	print sys.getsizeof(data)
	print sys.getsizeof(zlib.compress(data))
	print sys.getsizeof(zlib.compress(cPickle.dumps(data)))
	
	
	zipr = StringIO.StringIO()
	tmpf = gzip.GzipFile(filename="a.jpg", mode="wb", fileobj=zipr,)
	tmpf.write(data)
	tmpf.close()
	
	print sys.getsizeof(zipr.getvalue())
	
	time.sleep(0.1)
	if count == 20:
		pygame.image.save(image, "image.jpg")
		img = pygame.image.load('image.jpg')
		print sys.getsizeof(pygame.image.tostring(img,"RGB"))
	count = count + 1 
		

	
