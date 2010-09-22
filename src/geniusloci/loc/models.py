from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.


class Place(models.Model):
	name = models.CharField(max_length = 255)
	foursquare_id = models.IntegerField(blank = True, db_index = True, null = True)
	address = models.CharField(max_length = 255)
	geolong = models.DecimalField('longitude', max_digits=13, decimal_places=10, blank=True, null=True, db_index = True)
	geolat = models.DecimalField('latitude', max_digits=13, decimal_places=10, blank=True, null=True, db_index = True)
	city = models.CharField(max_length = 255, blank = True)
	foursquare_category = models.CharField(max_length = 255, blank = True, null = True)
	validated = models.BooleanField(default = False)
	
	def slug(self):
		if self.city != None:
			return slugify(self.city + ' ' +self.name)
		else:
			return slugify(self.name)
class FacebookUser(models.Model):
	facebook_id = models.CharField(max_length=100, unique=True)
	contrib_user = models.OneToOneField(User)
	contrib_password = models.CharField(max_length=100)

class UserProfile(models.Model):
	user = models.ForeignKey(User, unique = True, db_index = True)


class FacebookSessionError(Exception):   
	def __init__(self, error_type, message):
        self.message = message
        self.type = error_type
    def get_message(self): 
        return self.message
    def get_type(self):
        return self.type
    def __unicode__(self):
        return u'%s: "%s"' % (self.type, self.message)

class FacebookSession(models.Model):

				    access_token = models.CharField(max_length=103, unique=True)
				    expires = models.IntegerField(null=True)

				    user = models.ForeignKey(User, null=True)
				    uid = models.BigIntegerField(unique=True, null=True)

				    class Meta:
				        unique_together = (('user', 'uid'), ('access_token', 'expires'))

				    def query(self, object_id, connection_type=None, metadata=False):
				        import urllib
				        import simplejson

				        url = 'https://graph.facebook.com/%s' % (object_id)
				        if connection_type:
				            url += '/%s' % (connection_type)

				        params = {'access_token': self.access_token}
				        if metadata:
				            params['metadata'] = 1

				        url += '?' + urllib.urlencode(params)
				        response = simplejson.load(urllib.urlopen(url))
				        if 'error' in response:
				            error = response['error']
				            raise FacebookSessionError(error['type'], error['message'])
				        return response
	