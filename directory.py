import os
from metadata import clear_meta, change_meta

path = '/Users/saiarvind/Downloads/testMusicFolder/Music/'


def collapse():
   goDown(path, path)
   removeNonAudio(path)

def goDown(path, oldPath):
   for file in os.listdir(path):
      file+="/"
      print("Path " + path +" Old path: " +oldPath + "\n")
      if os.path.isdir(path+file):
         goDown(path+file, path)
   for file in os.listdir(path):
      if(os.path.isdir(path+file)):
         os.rmdir(path+file)
      elif(path != oldPath):
         os.rename(path+file, oldPath+file)
   
def removeNonAudio():
   
   
if __name__ == "__main__":
    collapse()
