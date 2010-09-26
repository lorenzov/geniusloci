from django.test.client import Client
import time
import random

c = Client()
lat = 45.4530
lon = 9.152


for i in range(0,100):
	c.get('/mobi/geo/?lat=' + str(lat)+ '&lon=' + str(lon))
	lon += 0.00005
	time.sleep(random.randint(0,20)/10)
	print lon