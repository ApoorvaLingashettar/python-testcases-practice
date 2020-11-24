import unittest

fibs = {
}


def fib(n):

    if not isinstance(n, int):
        raise Exception("Type mismatch")

    if isinstance(n, bool):
        raise Exception ("Inputs cannot be boolean")

    if n < 0:
        raise Exception("Invalid input")

    if n in fibs:
        return fibs[n]

    if n == 1 or n == 0:
        return n

    result = fib(n - 1) + fib(n - 2)
    fibs[n] = result

    return result


if __name__ == "__main__":
    assert fib(1) == 1
    assert fib(6) == 8

    assert fib(0) == 0
    assert fib(74) == 1304969544928657

    try :
        fib(None)
    except Exception as e:
        assert str(e) == 'Type mismatch'

    try :
        fib(-8)
    except Exception as e:
        assert str(e) == 'Invalid input'

    try :
        fib(True)
    except Exception as e:
        assert str(e) == 'Inputs cannot be boolean'



