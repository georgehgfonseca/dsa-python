# https://www.hackerrank.com/x/library/hackerrank/all/questions/222914
# A limousine service for an airport can transport multiple passengers simultaneously. On the return trip, the driver may pick up more passengers for the next journey to the airport. A map of passenger locations is represented as a square matrix.

# The matrix contains cells with initial values as follows:

# A value ≥ 0 signifies a path.
# A value of 1 indicates a passenger.
# A value of -1 signifies an obstruction.
# Movement rules are:

# The driver starts at (0, 0) and the airport is at (n-1, n-1). Movement towards the airport is either right (→) or down (↓) through valid path cells.
# After reaching (n-1, n-1), the driver returns to (0, 0) by moving left (←) or up (↑) through valid path cells.
# Upon passing through a path cell containing a passenger, the passenger is picked up. The cell then becomes an empty path cell (0).
# If there is no valid route between (0, 0) and (n-1, n-1), no passengers can be collected.
 

# Implement a function that returns the maximum number of passengers that can be collected.

 

# For example, consider the following grid:

# 	 0 1
# 	-1 0
# Start at the top left corner. Move right one, collecting a rider. Move down one to the airport. Cell (1, 0) is blocked, so the return path is the reverse of the path to the airport. All paths have been explored, and 1 rider was collected.

 

# Function Description 

# Complete the function collectMax in the editor with the following parameter(s):

#     int mat[n]:  an array of integers describing the map

 

# Returns:

#     int: the maximum number of riders that can be collected

 

# Constraints

# 1 ≤ n ≤ 100
# −1 ≤ mat[i][j] ≤ 1
 
#
# Complete the 'collectMax' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY mat as parameter.
#
from functools import lru_cache

def collectMax(mat):
    n = len(mat)
    if mat[0][0] == -1 or mat[n-1][n-1] == -1:
        return 0
    
    # Two-path DP: both paths go from (0,0) to (n-1,n-1)
    # Track positions of both paths at step k where x1+y1 = x2+y2 = k
    # Since y1 = k-x1 and y2 = k-x2, we only need (k, x1, x2)
    
    @lru_cache(maxsize=None)
    def dp(k, x1, x2):
        y1 = k - x1
        y2 = k - x2
        
        # Check bounds
        if x1 < 0 or x1 >= n or y1 < 0 or y1 >= n:
            return float("-inf")
        if x2 < 0 or x2 >= n or y2 < 0 or y2 >= n:
            return float("-inf")
        if mat[x1][y1] == -1 or mat[x2][y2] == -1:
            return float("-inf")
        
        # Base case: reached destination
        if k == 2 * (n - 1):
            return mat[n-1][n-1]
        
        # Collect passengers (only count once if both paths are on same cell)
        passengers = mat[x1][y1]
        if x1 != x2 or y1 != y2:
            passengers += mat[x2][y2]
        
        # Try all combinations of moves (right or down for each path)
        max_collected = float("-inf")
        for dx1 in [0, 1]:  # right or down for path 1
            for dx2 in [0, 1]:  # right or down for path 2
                max_collected = max(max_collected, passengers + dp(k + 1, x1 + dx1, x2 + dx2))
        
        return max_collected
    
    result = dp(0, 0, 0)
    return max(0, result)

from functools import cache

def collectMax2(mat):
    # dfs + dp (i, j, trip) -> max passengers
    # pickup passanger, and move to next cell
    n = len(mat)
    
    @cache
    def dfs(i, j, trip):
        if i < 0 or j < 0 or i >= n or j >= n or mat[i][j] == -1:
            return float("-inf")
        
        if i == 0 and j == 0 and trip == 2:
            return 0
        
        if i == n - 1 and j == n - 1 and trip == 1:
            trip = 2
        
        passengers = 0
        backup = mat[i][j]
        if mat[i][j] == 1:
            passengers = 1
            mat[i][j] = 0
                
        bot = float("-inf") if trip == 2 else passengers + dfs(i + 1, j, trip)
        right = float("-inf") if trip == 2 else passengers + dfs(i, j + 1, trip)
        top = float("-inf") if trip == 1 else passengers + dfs(i - 1, j, trip)
        left = float("-inf") if trip == 1 else passengers + dfs(i, j - 1, trip)
        
        if passengers:
            mat[i][j] = backup

        return max(bot, right, top, left)
    
    res = dfs(0, 0, 1)
    return max(0, res)