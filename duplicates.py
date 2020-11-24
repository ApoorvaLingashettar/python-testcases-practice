from collections import Counter


def get_dupes(input_list):
    if not isinstance(input_list, list):
        raise Exception('In correct input format')

    if len(input_list) < 1:
        raise Exception('input list cannot be empty')

    try:
        map(int, input_list)
    except ValueError:
        raise Exception('invalid input type')

    dupes = []
    c = Counter(input_list)
    for k, v in c.items():
        if v > 1:
            dupes.append(k)

    return dupes


if __name__ == '__main__':
    assert get_dupes([1, 4, 6, 3, 5, 6, 7]) == [6]
    assert get_dupes([2, 3, 5, 6]) == []
    assert get_dupes([6, -6]) == []
    assert get_dupes([1]) == []
    assert get_dupes([0, 0, 0, 0, 0, 7, 7]) == [0, 7]

    try:
        get_dupes([])
    except Exception as e:
        assert str(e) == 'input list cannot be empty'

    try:
        get_dupes(['a', 'f', 'g'])
    except Exception as e:
        assert str(e) == 'In correct input format'

    try:
        get_dupes([None, None, None])
    except Exception as e:
        assert str(e) == 'In correct input format'

    try:
        get_dupes([True, False])
    except Exception as e:
        assert str(e) == 'In correct input format'

    try:
        get_dupes('u')
    except Exception as e:
        assert str(e) == 'In correct input format'
