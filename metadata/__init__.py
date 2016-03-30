import eyed3
import requests
import json
import acoustid
from acoustid import match
data = match("MZMS6Rw8O0", "MoralOfTheStory.mp3")



def clear_meta_MP3(file):
	audiofile = eyed3.load(file)
	audiofile.tag.artist = u""
	audiofile.tag.album = u""
	audiofile.tag.album_artist = u""
	audiofile.tag.title = u""
	audiofile.tag.track_num = 0

	audiofile.tag.save()
	print("clear_meta > " + file)
	pass

def clear_meta_MP3(file, artist, album, album_artist, title, track_num):
	audiofile = eyed3.load(file)
	audiofile.tag.artist = artist
	audiofile.tag.album = album
	audiofile.tag.album_artist = album_artist
	audiofile.tag.title = title
	audiofile.tag.track_num = track_num

	audiofile.tag.save()
	print("Updated MP3 Tags > " + file)
	pass	
	
def change_meta_MP3(file):
	print("change_meta > " + file)
	pass
	
def return_meta(id):
	urlhead = "http://musicbrainz.org/ws/2/release/"
	urltail = "?inc=artist-credits&fmt=json"

	return [json['title'], json['artist-credit'][0]['name'], "album", "track_num"]
	pass
	
	
def find_id(file):

	pass