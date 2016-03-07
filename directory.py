import os
from metadata import clear_meta, change_meta

def collapse():
   goDown(path, path)

def goDown(path, oldPath):
   for file in os.listdir(path):
      if os.path.isdir(file):
         goDown(path+file, path)
   for file in os.listdir(path):
      os.rename(path+ffile, oldPath+file)
        
