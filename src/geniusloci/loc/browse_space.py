from django.test.client import Client
import time

c = Client()
lat = 45.4598
lon = 9.152


for i in range(0,100):
	c.get('/mobi/geo/?lat=' + str(lat)+ '&lon=' + str(lon))
	lon += 0.0001
	time.sleep(1)
	print lat