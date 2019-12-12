import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

class MyHandler(FileSystemEventHandler):
    def on_created(self,event):
        dirs = os.listdir(folder_to_track)
        for dir in dirs:
            src=(folder_to_track+"/"+dir)
            dst=(folder_to_dest+"/"+dir)
            os.rename(src, dst)



folder_to_track="C:/Users/Singh/Desktop/Projects"
folder_to_dest="C:/Users/Singh/Desktop/New folder"

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()
print('Oberserver Started')
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
