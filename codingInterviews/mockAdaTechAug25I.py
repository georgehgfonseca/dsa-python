"""
start_data_enginering
start_data_cleaning
start_training

end_data_enginering

start_X -> end_X
[start_data_enginering, start_data_cleaning, end_data_cleaning, end_data_engineering]

[start_data_enginering, end_data_cleaning, end_data_engineering]

start_data_enginering -> start_training -> start_data_validation

["start_data_validation"]


"""
from collections import defaultdict, deque

class Solution:

    def pipelineValidator(steps: List[str], order: List[str]) -> bool:
        stack = []
        orderSet = set(order)
        order = deque(order)

        for step in steps:
            isStart = len(step) >= 6 and step[0:6] == "start_"
            if isStart:
                   stack.append(step[6:])
            else:
                if not stack:
                    return False
                if stack[-1] != step[4:]:
                    return False
                if step in orderSet:
                    if order[0] != step:
                        return False
                    order.popleft()
                stack.pop()
        
        return len(stack) == 0

s = Solution()
testCases = [
    (["start_a", "end_b", "start_b", "end_b", "start_c", "end_c", "start_d", "end_d"], [("end_a", "end_b", "end_c")], True),
    (["start_a", "start_b", "end_b", "end_a"], [("start_b", "start_a")], True),
    (["end_a", "start_b", "end_b", "end_a"], [], False),
    (["start_a", "start_b", "end_a", "end_a"], [], False)
]

for testCase in testCases:
    assertEquals(s.pipelineValidator(testCase[0], testCase[1]), testCase[2])
