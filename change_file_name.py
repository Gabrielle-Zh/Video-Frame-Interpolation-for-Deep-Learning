from fnmatch import fnmatch
import os
import re

#root_dir = r"/Users/gxy.../desktop/sp1_3000"

def get_dirnames(root_dir):
    dirs = []
    for dir in os.listdir(root_dir):
        dirs.append(dir)
    return dirs

def modify_name(root_path,dirs):
    for dir in dirs:
        files = os.listdir(root_path + '/'+dir)
        files = sorted(files,key=lambda f: int(re.sub('\D', '', f)))
        for file in files:
            src =f"{dir}/{file}"  # foldername/filename, if .py file is outside folder
            dst = 'im' + str(files.index(file)+1) + '.jpg'
            dst =f"{dir}/{dst}"
            os.rename(root_path + '/' +src, root_path + '/' +dst)


if __name__ == "__main__":
    root_path = '/Users/gxy.../desktop/sequences/00001'
    dirs = get_dirnames(root_path)
    modify_name(root_path,dirs)
    #move(renames, practice=False)

