# Create a class the allows operations to insert intervals and to query if a value is on the intervals

# Insert
# [1, 3]
# [5, 7]
# [7, 8]
# [9, 10]

# Query
# 4 -> False
# 6 -> True
# 8 -> True

# brute-force approach
# optmization using binary search
# details on insertion (need to merge intervals)
# Q. can you implement insert without sorting? Yes, iterating of the array and finding the correct position to insert
# Q. disregard everything and optimize the query the most, what would you do? create a set of all values in the intervals for O(1) query time
