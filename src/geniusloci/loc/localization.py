import foursquare
from geniusloci.loc.models import *
categories = ['Arts & Entertainment', 'Arcade', 'Art Galley']


api = foursquare.Api()
places = Place.objects.all()


for place in places:
	placex = api.get_venue_detail(place.foursquare_id)
	venue = placex['venue']
	name = venue['name']
	distance = venue['distance']
	address = venue['address']
	city = venue['city']
	category = None
	try:
		category = venue['primarycategory']
		category = category['fullpathname']
	except:
		pass
	print name
	print city
	print category
	break