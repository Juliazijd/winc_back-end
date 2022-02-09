__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
from zipfile import ZipFile


def clean_cache():
    file_path = os.path.join(os.getcwd(), 'cache')
    if (os.path.exists(file_path)):
        file_list = os.listdir(file_path)
        for file in file_list:
            old_file = os.path.join(os.getcwd(), f'cache/{file}')
            os.remove(old_file)
    else:
        os.mkdir(file_path)
    return file_path


def cache_zip(zip_path, dir_path):
    with ZipFile(zip_path, 'r') as zip:
        zip.extractall(dir_path)
    return os.listdir(dir_path)


def cached_files():
    file_list = cache_zip(os.path.join(os.getcwd(), 'data.zip'), clean_cache())
    abs_path_list = []
    for file in file_list:
        file_path = os.path.join('cache/', file)
        abs_path = os.path.abspath(file_path)
        abs_path_list.append(abs_path)
    return abs_path_list


def find_password(list):
    for path in list:
        with open(path, 'r') as file:
            if 'password' in file.read():
                password_file = open(file.name)
                lines = password_file.readlines()
                for line in lines:
                    if 'password' in line:
                        password = line.replace('password:', '')
                        password = password.strip()
                        return password


find_password(cached_files())
