#!/usr/bin/python3

import os
import shutil

source_dir = "scripts/"
destination_dir = "/usr/local/bin"

for root,dirs,files in os.walk(source_dir):
    for filename in files:
        source_path = os.path.join(root,filename)
        destination_path = os.path.join(destination_dir,filename)
        extension = os.path.splitext(filename)[1][1:]
        if extension != 'md':
            try:
                shutil.copy(source_path,destination_path)
                print("Files copied successfully to /usr/local/bin/")
            except OSError as e:
                if e.errno == 13:
                    print("Please try running as sudo")
                else:
                    print(e)
        