if __name__ == '__main__':
    print('--------------------------------------')

    query = 'user=pilgrim&database=master&password=PapayaWhip'
    a_list = query.split('&')
    print(a_list)
    print('--------------------------------------')

    a_list_of_lists = [v.split('=', 1) for v in a_list if '=' in v]
    print(a_list_of_lists)
    a_dict = dict(a_list_of_lists)
    print(a_dict)
    print('--------------------------------------')

    a_string = 'My alphabet starts where your alphabet ends.'
    print(a_string[3:11])
    print(a_string[3:-3])
    print(a_string[0:2])
    print(a_string[:18])
    print(a_string[18:])
