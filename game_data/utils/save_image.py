import os.path
import requests
import shutil


def save_image(url, path):
    if os.path.isfile(path):
        return

    print('Downloading {}'.format(url))
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(path, 'wb') as out_file:
            shutil.copyfileobj(r.raw, out_file)
        del r
