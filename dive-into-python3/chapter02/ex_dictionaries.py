if __name__ == '__main__':
    a_dict = {'server': 'db.diveintopython3.org', 'database': 'mysql'}  # 1
    print(a_dict)
    print(a_dict['server'])
    print(a_dict['database'])

    import os

    print(os.getcwd())  # 1
    ## c:\Users\pilgrim\diveintopython3\examples
    metadata = os.stat('feed.xml')  # 2
    print(metadata.st_mtime)  # 3
    ## 1247520344.9537716
    import time  # 4

    time.localtime(metadata.st_mtime)  # 5
    time.struct_time(tm_year=2009, tm_mon=7, tm_mday=13, tm_hour=17,
                     tm_min=25, tm_sec=44, tm_wday=0, tm_yday=194, tm_isdst=1)
    # 데이터 변경
    a_dict['database'] = 'blog'
    print(a_dict)

    SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
                1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}
    print(SUFFIXES[1000][0])

