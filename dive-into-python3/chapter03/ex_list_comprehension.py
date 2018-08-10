import glob
import os

if __name__ == '__main__':
    a_list = [1, 9, 8, 4]
    print([elem * 2 for elem in a_list])
    print(a_list)
    a_list = [elem * 2 for elem in a_list]
    print(a_list)
    print('--------------------------------------')

    glob.glob('*.py')
    print([os.path.realpath(f) for f in glob.glob('*.py')])
    print([f for f in glob.glob('*.py') if os.stat(f).st_size > 10])
    print('--------------------------------------')

    metadata = [(f, os.stat(f)) for f in glob.glob('*.py')]
    print(metadata[0])
    metadata_dict = {f: os.stat(f) for f in glob.glob('*.py')}
    print(type(metadata_dict))
    print(list(metadata_dict.keys()))
    print(metadata_dict['ex_list_comprehension.py'].st_size)
    print('--------------------------------------')

    metadata_dict = {f: os.stat(f) for f in glob.glob('*')}
    print('--------------------------------------')

    a_dict = {'a': 1, 'b': 2, 'c': 3}
    print({value: key for key, value in a_dict.items()})
    print('--------------------------------------')

    a_set = set(range(10))
    print(a_set)
    print({x ** 2 for x in a_set})
    print({x for x in a_set if x % 2 == 0})
    print({2 ** x for x in range(10)})
