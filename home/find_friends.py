def check_connection(network, first, second):
    matches = [first]
    matches_found = True
    while(matches_found):
        matches_found = False
        for net in network:
            temp = net.split('-')
            if temp[0] in matches and temp[1] not in matches:
                matches.append(temp[1])
                matches_found = True
            elif temp[1] in matches and temp[0] not in matches:
                matches.append(temp[0])
                matches_found = True
    return second in matches


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
