import numpy as np
from collections import deque

visited_list = []

def print_matrix(state):
    counter = 0
    for row in range(0, len(state), 3):
        if counter == 0 :
            print("-------------")
        for element in range(counter, len(state), 3):
            if element <= counter:
                print("|", end=" ")
            print(int(state[element]), "|", end=" ")
        counter = counter +1
        print("\n-------------")

# function to check if the node has already been visited or not
def check_visited(state):
    status = False
    for i in range(len(visited_list)):
        if((state == visited_list[i][0]).all()):
            status = True
            break
    return status

# function to find the location of the blank tile in the node
def blank_tile_loc(state):
    index = np.where(state == 0)
    return index

def ActionMoveLeft(current_node):
    blank_tile_index = blank_tile_loc(current_node)
    i = blank_tile_index[0][0]
    j = blank_tile_index[1][0]
    child_node = np.zeros((3,3))
    if (j!= 0):
        child_node  = np.copy(current_node)
        q = current_node[i][j-1]
        child_node[i][j] = q
        child_node[i][j-1] = 0
        if(check_visited(child_node)):
            status = False
        else:
            status = True
    else:
        status = False
    return status, child_node

def ActionMoveRight(current_node):
    blank_tile_index = blank_tile_loc(current_node)
    i = blank_tile_index[0][0]
    j = blank_tile_index[1][0]
    child_node = np.zeros((3,3))
    if (j!= 2):
        child_node  = np.copy(current_node)
        a = current_node[i][j+1]
        child_node[i][j] = a
        child_node[i][j+1] = 0
        if(check_visited(child_node)):
            status = False
        else:
            status = True
    else:
        status = False
    return status, child_node

def ActionMoveUp(current_node):
    blank_tile_index = blank_tile_loc(current_node)
    i = blank_tile_index[0][0]
    j = blank_tile_index[1][0]
    child_node  = np.copy(current_node)
    if (i!= 0):
        child_node  = np.copy(current_node)
        a = current_node[i-1][j]
        child_node[i][j] = a
        child_node[i-1][j] = 0
        if(check_visited(child_node)):
            status = False
        else:
            status = True
    else:
        status = False
    return status, child_node

def ActionMoveDown(current_node):
    blank_tile_index = blank_tile_loc(current_node)
    i = blank_tile_index[0][0]
    j = blank_tile_index[1][0]
    child_node = np.zeros((3,3))
    if (i<2):
        child_node  = np.copy(current_node)
        a = current_node[i+1][j]
        child_node[i][j] = a
        child_node[i+1][j] = 0
        if(check_visited(child_node)):
            status = False
        else:
            status = True
    else:
        status = False
    return status, child_node

def main():

    print("Enter the initial state row wise")
    start = np.array([[int(x) for x in input(f"Enter the value{[i+1]}:").split()] for i in range(9)])
    start = np.reshape(start, (3,3))
    print(start)
    print("Enter the goal state row wise")
    goal = np.array([[int(x) for x in input(f"Enter the value{[i+1]}:").split()] for i in range(9)])
    goal = np.reshape(goal, (3,3))
    print(goal)
    if((start == goal).all()):
        print("Start and goal location are same")
    else:
    # initializing the node index and parent node index to 1
        node_index_i = 1
        parent_node_index_i = 1
        node_queue = deque([[start, node_index_i, parent_node_index_i]])

        while True:
            # poping the first node in the queue
            a = node_queue.popleft()
            # checking if the node has been visited or not
            if check_visited(a[0]):
                continue
            # if not visited, add it to the visited list and explore
            visited_list.append(a)
            parent_node_index_i = a[1]
            # Exploring the current node
            # The order of exploring is left, up, right, down
            status_left, child_node_l = ActionMoveLeft(a[0])
            status_up, child_node_u = ActionMoveUp(a[0])
            status_right, child_node_r = ActionMoveRight(a[0])
            status_down, child_node_d = ActionMoveDown(a[0])
            # if child node is equal to the goal node, stop the process
            # if child node is not equal to the goal node, add it to the queue
            if status_left:
                if((child_node_l == goal).all()):
                    print("Goal location reached")
                    break
                else:
                    node_index_i += 1
                    node_queue.append([child_node_l, node_index_i, parent_node_index_i])
            
            if status_up:
                if((child_node_u == goal).all()):
                    print("Goal loc,ation reached")
                    break
                else:
                    node_index_i += 1
                    node_queue.append([child_node_u, node_index_i, parent_node_index_i])
            
            if status_right:
                if((child_node_r == goal).all()):
                    print("Goal location reached")
                    break
                else:
                    node_index_i += 1
                    node_queue.append([child_node_r, node_index_i, parent_node_index_i])
            
            if status_down:
                if((child_node_d == goal).all()):
                    print("Goal location reached")
                    break
                else:
                    node_index_i += 1
                    node_queue.append([child_node_d, node_index_i, parent_node_index_i])
        

        # Writing visited nodes in Nodes.txt
        f = open("Nodes.txt", "w+")
        for i in range(len(visited_list)):
            v =  visited_list[i][0].flatten('F')
            for i in range(v.size):
                f.write(str(v[i]))
                f.write(" ")
            f.write("\n")
        f.close()
        # writing node index and parent node index in NodesInfo.txt 
        f = open("NodesInfo.txt", "w+")
        for i in range(len(visited_list)):
            for j in range(1,3,1):
                f.write(str(visited_list[i][j]))
                f.write(" ")
            f.write("\n")
        f.close()
        
        start_rechd = False
        goal_path = [goal]
        parent = visited_list[-1][1]
        while not start_rechd:
            goal_path.append(visited_list[parent-1][0])
            parent = visited_list[parent-1][2]
            if (parent == 1):
                start_rechd = True
                goal_path.append(start)

        # Writing the states from start node to goal node in nodePath.txt
        f = open("nodePath.txt", "w+")
        for i in range(len(goal_path)):
            m = goal_path[len(goal_path)-i-1].flatten('F')
            for j in range(m.size):
                f.write(str(m[j]))
                f.write(" ")
            f.write("\n")

        f.close()

        # Visualizing the output/solution
        fname = 'nodePath.txt'
        data = np.loadtxt(fname)
        if len(data[1]) != 9:
            print("Format of the text file is incorrect, retry ")
        else:
            for i in range(0, len(data)):
                if i == 0:
                    print("Start Node")
                elif i == len(data)-1:
                    print("Achieved Goal Node")
                else:
                    print("Step ",i)
                print_matrix(data[i])
                print()
                print()
        
if __name__ == '__main__':
    main()
