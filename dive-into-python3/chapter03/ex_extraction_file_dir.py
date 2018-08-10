import os

if __name__ == '__main__':
    print('--------------------------------------')
    print(os.path.join('E:/02.Workspace-personal/learning-python/dive-into-python3/chapter01', 'humansize.py'))
    print(os.path.expanduser('~'))
    print(os.path.join(os.path.expanduser('~'), 'diveintopython3', 'examples', 'humansize.py'))
    print('--------------------------------------')

    pathname = '/Users/pilgrim/diveintopython3/examples/humansize.py'
    print(os.path.split(pathname))
    print('--------------------------------------')

    (dirname, filename) = os.path.split(pathname)
    print(dirname)
    print(filename)
    print('--------------------------------------')

    (shortname, extension) = os.path.splitext(filename)
    print(shortname)
    print(extension)
    print('--------------------------------------')

    os.chdir('E:/02.Workspace-personal/learning-python/dive-into-python3/chapter02/')
    import glob

    print(glob.glob('*.py'))
    print(glob.glob('ex_*.py'))
