from django.conf import settings
from django.contrib.auth import models as auth_models
from django.contrib.auth import authenticate as super_authenticate
import cgi
import urllib
import simplejson 
import md5

from music.discotheque import models

class FacebookBackend:
    
    def authenticate(self, token=None, request = None):

        facebook_session = models.FacebookSession.objects.get(
            access_token=token,
        )

        profile = facebook_session.query('me')
        password = md5.new(settings.API_KEY + '_user' + settings.FACEBOOK_APPLICATION_SECRET).hexdigest()    
        try:
            user = auth_models.User.objects.get(username=profile['id'])
        except auth_models.User.DoesNotExist, e:
            user = auth_models.User.objects.create_user(profile['id'], '', password)
   
        user.email = profile['email']
        user.first_name = profile['first_name']
        user.last_name = profile['last_name']
        user.save()

        try:
            models.FacebookSession.objects.get(uid=profile['id']).delete()
        except models.FacebookSession.DoesNotExist, e:
            pass

        facebook_session.uid = profile['id']
        facebook_session.user = user
        facebook_session.save()
        #user2 = super_authenticate(username = profile['id'], password  = password)
        
        return user
   
    def get_user(self, user_id):

        try:
            return auth_models.User.objects.get(pk=user_id)
        except auth_models.User.DoesNotExist:
            return None