from django.test.client import Client
import time

c = Client()
lat = 45.4398
lon = 9.2244


for i in range(0,100):
	client.get('/mobi/geo/?lat=' + str(lat)+ '&lon=' + str(lon))
	lat += 0.0001
	time.sleep(1)
	print lat