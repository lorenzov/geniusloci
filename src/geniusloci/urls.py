from django.conf.urls.defaults import *
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
	(r'', include('facebook_oauth.urls')),
	url(r'^$', 'geniusloci.loc.views.index'),
	
	
	(r'^p/(?P<slug>).*/(?P<id>\d+)/$', 'geniusloci.loc.views.place'),
	
	#mobile site
	(r'^mobile/geo/$', 'geniusloci.loc.views.geo'),
	(r'^mobile/p/(?P<slug>).*/(?P<id>\d+)/$', 'geniusloci.loc.views.mobile_place'),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve',
	        {'document_root': '/home/ubuntu/geniusloci/src/iui/'}),
	
)
