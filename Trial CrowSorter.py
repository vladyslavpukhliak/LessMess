from watchdog.observers import Observer
import os
import time
import sys
from datetime import datetime, date, timedelta
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_track):
            extension = filename.split('.')
            if len(extension) > 1:
                file = folder_track + '\\' + filename
                if extension[-1].lower() in picType:
                    new_path = folder_pics + '\\' + filename
                    os.rename(file, new_path)
                if extension[-1].lower() in videoType:
                    new_path = folder_video + '\\' + filename
                    os.rename(file, new_path)
                if extension[-1].lower() in audioType:
                    new_path = folder_audio + '\\' + filename
                    os.rename(file, new_path)
                if extension[-1].lower() in insType:
                    new_path = folder_ins + '\\' + filename
                    os.rename(file, new_path)
                if extension[-1].lower() in docType:
                    new_path = folder_docs + '\\' + filename
                    os.rename(file, new_path)


picType = ['svg', 'tif', 'tiff', 'bmp', 'gif', 'png']
videoType = ['mov', 'm4v', 'asf', 'avi',
             'wmv', 'm2ts', '3g2', '3gp2', '3gpp']
audioType = ['wav']
insType = ['iso', 'bat', 'bin', 'exe']
docType = ['pdf', 'md', 'rtf', 'accdb',
           'pptx', 'xlsx', 'psd', 'html', 'htm' 'xml']

if not os.path.exists(os.path.expanduser('~\Downloads\Pictures')):
    os.mkdir(os.path.expanduser('~\Downloads\Pictures'))
if not os.path.exists(os.path.expanduser('~\Downloads\Video')):
    os.mkdir(os.path.expanduser('~\Downloads\Video'))
if not os.path.exists(os.path.expanduser('~\Downloads\Audio')):
    os.mkdir(os.path.expanduser('~\Downloads\Audio'))
if not os.path.exists(os.path.expanduser('~\Downloads\Installers')):
    os.mkdir(os.path.expanduser('~\Downloads\Installers'))
if not os.path.exists(os.path.expanduser('~\Downloads\Docs')):
    os.mkdir(os.path.expanduser('~\Downloads\Docs'))


d1 = datetime.strptime(datetime.fromtimestamp(
    os.path.getctime(sys.argv[0])).strftime("%d.%m.%Y"), "%d.%m.%Y")
d2 = datetime.strptime(date.today().strftime("%d.%m.%Y"), "%d.%m.%Y")
d3 = d1 + timedelta(days=30)

print(f"The program expires in {(d3-d2).days} days")

if ((d2-d1).days >= 30):
    os.remove(sys.argv[0])
    exit()

folder_track = os.path.expanduser('~\Downloads')
folder_pics = os.path.expanduser('~\Downloads\Pictures')
folder_video = os.path.expanduser('~\Downloads\Video')
folder_audio = os.path.expanduser('~\Downloads\Audio')
folder_ins = os.path.expanduser('~\Downloads\Installers')
folder_docs = os.path.expanduser('~\Downloads\Docs')

handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
