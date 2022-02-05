__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
from zipfile import ZipFile
import shutil


def clean_cache():
    file_path = os.path.join(os.getcwd(), 'files/cache')
    if (os.path.exists(file_path)):
        shutil.rmtree('files/cache', ignore_errors=True)
        os.mkdir('files/cache')
    else:
        os.mkdir('files/cache')
    return file_path


def cache_zip(zippath, dirpath):
    with ZipFile(zippath, 'r') as zip:
        zip.extractall(dirpath)
        return dirpath


def cached_files():
    fileList = os.listdir(cache_zip(
        '/Users/JULIA/Winc/back-end/files/data.zip',
        clean_cache()))
    pathList = []
    for file in fileList:
        pathList.append(os.path.abspath(f'files/cache/{file}'))
    return pathList


def find_password(list):
    for file in list:
        with open(file, 'r') as file:
            if 'password' in file.read():
                passwordFile = open(file.name)
                lines = passwordFile.readlines()
                for line in lines:
                    if 'password' in line:
                        password = line.replace('password: ', '')
                        return password


find_password(cached_files())
