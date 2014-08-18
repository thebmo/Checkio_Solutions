def checkio(data):
    if len(data) > 1:
        data[0]+=data.pop()
        return checkio(data)
    return data.pop()
    
assert checkio([1]) == 1, 'single item'
assert checkio([1,2,3]) == 6, 'second'
assert checkio([5,6,7]) == 18, 'third'