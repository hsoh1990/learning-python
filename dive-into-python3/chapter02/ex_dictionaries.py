if __name__ == '__main__':
    a_dict = {'server': 'db.diveintopython3.org', 'database': 'mysql'}  # 1
    print(a_dict)
    print(a_dict['server'])
    print(a_dict['database'])

    print('--------------------------------------')
    # 데이터 변경
    a_dict['database'] = 'blog'
    print(a_dict)

    SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
                1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}
    print(SUFFIXES[1000][0])

