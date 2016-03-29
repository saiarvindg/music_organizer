import eyed3

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