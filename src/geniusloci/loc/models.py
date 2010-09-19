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
	
	def slug(self):
		if self.city != None:
			return slugify(self.city + ' ' +self.name)
		else:
			return slugify(self.name)
	