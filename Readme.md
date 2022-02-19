This code finds all the possible states of the 8-Puzzle starting from the given initial state until the goal node is reached
Used the Breath First Search(BFS) to find the path to reach the goal.
Implemented back tracking to find the plan to solve the problem

Libraries required:-
    Numpy

Steps to run the code: -
    Run the command $ python3 proj1_final.py
    
    Enter the initial state row wise
        Enter the value[1]:1
        Enter the value[2]:4
        Enter the value[3]:7
        Enter the value[4]:5
        Enter the value[5]:0
        Enter the value[6]:8
        Enter the value[7]:2
        Enter the value[8]:3
        Enter the value[9]:6
        [[1 4 7]
        [5 0 8]
        [2 3 6]]
        Enter the goal state row wise
        Enter the value[1]:1 
        Enter the value[2]:4
        Enter the value[3]:7
        Enter the value[4]:2
        Enter the value[5]:5
        Enter the value[6]:8
        Enter the value[7]:3
        Enter the value[8]:6
        Enter the value[9]:0
        [[1 4 7]
        [2 5 8]
        [3 6 0]]
    The code will generate 3 text files with the appropriate node data

The following is the output : - 
Start Node
-------------
| 1 | 4 | 7 | 
-------------
| 5 | 0 | 8 | 
-------------
| 2 | 3 | 6 | 
-------------


Step  1
-------------
| 1 | 4 | 7 | 
-------------
| 0 | 5 | 8 | 
-------------
| 2 | 3 | 6 | 
-------------


Step  2
-------------
| 1 | 4 | 7 | 
-------------
| 2 | 5 | 8 | 
-------------
| 0 | 3 | 6 | 
-------------


Step  3
-------------
| 1 | 4 | 7 | 
-------------
| 2 | 5 | 8 | 
-------------
| 3 | 0 | 6 | 
-------------


Achieved Goal Node
-------------
| 1 | 4 | 7 | 
-------------
| 2 | 5 | 8 | 
-------------
| 3 | 6 | 0 | 
-------------
