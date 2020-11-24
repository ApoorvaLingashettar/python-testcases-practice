def get_second_high(input_list):
    if not isinstance(input_list, list):
        raise Exception('Invalid Input')

    try:
        list(map(int, input_list))
    except ValueError:
        raise Exception('input list has inappropriate values')

    if len(input_list) < 2:
        raise Exception('Invalid length')

    max_num = max(input_list)
    input_list.sort(reverse=True)
    print(input_list)
    second_high = -8457649867
    for num_1 in input_list:
        if num_1 < max_num:
            second_high = num_1
            break

    if second_high == -8457649867:
        raise Exception('No second high number')

    return second_high


if __name__ == '__main__':
    assert get_second_high([1, 5, 7, 3, 6]) == 6
    assert get_second_high([4, 4, 0]) == 0

    try:
        get_second_high([-8, -8, -8, -8])
    except Exception as e:
        assert str(e) == 'No second high number'

    try:
        print('before try')
        get_second_high([]) and print('after try')
        print('test 1')
    except Exception as e:
        assert str(e) == 'Invalid length'

    try:
        get_second_high([2])
    except Exception as e:
        assert str(e) == 'Invalid length'



    try:
        get_second_high([4, 4])
    except Exception as e:
        assert str(e) == 'No second high number'

    try:
        get_second_high('string')
    except Exception as e:
        assert str(e) == 'Invalid Input'

    try:
        get_second_high(True)
    except Exception as e:
        assert str(e) == 'Invalid Input'

    try:
        get_second_high([2, 'q', None])
    except Exception as e:
        assert str(e) == 'input list has inappropriate values'
