# This class will create two things:
# 1. A directory (for each individual website).
# 2. A text file (for storing scanned results).

import os


def create_dir(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)


def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()