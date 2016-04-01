import requests
import json

def return_meta(mbid):
	urlhead = "http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key=a0a2dc22c307a2dd5b69051883706a65&mbid="
	urltail = "&format=json"

	json = (requests.get(urlhead + mbid + urltail)).json()
	
	if json.get('error'):
		return [None, None, None, None]
	else:
		return [json['track']['name'],json['track']['artist']['name'],json['track']['album']['title'],json['track']['album']['@attr']['position']]
	pass