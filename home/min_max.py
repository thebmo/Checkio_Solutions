def min(*args, **kwargs):
    key = kwargs.get("key", None)
    items = sorted(get_items(args), key=key)
    min = items[0]
    if key == int:
        min = int_key(items, min)
    return min

def max(*args, **kwargs):
    key = kwargs.get("key", None) 
    items = sorted(get_items(args), key=key)
    max = items[-1]
    if key == int:
        max = int_key(items, max)
    return max
    
def get_items(args):
    items = []
    if len(args) == 1:
        for arg in args:
            for a in arg:
                items.append(a)
    else:
        for arg in args:
            items.append(arg)
    return items

# I feel like this is a hack but dont know how else to
# handle the float -> int sorting
def int_key(items, num):
    for item in items:
        if int(item) == int(num) and item < num:
            num = item
    return num
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
