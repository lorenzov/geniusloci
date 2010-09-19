# Create your views here.
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, HttpResponseServerError, HttpResponsePermanentRedirect
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
#from django.contrib.auth.decorators import login_required
#from django.views.decorators.vary import vary_on_headers
#from django.contrib.auth.models import *
#from django.core.paginator import Paginator, InvalidPage, EmptyPage
#from django.core import serializers
#from django.shortcuts import get_object_or_404
#from django.core.cache import cache
from geniusloci.loc.models import *
import foursquare
from decimal import *

def index(request):
	
	places = Place.objects.all().order_by('-id')[:10]
	c = RequestContext(request, {'places': places})
	t = loader.get_template('index.html')
	return HttpResponse(t.render(c))
	return HttpResponse('d')#render_to_response('index.html', template_context, context_instance = RequestContext(request))
	
	
def geo(request):
	lat = request.GET.get('lat')
	lon = request.GET.get('lon')
	api = foursquare.Api()
	groups =  api.get_venues(geolat = lat, geolong = lon, l = 50)['groups']
	
	
	resp = '<html><body>'
	venues = []
	if len(groups)> 0:
		for venue in groups[0]['venues']:
			
			name = venue['name'].encode('ascii', 'ignore')
			distance = venue['distance']
			address = venue['address'].encode('ascii', 'ignore')
			city = venue['city'].encode('ascii', 'ignore')
			category = None
			try:
				category = venue['primarycategory']
				category = category['fullpathname'].encode('ascii', 'ignore')
			except:
				pass
			f_id = venue['id']
			geolat = venue['geolat']
			geolong = venue['geolong']
			myvenue = {}
			
			place, created = Place.objects.get_or_create(foursquare_id__exact = f_id)
			if created == True:
				place.city = city.lower()
				place.name = name.encode('ascii', 'ignore')
				place.address = address
				place.foursquare_id = f_id
				place.foursquare_category = category
				place.geolat = Decimal(str(geolat))
				place.geolong = Decimal(str(geolong))
				print str(place.geolong)
				place.save()	
			venues.append(place)
		c = RequestContext(request, {'venues': venues})
		t = loader.get_template('geo.html')
		return HttpResponse(t.render(c))
			
			
	print lat
	return HttpResponse(resp + '</body></html>')



def place(request, slug, id):
	place = None
	try:
		place = Place.objects.get(pk = id)
	except:
		return HttpResponseServerError(id)
	c = RequestContext(request, {'place': place})
	t = loader.get_template('place.html')
	return HttpResponse(t.render(c))	
		
	
def mobile_place(request, slug, id):
	place = None
	try:
		place = Place.objects.get(pk = id)
	except:
		return HttpResponseServerError(id)
	c = RequestContext(request, {'place': place})
	t = loader.get_template('mobile_place.html')
	return HttpResponse(t.render(c))	
	
def mobile_place(request, id):
	place = None
	try:
		place = Place.objects.get(pk = id)
	except:
		return HttpResponseServerError(id)
	c = RequestContext(request, {'place': place})
	t = loader.get_template('mobile_map.html')
	return HttpResponse(t.render(c))		
	
	
	