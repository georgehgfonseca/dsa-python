"""

63. Unique Paths II

You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.


Example 1:

Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.

-----

 [[0,0,0],
  [0,1,0],
  [0,0,0]]

"""

# [[1]] -> 0
# [[0, 0, 0]] -> 1
# dfs(0, 0) 0+1 = 1
#   dfs(1, 0) 0
#   dfs(0, 1) 0+1 = 1
#     dfs(1, 1) 0
#     dfs(0, 2) 1
# [[0, 0, 0]] -> 0

# [[0, 0, 0], 
#  [0, 0, 0]] -> 3
# dfs(0, 0) 1+2 = 3
#   dfs(1, 0) 0+1 = 1
#     dfs(2, 0) 0
#     dfs(1, 1) 0+1 = 1
#       dfs(2, 1) 0 
#       dfs(1, 2) 1
#   dfs(0, 1) 1+1 = 2
#     dfs(1, 1) = 1
#     dfs(0, 2) 0+1 = 1
#       dfs(1, 2) 1
#       dfs(0, 3) 0
#   
# [[0,1,1],
#  [1,-1,1],
#  [1,1,2]]
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # dfs with DP
        N, M = len(obstacleGrid), len(obstacleGrid[0])

        # O(2^(n*m)) (n*m) cells
        # O(n*m) (n*m) cells using DP
        @cache
        def dfs(i, j):
            if i > N - 1 or j > M - 1 or obstacleGrid[i][j] == 1:
                return 0

            reachedBotRight = i == N - 1 and j == M - 1                
            if reachedBotRight:
                return 1
            
            return dfs(i + 1, j) + dfs(i, j + 1)

        return dfs(0, 0)

            

            
"""

[MK-001] Problem Analysis and Synthesis
☑️✅
[NE] - Insufficient participation to evaluate.


[0] - Poor. Did not demonstrate a full understanding of the problem. Did not ask questions to clarify the problem, or the questions asked were not relevant to better understand it.


[1] - Fair. Developed a partial understanding of the problem. Asked some questions but omitted relevant aspects (such as edge cases, input constraints, usage scenarios, etc.).


[2] - Good. Developed a complete understanding of the problem. Asked pertinent questions and identified edge cases.


[3] - Excellent. Questions considered possible generalizations or more complex scenarios, such as distributed systems or computational bottlenecks not explicitly mentioned (e.g., limited memory).



[MK-002] Communication
☑️✅
[NE] - Insufficient participation to evaluate.


[0] - Poor. Did not incorporate the interviewer’s feedback into the proposed solution or disregarded the suggestions.


[1] - Fair. Did not clearly express some of their ideas. When facing difficulties, they discussed what they were thinking with the interviewer, but at times in a confusing way.


[2] - Good. There were moments when communication wasn’t fully effective, but they managed to convey their ideas. They discussed with the interviewer what they were thinking and which solutions they were considering when encountering problems. They incorporated feedback into the proposed solution, albeit with some difficulty.


[3] - Excellent. Clear and coherent communication. Explained their reasoning to the interviewer, who could follow their decisions. When in doubt, they discussed solutions with the interviewer, sparking technical discussion.



[MK-003] Problem solving
☑️✅
[NE] - Insufficient participation to evaluate.


[0] - Poor. The proposed solution does not produce correct results.


[1] - Fair. Presented a correct solution, albeit not optimized, but was unable to discuss possible improvements.


[2] - Good. Solved the problem in a non-optimized way and was able to discuss with the interviewer how to improve the proposed solution.


[3] - Excellent. Solved the problem in an optimized manner, using appropriate data structures and/or algorithms for the given task.



[MK-004] Testing
☑️✅
[NE] - Insufficient participation to evaluate.


[0] - Poor. Did not create any new test cases.


[1] - Fair. Created test cases capable of catching some edge cases, but not all.


[2] - Good. Created comprehensive test cases that cover the problem’s edge cases.


[3] - Excellent. Created comprehensive test cases that cover the problem’s edge cases.



[MK-005] Debugging
☑️✅
[NE] - Insufficient participation to evaluate.


[0] - Poor. The candidate did not take the initiative to debug the implemented solution. When prompted, they didn’t know how to test or tested ineffectively. The final implementation contains many bugs.


[1] - Fair. The candidate performed debugging proactively but ineffectively, using methods that couldn’t fully verify the implemented code.


[2] - Good. They tested the code proactively and correctly. The final code has few or no minor bugs.


[3] - Excellent. They discussed advanced debugging approaches—techniques and tools for more complex scenarios like distributed systems. The final code has few or no minor bugs.



[MK-006] Fundamentals
☑️✅ 
[NE] - Insufficient participation to evaluate.


[0] - Poor. Showed insufficient knowledge of the fundamentals/concepts covered in the mock.


[1] - Fair. Showed some knowledge of the fundamentals/concepts covered in the mock but had difficulty applying them to solve the proposed problem.


[2] - Good. Demonstrated knowledge of the fundamentals/concepts covered in the mock, using them appropriately to solve the proposed problem, though with some difficulty.


[3] - Excellent. Demonstrated mastery of the fundamentals/concepts covered in the mock, applying them to problem-solving without difficulty.



[MK-007] Complexity Analysis
☑️✅ 
[NE] - Insufficient participation to evaluate.


[0] - Poor. Performed analysis only when prompted, or made mistakes analyzing trivial parts of the code.


[1] - Fair. Performed the analysis proactively, though made an error in part of the analysis.


[2] - Good. Performed the analysis proactively.


[3] - Excellent. Performed the analysis proactively.



[MK-008] Code Structure
☑️✅
[NE] - Insufficient participation to evaluate.


[0] - Poor. Demonstrated significant difficulty translating proposed ideas into code. Shows a lack of familiarity with the language.


[1] - Fair. Shows some familiarity with the language but has difficulty translating ideas into code.


[2] - Good. Translates ideas into code without major difficulties. Writes idiomatic code for the language.


[3] - Excellent. Demonstrates strong fluency in translating ideas into code. Knows specific or advanced features of the language.



"""

# /in/jefersonla
# @jefersonla
# je.myandroid@gmail.com