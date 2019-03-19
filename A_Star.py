import math
class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0
    def __eq__(self, other):
        return self.position == other.position

def a_star(maze, start, end, size):
    nodes_visited = 0
    nodes_memory = 0
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:
        current_node = open_list[0]
        nodes_visited += 1
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node:
            print("nodes in memory: %d" % nodes_memory)
            print("nodes visited: %d" % nodes_visited)
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            print("path size: %d" % len(path))
            print(path[::-1])

        kids = generate_kids(maze, current_node, size)
        for node in kids:
            if node in closed_list:
                continue
            if node in open_list:
                new_g = current_node.g + 1
                if node.g > new_g:
                    node.g = new_g
                    node.parent = current_node
            else:
                node.g = current_node.g + 1
                node.h = heuristica_manhattan(node.position[0], node.position[1], end[0], end[1])
                node.parent = current_node
                open_list.append(node)
            if(nodes_memory < (len(closed_list) + len(open_list))):
                nodes_memory = len(closed_list) + len(open_list)

def heuristica_manhattan(i, j, xF, yF):
    return (abs(xF - i) + abs(yF - j))

def heuristica_reta(i, j, xF, yF):
    return math.sqrt( ((i - xF)**2) + ((j - yF)**2) )

def generate_kids(maze, current, size):
    i = current.position[0]
    j = current.position[1]
    kids = []
    if(i-1 >= 0 and not(i-1 == 3 and j == 5) and (maze[i-1][j] != -2)):
        kids.append(Node(current, (i-1, j)))
    if(j-1 >= 0 and not(i == 2 and j-1 == 2) and (maze[i][j-1] != -2)):
        kids.append(Node(current, (i, j-1)))
    if(i+1 < size and not(i+1 == 4 and j == 4) and (maze[i+1][j] != -2)):
        kids.append(Node(current, (i+1, j)))
    if(j+1 < size and not(i == 1 and j+1 == 3) and (maze[i][j+1] != -2)):
        kids.append(Node(current, (i, j+1)))
    return kids

def main(size):
    maze = []
    l = 0
    for i in range(0, size):
        new = []
        for x in range(0, size):
            new.append(l)
            l += 1
        maze.append(new)

    start = (18, 18)
    end = (26, 26)

    a_star(maze, start, end, size)

if __name__ == '__main__':
    main(30)