import os

if __name__ == '__main__':
    print(os.getcwd())
    metadata = os.stat('ex_mng_file.py')
    print(metadata.st_mtime)

    import time

    print(metadata.st_size)
    print(time.localtime(metadata.st_mtime))

    print(os.getcwd())
    print(os.path.realpath('ex_mng_file.py'))
