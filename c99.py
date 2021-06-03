import os
import time
base_path = '/Users/ADMIN/New folder (2)'

def remove_files(dir_path, n):
    all_files = os.listdir(dir_path)
    now = time.time()
    n_days = n * 86400
    for f in all_files:
        file_path = os.path.join(dir_path, f)
        if os.path.isfile(file_path):
            continue
        if os.stat(file_path).st_mtime < now - n_days:
            os.remove(file_path)
            print("Your file is deleted by harish's code! ", f)

remove_files(base_path, 30)
