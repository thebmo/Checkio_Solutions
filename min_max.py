def min(*args, **kwargs):
    key = kwargs.get("key", None)
    min = 100000
    for item in args:
        if item < min:
            min = item
        
    return min


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    max = 0
    for item in args:
        if item > max:
            max = item
    return max


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
