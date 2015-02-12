class Friends(object):
    
    def __init__(self, connections):
        self.connections = list(connections)


    def add(self, connection):
        if connection in self.connections:
            return False
        self.connections.append(connection)
        return True


    def remove(self, connection):
        if connection in self.connections:
            self.connections.remove(connection)
            return True
        return False

        
    def names(self):
        names = []
        for c in self.connections:
            for n in c:
                if n not in set(names):
                    names.append(n)
                    
        return set(names)


    def connected(self, name):
        connected = []
        for c in self.connections:
            if name in set(c):
                for n in c:
                    if n != name and n not in set(connected):
                        connected.append(n)
        
        return set(connected)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
