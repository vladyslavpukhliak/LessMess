import json
import os
import sys
from GUI import MessageBoxUtils

def load_configuration():
    cwd = sys.executable
    # cwd = 'C:/Users/user/Downloads'
    configuration = cwd + '/' + 'parameters.json'
    with open(configuration, 'r') as config:
        return json.load(config)


def create_folders(data):
    folders = []
    for category_path in data['extension']:
        dir_path = os.path.expanduser(category_path)

        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        folders.append(dir_path)
    return folders, os.path.expanduser(data['track'])


def check_files(files):
    file_count = len(files)
    if file_count > 0:
        MessageBoxUtils.init()
        if MessageBoxUtils.allowed_renaming(file_count):
            for f in files:
                extension = get_extension(f)
                os.rename(f, f + '_duplicate.' + extension)
            organise(folders, track)
            MessageBoxUtils.show_success()

        MessageBoxUtils.destroy()
        


def get_extension(file):
    return file.split('.')[-1].lower()


def organise(folders, track):
    files_to_rename = []
    files = os.listdir(track)
    for filename in files:
        extension = get_extension(filename)
        if extension:
            source = track + '/' + filename

            for path, ext_list in enumerate(data['extension']):
                if extension in data['extension'][ext_list]:
                    new_path = folders[path] + '/' + filename
                    if not os.path.exists(new_path):
                        os.rename(source, new_path)
                    else:
                        files_to_rename.append(source)

    check_files(files_to_rename)


data = load_configuration()
folders, track = create_folders(data)
organise(folders, track)
