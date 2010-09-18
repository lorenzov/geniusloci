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




def index(request):
	c = RequestContext(request, {'test': 'test'})
	t = loader.get_template('index.html')
	return HttpResponse(t.render(c))
	return HttpResponse('d')#render_to_response('index.html', template_context, context_instance = RequestContext(request))
	
	
def geo(request):
	lat = request.GET.get('lat')
	lon = request.GET.get('lon')
	print lat
	return HttpResponse(str(lat) + ' ' + str(lon))
	
	
	
	