from fnmatch import fnmatch
import os
import shutil
import re

#root_dir = r"/Users/gxy.../desktop/sp1_3000"

def get_filenames(root_dir):
    pattern = '*.jpg'
    files = []
    for file in os.listdir(root_dir):
        if fnmatch(file, pattern):
            files.append(file)
    return files


def distribute_files():
    root_dir = r"/Users/gxy.../desktop/sp1_3000_2"
    files = get_filenames(root_dir)
    increment = 3

    #sorted(files, key = lambda x: int(''.join([i for i in x if i.isdigit()])))
    files.sort(key=lambda f: int(re.sub('\D', '', f)))
    
    for i in range(0, len(files), increment):
        subfolder = "files{}".format(i + 1)
        new_dir = os.path.join(root_dir, subfolder)
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        for file in files[i:i + increment]:
            file_path = os.path.join(root_dir, file)
            shutil.move(file_path, new_dir)
    

if __name__ == "__main__":
    distribute_files()









