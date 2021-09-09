from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_track):
            extension = filename.split('.')
            if len(extension) > 1:
                file = folder_track + '\\' + filename
                if extension[-1].lower() in PicturesType:
                    new_path = folder_pics + '\\' + filename
                    os.rename(file, new_path)
                if extension[-1].lower() in VideoType:
                    new_path = folder_video + '\\' + filename
                    os.rename(file, new_path)
                if extension[-1].lower() in AudioType:
                    new_path = folder_audio + '\\' + filename
                    os.rename(file, new_path)
                if extension[-1].lower() in insType:
                    new_path = folder_ins + '\\' + filename
                    os.rename(file, new_path)
                if extension[-1].lower() in docType:
                    new_path = folder_docs + '\\' + filename
                    os.rename(file, new_path)
                if extension[-1].lower() in PresentationsType:
                    new_path = folder_docs + '\\' + filename
                    os.rename(file, new_path)


PicturesType = ['jpg', 'png', 'svg', 'tif', 'jpeg', 'tiff',
                'gif', 'bmp', 'dib', 'ico', 'icns', 'bw', 'cdr', 'cmx']
VideoType = ['mp4', 'mov', 'm4v', 'asf', 'avi',
             'wmv', 'm2ts', '3g2', '3gp2', '3gpp', 'mpg', 'mpeg', 'webm']
AudioType = ['mp3', 'wav', 'm4a', 'wma', 'aac', 'au', 'mp2']
insType = ['exe', 'msi', 'zip', 'rar', '7z', 'iso', 'bat',
           'bin', 'apk', 'ipa', 'dmg', 'pkg', 'deb', 'torrent', 'jar', 'tar', 'zipx', 'xar']
docType = ['txt', 'docx', 'doc', 'dot', 'docm', 'dotx', 'dotm', 'odt', 'ott', 'oth', 'odm', 'wpd', 'pdb', 'ini', 'json', 'csv', 'md', 'rtf', 'mdb',
           'accdb', 'pub', 'psd', 'xml', 'xlsx', 'xlw', 'xlt', 'xlsb', 'xlsm', 'xltm', 'ods', 'ots', 'fods', 'sxc', 'stc']
WebDocuments = ['html', 'htm', 'xhtml', 'mht', 'mhtml']
PresentationsType = ['pdf', 'ppt', 'pot', 'pptx', 'pptm', 'potx', 'potm',
                     'odp', 'odg', 'otp', 'fopd', 'sxi', 'sti', 'uop', 'uof', 'cgm', 'key']

folder_track = os.path.expanduser('~\Downloads')
folder_pics = os.path.expanduser('~\Downloads\Pictures')
folder_video = os.path.expanduser('~\Downloads\Video')
folder_audio = os.path.expanduser('~\Downloads\Audio')
folder_ins = os.path.expanduser('~\Downloads\Archives')
folder_docs = os.path.expanduser('~\Downloads\Docs')
folder_Presentations = os.path.expanduser('~\Downloads\Docs\Presentations')

if not os.path.exists(folder_pics):
    os.mkdir(folder_pics)
if not os.path.exists(folder_video):
    os.mkdir(folder_video)
if not os.path.exists(folder_audio):
    os.mkdir(folder_audio)
if not os.path.exists(folder_ins):
    os.mkdir(folder_ins)
if not os.path.exists(folder_docs):
    os.mkdir(folder_docs)
if not os.path.exists(folder_Presentations):
    os.mkdir(folder_Presentations)


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
