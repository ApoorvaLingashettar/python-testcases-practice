def check_palindrome(input_string):

    if not isinstance(input_string, str):
        raise Exception ('Type mismatch')

    reverse_string = input_string[::-1]

    if input_string.lower() == reverse_string.lower():
        return True
    return False


if __name__ == '__main__':

    assert check_palindrome('845764') == False
    assert check_palindrome('MadaM') == True
    assert check_palindrome('') == True

    assert check_palindrome('gadag gaDAG') == True
    assert check_palindrome('gadag gaDAG kldfg') == False
    assert check_palindrome('++==++') == True
    assert check_palindrome('&!7!&') == True

    assert check_palindrome('àa') == False

    try:
        check_palindrome([])
    except Exception as e:
        assert str(e) == 'Type mismatch'

    try:
        check_palindrome(-99)
    except Exception as e:
        assert str(e) == 'Type mismatch'



