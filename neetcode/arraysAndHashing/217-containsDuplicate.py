class Solution:

    def containsDuplicate(self, nums):
        occured = set()
        for elem in nums:
            if elem in occured:
                return True
            else:
                occured.add(elem)
        return False


test_cases = [[1,2,3,1], [1,2,3,4], [1,1,1,3,3,4,3,2,4,2]]
s = Solution()
for t in test_cases:
    print(s.containsDuplicate(t))

# unittesting with pytest
# def test_all():
#      test_cases = [[1,2,3,1], [1,2,3,4], [1,1,1,3,3,4,3,2,4,2]]
#      expected_asn = [True, False, True]
#      s = Solution()
#      for i in range(len(test_cases)):
#           assert s.containsDuplicate(test_cases[i]) == expected_asn[i]