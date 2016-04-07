import requests
import json
import acoustid

def return_meta(path):
        mbid = None
        info=list(acoustid.match('MZMS6Rw8O0', path))
        if ((len(info) != 0) and (len(info[0]) != 0)):
                mbid=info[0][1]
                title=info[0][2]
                artist=info[0][3]
        print(title)
        album = None
        position = None
        urlhead = "http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key=a0a2dc22c307a2dd5b69051883706a65&mbid="
        urltail = "&format=json"
        if mbid is None:
                return [None, None, None, None]
        json = (requests.get(urlhead + mbid + urltail)).json()	
        if json.get('error'):
                return [artist, None, title, None]
        if ("track" not in json.keys()):
                album = None
                position=None
                return [artist,album,title,position]
        if("album" not in json["track"].keys()):
                album = None
                position=None
                return [artist,album,title,position]
        if("title" not in json["track"]["album"].keys()):
                album = None
        else:
                album = json["track"]["album"]["title"]
        if("@attr" not in json["track"]["album"].keys()):
                position = None
        elif("position" not in json["track"]["album"]['@attr'].keys()):
                position = None
        else:
                position = json["track"]["album"]['@attr']['position']
        return [artist,album,title,position]

