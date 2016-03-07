import os
from metadata import clear_meta, change_meta

path = '/Users/saiarvind/Downloads/testMusicFolder/Music/'


def collapse():
   print("called collapse!\n")
   goDown(path, path)

def goDown(path, oldPath):
   for file in os.listdir(path):
      file+="/"
      print("Path " + path +" Old path: " +oldPath + "\n")
      if os.path.isdir(path+file):
         print("going down")
         goDown(path+file, path)
      if(path != oldPath):
       	 for file in os.listdir(path+file):
            os.rename(path+file, oldPath+file)
   
        

        
#def __main__():
#    print("called main")
#    collapse()


if __name__ == "__main__":
    print("main\n")
    collapse()