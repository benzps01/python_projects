'''
This is a simple implementation in python 
where we take an input of values and check whether the files exists 
and then copy it to a new path. Then it opens the destination folder
'''

import os
import shutil

dir_path = os.path.dirname("H:/")

file_name = ["file_search.py"]

for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file in file_name:
            src = root+'/'+str(file)
            dst = 'D:/Github/python_projects/'
            shutil.copy(src, dst)
os.startfile(dst)
            