from functools import lru_cache

class Solution:
    def lengthOfLIS2(self, nums: List[int]) -> int:

        def dfs(i, subset):
            if i == len(nums):
                return len(subset)
            if not subset:
                return dfs(i + 1, [nums[i]])
            
            if nums[i] > subset[-1]:
                return dfs(i + 1, subset[:] + [nums[i]])
            else:
                reducedSubset = subset[:]
                while reducedSubset and reducedSubset[-1] >= nums[i]:
                    reducedSubset.pop()
                return max(dfs(i + 1, subset[:]), dfs(i + 1, reducedSubset + [nums[i]]))
        
        return dfs(0, [])

    def lengthOfLIS(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, subset):
            if i == len(nums):
                return len(subset)
            if not subset:
                return dfs(i + 1, tuple([nums[i]]))
            
            #print(subset)
            if nums[i] > subset[-1]:
                return dfs(i + 1, tuple(list(subset) + [nums[i]]))
            else:
                reducedSubset = list(subset)
                while reducedSubset and reducedSubset[-1] >= nums[i]:
                    reducedSubset.pop()
                return max(dfs(i + 1, subset), dfs(i + 1, tuple(reducedSubset + [nums[i]])))
        
        return dfs(0, ())