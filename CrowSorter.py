from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
import json


configuration = open('parameters.json')
data = json.load(configuration)

folders = []
for dirPath in data['path']:
    folders.append(os.path.expanduser(data['path'][dirPath]))

track = folders[0]


for folder in data['path']:
    if not os.path.exists(os.path.expanduser(data['path'][folder])):
        os.mkdir(os.path.expanduser(data['path'][folder]))


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(track):
            extension = filename.split('.')
            if len(extension) > 1:
                file = track + '\\' + filename

                for tuple in enumerate(data['extension']):
                        if extension[-1].lower() in data['extension'][tuple[1]]:
                            new_path=folders[tuple[0] + 1] + '\\' + filename
                            time.sleep(3)
                            os.rename(file, new_path)



handle = Handler()
observer = Observer()
observer.schedule(handle, track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()