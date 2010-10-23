from geniusloci.loc.models import *



def score_like(like):
	place = Place.objects.get(pk = like.place.id)
	place.points = place.points + 1
	print place.name
	place.save()
	
	
def score_likes():
	likes = Like.objects.all()
	for like in likes:
		score_like(like)
	
	
def reset_points():
	places = Place.objects.all()
	for place in places:
		place.points = 0
		place.save()
	pass	
		
if __name__ == '__main__':

	score_likes()