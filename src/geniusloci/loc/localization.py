categories = ['Arts & Entertainment', 'Arcade', 'Art Galley']


api = foursquare.Api()
places = Place.objects.all()


for place in places:
	placex = api.get_venue_detail(place.foursquare_id)
	print placex
	break