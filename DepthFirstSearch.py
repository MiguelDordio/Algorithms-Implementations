class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.visited = 0

    def __eq__(self, other):
        return self.position == other.position


def dfs(maze, start, end, size):
    stack = []
    path = []
    nodes_visited = 0
    nodes_memory = 0
    start_node = Node(None, start)
    end_node = Node(None, end)

    stack.append(start_node)

    while (len(stack) != 0):
        current_node = stack.pop()
        nodes_visited += 1
        if (current_node == end_node):
            print("nodes in memory: %d" % nodes_memory)
            print("nodes visited: %d" % nodes_visited)
            print("path size: %d" % len(path))
            path.append(current_node)
            for i in path:
                print(i.position)

            break
        if (current_node.visited != 1):
            maze[current_node.position[0]][current_node.position[1]].visited = 1
            path.append(current_node)
            kids = generate_kids(maze, current_node, size)
            for k in range(len(kids)):
                stack.append(kids.pop())
                if(len(stack) > nodes_memory):
                    nodes_memory = len(stack)


def generate_kids(maze, current, size):
    i = current.position[0]
    j = current.position[1]
    kids = []
    if (i - 1 >= 0 and not (i - 1 == 3 and j == 5) and (maze[i - 1][j].visited != 1)):
        kids.append(Node(current, (i - 1, j)))
    if (j - 1 >= 0 and not (i == 2 and j - 1 == 2) and (maze[i][j - 1].visited != 1)):
        kids.append(Node(current, (i, j - 1)))
    if (i + 1 < size and not (i + 1 == 4 and j == 4) and (maze[i + 1][j].visited != 1)):
        kids.append(Node(current, (i + 1, j)))
    if (j + 1 < size and not (i == 1 and j + 1 == 3) and (maze[i][j + 1].visited != 1)):
        kids.append(Node(current, (i, j + 1)))
    return kids


def main(size):
    maze = []
    for i in range(0, size):
        new = []
        for j in range(0, size):
            new.append(Node(Node, (i, j)))
        maze.append(new)

    start = (18, 18)
    end = (26, 26)
    dfs(maze, start, end, size)

if __name__ == '__main__':
    main(30)








