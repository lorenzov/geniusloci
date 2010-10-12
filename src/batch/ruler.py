from geniusloci.loc.models import *






def rule_category():
	places = Place.objects.all()
	for place in places:
		if len(place.foursquare_category) == 0:
			continue
		
		cat = place.foursquare_category
		if cat.find('Arts & Entertainment:') == 0:
			place.category = 1 #visit
		if cat.find('Food:') == 0:
			place.category = 2 #eat
		if cat.find('Parks & Outdoors:') == 0:
			place.category = 1 #visit		
		#Shops:
		if cat.find('Shops:') == 0:
			place.category = 3 #shop
		#Travel:
		if cat.find('Travel:') == 0:
			place.category = 1 #visit
		#Home / Work / Other:
		if cat.find('Home / Work / Other:') == 0:
			place.category = 0 #excluded
		#Nightlife:
		if cat.find('Nightlife:') == 0:
			place.category = 4 #have fun
		
if __name__ == '__main__':
	rule_category