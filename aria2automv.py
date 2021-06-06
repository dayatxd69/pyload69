import os, re, time, shutil, glob

destination = "C:/Users/runneradmin/Documents/GoogleDrive/aria2"

while True:
  rootdir = "C:/Users/runneradmin/Downloads/aria2/"
  regex = re.compile('(.*zip$)|(.*rar$)|(.*mp4$)|(.*mkv$)')
  if not glob.glob(rootdir+"*.aria2"):
    for root, dirs, files in os.walk(rootdir):
      for file in files:
        if regex.match(file):
          shutil.move(root+file, destination)
          print("Moved From", root+file, "to", destination+file)
        else: pass
  else: pass
  time.sleep(30)
  pass
