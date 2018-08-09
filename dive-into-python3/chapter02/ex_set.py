if __name__ == '__main__':
    a_set = {1}
    print(a_set)
    print(type(a_set))
    a_set = {1, 2}
    print(a_set)

    a_list = ['a', 'b', 'c']
    a_set = set(a_list)
    print(a_set)

    a_set = set()
    print(type(a_set))
    print(len(a_set))
    # a_set = {} -> dictionary

    print('--------------------------------------')

    # 집합에 추가
    a_set.add(1)
    a_set.add(1)
    a_set.add(2)
    print(a_set)
    print(len(a_set))

    a_set.update({2, 4, 6})
    print(a_set)
    # a_set.update({2}, {4, 6}) 가능
    a_set.update([10, 20, 30])
    print(a_set)

    print('--------------------------------------')

    # 집합에서 삭제
    a_set.discard(10)
    print(a_set)
    a_set.remove(20)
    print(a_set)

    print('--------------------------------------')

    # 집합 연산
    a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}
    print(30 in a_set)
    print(31 in a_set)
    b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
    print(a_set.union(b_set))
    print(a_set.intersection(b_set))
    print(a_set.difference(b_set))
    print(a_set.symmetric_difference(b_set))
    print(b_set.symmetric_difference(a_set) == a_set.symmetric_difference(b_set))
    a_set = {1, 2, 3}
    b_set = {1, 2, 3, 4}
    print(a_set.issubset(b_set))
    print(b_set.issuperset(a_set))
    a_set.add(5)
    print(a_set.issubset(b_set))
    print(b_set.issuperset(a_set))
