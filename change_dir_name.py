from fnmatch import fnmatch
import os
import shutil
import re

#root_dir = r"/Users/gxy.../desktop/sp1_3000"

def get_filenames(root_dir):
    files = []
    for file in os.listdir(root_dir):
        files.append(file)
        #print(file)
    return files
'''
def cal_dirname(name):
    result = ['0','0','0','0']
    num = int(re.sub('\D', '', name))
    record = list(str(num // 3))
    result[-1-len(record):-1] = record
    return result
    




def distribute_files():
    root_dir = r"/Users/gxy.../desktop/sp1_3000_2"
    files = get_filenames(root_dir)
    
    files.sort(key=lambda f: int(re.sub('\D', '', f)))
    for i in files:
        src = i
        
        os.rename(src, dst)

    
    files.sort(key=lambda f: int(re.sub('\D', '', f)))
    
    for i in range(0, len(files), increment):
        subfolder = "files_{}_{}".format(i + 1, i + increment)
        new_dir = os.path.join(root_dir, subfolder)
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        for file in files[i:i + increment]:
            file_path = os.path.join(root_dir, file)
            shutil.move(file_path, new_dir)
    '''
def rename_files(files, prefix, start_num=0):
    """Generates the new filename"""
    files = sorted(files,key=lambda f: int(re.sub('\D', '', f)))
    '''
    last_file_num = files[-1][0]
    max_num = max(last_file_num, start_num + len(files))
    num_length = len(str(max_num))
    
    for new_number, (_, file) in enumerate((files), start_num):
        new_name = f"{str(new_number).zfill(4)}"
        yield file, new_name
    '''
    for file in files:
        new_number = int(re.sub('\D', '', file)) // 3 + 1
        new_name = f"{str(new_number).zfill(4)}"
        os.rename('/Users/gxy.../desktop/sequences/00001/'+file, '/Users/gxy.../desktop/sequences/00001/'+new_name)



def move(renames, practice=True):
    for file, new_name in renames:
        new_file = file.with_name(new_name)
        print(f"renaming {file.name} to {new_name}")
        if not practice:
            os.rename(file, new_file)



if __name__ == "__main__":
    prefix = "files"
    files = get_filenames('/Users/gxy.../desktop/sequences/00001')
    renames = rename_files(files, prefix)
    #move(renames, practice=False)









