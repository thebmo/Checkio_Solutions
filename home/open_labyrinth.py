# get current position
# check for nodes at CP
# for each node, proceed down path until dead end or next node
#    if next node, check if in visited spots
#        if yes, skip it
#        if no, take it (or maybe throw in temp list choice) and update visited spots
#    repeat

def main():
    GRAPH = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    initial = (1,1)
    curr = initial
    goal = (10, 10)
    visited = [curr]
    dirs = {
        (-1, 0): 'N',
        (1, 0): 'S',
        (0, -1): 'W',
        (0, 1): 'E'
        }
    
    print '\n'
    
    # prints the graph
    for line in GRAPH:
        row = ''
        for i in line:
            row += (str(i) + ' ')
        print row
    
    print '\ninitial:', initial
    print '   goal:', goal
    print 'Is Node?:', is_node(curr, visited, GRAPH, dirs)
    
    # master loop
    while(True):
        starting_nodes = node_test(curr, GRAPH, visited, dirs)
        print 'starting nodes:', starting_nodes
        
        # builds a list of possible paths
        temp_paths = []
        for node in starting_nodes:
            path = []
            next = node
            
            while(True):
                next_list = node_test(next, GRAPH, visited, dirs)
                if len(next_list) == 1:
                    next = next_list[0]
                    path.append(next)
                else:
                    break
            temp_paths.append(path)
            
        print 'temp paths:', temp_paths
        print 'visited:', visited
        
        raw_input('Press Enter\n')
        
        if curr == goal:
            print 'Goal Reached!'
        
    
# returns the charecter of the direction traveled
def get_direction(dirs, curr, next):
    return dirs[(next[0] - curr [0], next[1] - curr [1])]
        

# Tests a coord to see if it open nodes next to it
def node_test(curr, GRAPH, visited, dirs):
    nodes = []
    temp_visited = [v for v in visited]
    temp_visited.append(curr)
    x = curr[0]
    y = curr[1]
    
    for d in dirs:
        if GRAPH[x+d[0]][y+d[1]] == 0 and (x+d[0], y+d[1]) not in temp_visited: 
                nodes.append((x+d[0], y+d[1]))
                temp_visited.append(nodes[-1])
    return nodes


# returns true if POS is a node
def is_node(curr, visited, GRAPH, dirs):
    x = curr[0]
    y = curr[1]
    nodes = 0
    for d in dirs:
        if GRAPH[x+d[0]][y+d[1]] == 0:
            nodes+=1
            # nodes.append((x+d[0], y+d[1]))
    
    return True if nodes > 2 or curr == (1, 1) else False
    
if __name__ == '__main__':
  main()