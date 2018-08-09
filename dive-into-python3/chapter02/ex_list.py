if __name__ == '__main__':
    a_list = ['a', 'b', 'mpilgrim', 'z', 'example']
    # list 값 가져오기
    print(a_list)
    print(a_list[:3])
    print('--------------------------------------')
    # 아이템 추가하기
    a_list = a_list + [2.0, 3]
    print(a_list)
    a_list.append(True)
    print(a_list)
    a_list.extend(['four', 'Ω'])
    print(a_list)
    a_list.insert(0, 'Ω')
    print(a_list)
    print('--------------------------------------')
    # append, extend 차이
    b_list = ['a', 'b', 'c']
    b_list.extend(['d', 'e', 'f'])
    print(b_list)
    print(len(b_list))
    print(b_list[-1])
    b_list.append(['g', 'h', 'a'])
    print(b_list)
    print(len(b_list))
    print(b_list[-1])
    print('--------------------------------------')
    # 리스트 검색
    print(b_list.count('a'))
    print('a' in b_list)
    print(b_list.index('c'))
    print('--------------------------------------')
    # 리스트 삭제
    print(b_list)
    del b_list[1]
    print(b_list)
    b_list.remove('f')
    print(b_list)
    print(b_list.pop(0))
    print(b_list)

