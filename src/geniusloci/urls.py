from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from loc.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^geniusloci/', include('geniusloci.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
	
	(r'^$', 'geniusloci.loc.views.index'),
	
	(r'^logout/$', 'geniusloci.loc.views.logout_view'),
	(r'^p/(?P<slug>).*/(?P<id>\d+)/$', 'geniusloci.loc.views.place'),
	(r'^search/$', 'geniusloci.loc.views.search'),
	(r'^home/$', 'geniusloci.loc.views.mobile_home'),
	(r'^locate/$', 'geniusloci.loc.views.locate'),
	(r'^services/like/(?P<id>\d+)/$', 'geniusloci.loc.views.services_like'),
	(r'^services/mobile/like/(?P<id>\d+)/$', 'geniusloci.loc.views.services_mobile_like'),
	(r'^services/mobile/tip/(?P<id>\d+)/$', 'geniusloci.loc.views.services_mobile_tip'),
	(r'^geolocate/$',  direct_to_template, {'template': 'geolocate.html'}),
	(r'^near_me/$', 'geniusloci.loc.views.near_me'),
	(r'^login/$', 'geniusloci.loc.views.login'),
	#mobile site
	(r'^mobile/geo/$', 'geniusloci.loc.views.geo'),
	(r'^mobile/map/(?P<id>\d+)/$', 'geniusloci.loc.views.mobile_map'),
	(r'^mobile/p/(?P<slug>).*/(?P<id>\d+)/$', 'geniusloci.loc.views.mobile_place'),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve',
	        {'document_root': '/home/ubuntu/geniusloci/src/iui/'}),
			(r'^xd_receiver\.html$', direct_to_template, {'template': 'xd_receiver.htm'}),
	
)
