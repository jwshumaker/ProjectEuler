'''
Created on Apr 15, 2014

@author: JWShumaker

ProjectEuler.net
Problem ID 15
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down,
 there are exactly 6 routes to the bottom right corner.
 
How many such routes are there through a 20x20 grid?

Solution:
A blind search takes much too long!

Instead, working a few examples yields a result based on combinations.  In fact, for
 for any NxN graph, finding (N*2) choose (N) will count the number of paths.  This is
 due to the rectilinear nature of all possible paths.  Since we can only move right
 or down, all solutions have the same length... N*2.  You can regard any
 valid path as a sequence of R's and D's.  However, since the number of R's and D's is
 fixed, you can simplify the problem to counting the number of ways to distribute a
 number N of R's through N*2 slots... the placement of the D's is then forced.  Hence,
 N*2 choose N is our solution.
'''

# A grid class.
class Grid:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        
    def GetChildren(self, path):
        children = []
        
        if path[1] < self.width - 1:
            children.append((path[0] + 'R', path[1] + 1, path[2]))
        
        if path[2] < self.height - 1:
            children.append((path[0] + 'D', path[1], path[2] + 1))
    
        return children
    
# The search algorithm.
def PathCount(width, height):
    search_state = []
    number_of_paths = 0
    grid_to_search = Grid(width, height)
    #print('current_path', current_path)
    # Prime the search state with our initial state.
    search_state.append(('', 0, 0))
    #print('search_state', search_state)
    
    # Keep searching while we have paths in our search state.
    while search_state:
        new_children = grid_to_search.GetChildren(search_state.pop())
        #print('temp_path', temp_path)
        #print('new_children', new_children)
        # Add the new children to our search_state.
        while new_children:
            new_child = new_children.pop()
            #print('new_child', new_child)
            if new_child[1] == width - 1 and new_child[2] == height - 1:
                number_of_paths += 1
            else:     
                search_state.append(new_child)
                
    return number_of_paths
        
        
        
        

#my_grid = Grid(3, 3)
#print(my_grid.GetChildren(('', 0, 0)))


# Our necessary function call.
print(PathCount(8,8))














