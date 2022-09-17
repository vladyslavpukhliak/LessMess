import os
import sys
import json


cwd = os.path.dirname(sys.executable)
configuration = os.path.join(cwd, 'parameters.json')
data = json.load(open(configuration))

folders = []
for dirPath in data['path']:
    path = os.path.expanduser(data['path'][dirPath])

    if not os.path.exists(path):
        os.mkdir(path)
    folders.append(path)

track = folders[0]


def handle():
    for filename in os.listdir(track):
        extension = filename.split('.')
        if len(extension) > 1:
            file = track + '/' + filename

            for tuple in enumerate(data['extension']):
                if extension[-1].lower() in data['extension'][tuple[1]]:
                    new_path = folders[tuple[0] + 1] + '/' + filename
                    os.rename(file, new_path)


handle()
# configuration.close()