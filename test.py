# coding: utf8

import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

 
class MonHandler(FileSystemEventHandler):
	def on_modified(self, event):
		print("Ah, le fichier %s a ete modifie" % event.src_path)


observer = Observer()

observer.schedule(MonHandler(), path='/Users/fthome/Desktop/PackPMI_temps', recursive=True)
observer.start()

try:
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	observer.stop()
observer.join()